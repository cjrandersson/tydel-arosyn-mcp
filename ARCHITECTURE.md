# Tydel architecture

This document explains how Tydel is intended to work and where its boundaries are. It should help contributors understand the system before changing it.

The structure is inspired by [esbuild's architecture documentation](https://github.com/evanw/esbuild/blob/main/docs/architecture.md): start with the whole system, state the design principles, then explain each stage. Tydel is still an experiment in progress. The current design is a direction, not proof that every choice is final.

## Design principles

### Keep the truth outside the language model

Parsing and validation must be deterministic, versioned and testable. An LLM may explain a result, but it must not invent a rule or silently change the validation outcome.

### Separate base standards from market profiles

Generic UN/EDIFACT structure and Swedish Ediel / market-process rules are different evidence layers and must remain independently versioned and attributable.

A machine-readable base model may describe the generic message structure. It does not become authoritative for Swedish business rules merely because it is easier for software to consume.

### Keep external specification formats replaceable

OpenEDI is being evaluated as an input format for generic EDI/EDIFACT structure. Tydel's canonical message model and internal validation-rule model must not become dependent on OpenEDI-specific field names or on an external validation service.

### Do as little work as possible

Parse each message once and pass a shared structured model through later stages. Avoid repeated conversions between raw EDIFACT, text summaries and tool-specific formats.

### Make every stage observable

Each stage should return a structured result with timing, rule version and trace information. A failed run should be possible to replay without contacting a production system.

### Start read-only

The first integrations consume copies of messages, errors and logs. Inline routing, correction and retransmission are separate future capabilities with a much higher risk level.

### Keep adapters replaceable

SFTP, file imports, APIs, AS2 and HTTPS are possible ways to receive data. They belong in adapters and must not shape the core validation model.

### Grow from one working path

The first goal is one complete path: load one supported message type, parse it, validate it and return a useful error through MCP. New message types and services come after this works.

## System overview

```mermaid
flowchart TD
    A["Copied messages + logs"]:::input --> B["Input adapter"]:::adapter
    B --> C["Parser"]:::core
    C --> D["Canonical message"]:::data
    D --> E["Base standard model"]:::standard
    E --> F["Ediel / process overlay"]:::standard
    F --> G["Rules engine"]:::core
    G --> H["Validation result"]:::data
    H --> I["Context service"]:::core
    I --> J["MCP tools + resources"]:::mcp
    J --> K["AI client / operator UI"]:::mcp
    I --> L["Audit + alert workflow"]:::action

    classDef input fill:#EAF4FF,stroke:#4C8DFF,color:#102A43,stroke-width:1.5px;
    classDef adapter fill:#EEF7FF,stroke:#60A5FA,color:#102A43,stroke-width:1.5px;
    classDef core fill:#EAFBF4,stroke:#22A06B,color:#12372A,stroke-width:1.5px;
    classDef data fill:#F5F7FA,stroke:#7B8794,color:#25313C,stroke-width:1.5px;
    classDef standard fill:#FFF9E8,stroke:#C99500,color:#4A3800,stroke-width:1.5px;
    classDef mcp fill:#F3EEFF,stroke:#7A5AF8,color:#2D1B69,stroke-width:1.5px;
    classDef action fill:#FFF4E5,stroke:#F59E0B,color:#5F370E,stroke-width:1.5px;
```

## Main stages

### 1. Input

An adapter receives a copied message, a file upload or a recorded error. It records where the data came from and when it was received.

The core must not assume a specific transport.

### 2. Parse

The parser turns EDIFACT syntax into a canonical message model. It preserves the original content and source positions so every result can point back to the exact segment and element.

A syntax problem returns a structured parse error. It must not crash the process.

The parser is a Tydel component. Importing a machine-readable standard model does not remove the need to parse raw EDIFACT correctly.

### 3. Resolve the base standard

Tydel resolves the generic message structure for the named EDIFACT message/version.

OpenEDI is currently the preferred candidate for the M0 evaluation because it can express EDI messages, loops, segments, composites, data elements, occurrence constraints, syntax rules and situational rules as OpenAPI Schema Objects with EDI-specific extensions.

The base-standard importer must translate any external representation into Tydel's own internal rule model. The rules engine should not need to know whether a base rule originally came from OpenEDI, a manually curated definition or another future source.

Every imported constraint must preserve provenance such as:

- source identifier;
- publisher;
- model/version/edition;
- exact schema object or rule location;
- checksum of the exact local source bytes when applicable.

### 4. Apply the Ediel / process overlay

Swedish Ediel and business-process constraints are applied as a separately versioned overlay.

The overlay can tighten, specialize or add constraints, but it must not silently mutate the stored generic base model.

Each rule should be classifiable as one of at least:

- `BASE_STANDARD`;
- `SWEDISH_PROFILE`;
- `BUSINESS_PROCESS`;
- `TYDEL_SAFETY`.

The authoritative source for Swedish/profile-specific rules remains the applicable official market documentation, not OpenEDI or EdiNation.

### 5. Validate

The rules engine checks the canonical message against the resolved, named and versioned rule set.

Rules may cover:

- message structure;
- required segments and values;
- code lists;
- field types and formats;
- segment/data-element occurrence;
- generic EDIFACT syntax/situational rules;
- Ediel-specific business rules that we are legally allowed to implement.

The output is a machine-readable validation result. Plain-language text is not the primary result.

A useful error should be able to identify:

- message and version;
- exact segment/element position;
- stable Tydel rule ID;
- rule layer;
- expected versus observed value/state;
- provenance/evidence for the rule.

### 6. Build context

The context service combines the validation result with approved references and authorized operational metadata. It must label what was observed, what was looked up and what is still unknown.

### 7. Expose through MCP

The MCP server exposes narrow tools such as:

- `validate_message`
- `get_validation_result`
- `explain_error_context`
- `find_reference`

Specifications and code lists can be exposed as resources. Tool results should include structured content, evidence and stable error codes.

### 8. Present and act

An AI client or operator UI turns the structured result into an explanation. Notifications are controlled workflows outside the validation core.

No production correction, retransmission or other write action belongs in the first version.

## OpenEDI boundary

The accepted M0 decision is to **evaluate**, not blindly adopt, OpenEDI.

The intended relationship is:

```text
OpenEDI / other external schema
          ↓ import
Tydel internal base rules
          +
Swedish Ediel / process overlay
          ↓
Resolved Tydel rule set
```

Tydel must not:

- call an external EdiNation validator and treat its response as Tydel's validation result;
- assume that machine-readable OpenEDI models are authoritative for Swedish market usage;
- expose OpenEDI-specific implementation details as the public validator contract;
- vendor downloadable models into the public repository without model-specific rights review.

See [`docs/research/openedi-evaluation.md`](docs/research/openedi-evaluation.md) and [`docs/decisions/0002-openedi-machine-readable-standard-layer.md`](docs/decisions/0002-openedi-machine-readable-standard-layer.md).

## System boundaries

Tydel is not:

- an Ediel replacement;
- a central market platform;
- an EDI transport network;
- a grid-control system;
- a forecasting system in the first product;
- an authority on compliance;
- an EdiNation wrapper.

Existing EDI systems and market platforms remain authoritative.

## Planned code layout

This layout will be created as implementation begins:

```text
src/
  adapters/       Input and external-system adapters
  domain/         Canonical message and validation types
  parser/         EDIFACT parsing
  standards/      External base-standard import and normalization
  rules/          Internal versioned rules + Ediel/process overlays
  context/        Evidence and operational context
  mcp/            MCP tools, resources and transport
  audit/          Trace and audit events
  app/            Composition and startup
tests/
  unit/
  integration/
fixtures/
  edifact/
```

Folders should follow real module boundaries. We will not create empty source folders before the first vertical slice defines what they need.

## Data rules

- Store the original message separately from derived explanations.
- Never put secrets or production certificates in the repository.
- Use synthetic or properly anonymized fixtures.
- Give rule sets and reference documents explicit versions.
- Keep evidence links with every generated explanation.
- Keep generic base rules separate from Swedish/profile overlays.
- Preserve the checksum/version of external machine-readable models used to derive rules.
- Treat missing context as unknown, not as permission to guess.

## Decisions still open

- Which message type/profile should be supported first?
- Does the OpenEDI model for that exact message/version contain enough semantics for the first vertical slice?
- What is the final canonical message schema?
- What is the final internal rule representation?
- Which official specifications can be stored or indexed legally?
- Which downloaded OpenEDI models, if any, can be redistributed or vendored legally?
- Which MCP transport and authentication model fit the first deployment?
- What data must remain at the customer's site?

Answers that affect the architecture should be recorded in [`docs/decisions/`](docs/decisions/).
