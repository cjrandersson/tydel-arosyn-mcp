# CIM / IEC 62325 tooling — future research track

> Status: **research / future evaluation**. This document records relevant tooling and standards signals for Tydel's future XML/CIM capability. It does **not** change the current M0/M1 implementation scope, select a production dependency, or make CIM authoritative for current Swedish Ediel validation.

## Why this matters

Tydel starts with a narrow deterministic Swedish Ediel validator, but the product architecture is intentionally not tied to EDIFACT forever. Nordic and European energy-market communication increasingly includes XML/CIM-based profiles alongside legacy/current Ediel flows.

The architectural goal is therefore to preserve one validation model across multiple syntax families:

```text
PROCESS
→ MESSAGE / PROFILE
→ SYNTAX
→ VERSION
→ RULESET
→ VALIDATION
→ EVIDENCE
```

Potential syntax/profile families include:

```text
EDIFACT / Ediel
XML / CIM / IEC 62325 / ENTSO-E ESMP
```

This is a **future compatibility track**, not a reason to widen the first validator slice.

## Standards boundary

CIM is a family of information models used across several IEC series, including IEC 61970, IEC 61968 and IEC 62325. They overlap conceptually but serve different use cases.

For Tydel, keep these areas separate:

- **IEC 61970 / CGMES** — primarily grid-model and power-system model exchange.
- **IEC 62325 / ENTSO-E ESMP** — energy-market information exchange and market-message profiles; directly relevant to Tydel's longer-term market-messaging scope.
- **Swedish / Nordic process rules** — remain a separate market/profile overlay and must be sourced from the appropriate authoritative actors and implementation guides.

Do not infer that a CGMES tool is automatically an IEC 62325 market-message validator.

## CIMTool

Source:
- https://cimtool.ucaiug.io/
- https://github.com/cimug-org/CIMTool

CIMTool is an open-source CIM profile/model tooling project maintained in the UCAIug/CIMug ecosystem. It is relevant to Tydel because it can work with contextual CIM profiles and generate machine-readable artifacts such as schema/profile representations.

The project's newer CLI / SchemaOps direction is especially relevant as a reference pattern for treating profiles as versioned, reproducible build artifacts rather than loose documentation.

### Potential Tydel relevance

Possible future role:

```text
Authoritative CIM / ESMP profile artifact
        ↓
CIMTool or equivalent profile tooling
        ↓
XSD / RDFS / JSON Schema / profile metadata
        ↓
Tydel importer
        ↓
Tydel canonical rules
        +
Nordic / Swedish process overlay
        ↓
Deterministic validation
```

### Current classification

`REFERENCE / MACHINE-READABLE PROFILE TOOLING / EVALUATE LATER`

CIMTool is **not** currently a selected Tydel dependency or validation authority.

## OpenCGMES

Sources:
- https://github.com/SOPTIM/OpenCGMES
- https://opencgmes.soptim.de/

OpenCGMES is an Apache-2.0-licensed suite for CGMES / CIM (IEC 61970) RDF workflows. Its current documented components include:

- **CIMXML** — Java parsing of IEC 61970-552 CIMXML into Apache Jena RDF graphs, including full and difference models;
- **CIMVocabCheck** — static SPARQL and SHACL validation against RDFS / CIM profile schemas;
- **CIMNotebook** — editor integrations around the same validation tooling.

The project is primarily focused on **CGMES / grid-model exchange**, not directly on IEC 62325 energy-market messages.

### What is useful for Tydel

OpenCGMES is valuable as a technical reference for:

- profile-aware schema resolution;
- RDF/RDFS-based CIM representation;
- SHACL constraints;
- deterministic structured validation;
- machine-readable validation findings;
- CI/editor validation patterns.

A possible future CIM validation pattern for Tydel could look like:

```text
CIM / ESMP profile
      ↓
RDFS / profile schema
      +
SHACL constraints
      ↓
Deterministic validation
      ↓
Structured violations
      ↓
Tydel evidence + diagnostics
```

### Current classification

`REFERENCE / CIM VALIDATION PATTERN / FUTURE EVALUATION`

OpenCGMES is **not** a planned production dependency at this stage.

## Relationship to OpenEDI

The emerging architectural analogy is:

```text
EDIFACT side                    CIM side

OpenEDI / base schema    ↔      CIM / ESMP profile artifacts
Ediel profile overlay    ↔      Nordic / market-process overlay
Tydel rules              ↔      SHACL/schema + Tydel rules
EDIFACT parser            ↔      XML/RDF/CIM parser

                ↓
      TYDEL CANONICAL VALIDATION RESULT
                ↓
       diagnostics + evidence
```

This analogy is useful, but the technologies are not interchangeable and should not be forced into one representation prematurely.

## Proposed research spike after first Ediel vertical slice

Do **not** start this before the first Swedish validator slice is sufficiently locked.

When the CIM track becomes active:

1. Identify authoritative IEC 62325 / ENTSO-E ESMP profiles relevant to one concrete market process.
2. Determine which machine-readable profile/schema artifacts are officially available and under what rights.
3. Evaluate CIMTool as profile/schema ingestion or build tooling.
4. Evaluate SHACL/RDFS as a deterministic constraint layer where appropriate.
5. Use OpenCGMES as a reference implementation for CIM parsing/profile-aware validation patterns, without assuming CGMES semantics equal market-message semantics.
6. Map external constraints into Tydel's own canonical rule/result model rather than exposing tool-specific contracts.
7. Add Nordic/Swedish process rules as a separately versioned overlay.
8. Test one synthetic market message end-to-end.

## Guardrails

- No scope creep into M0/M1 solely because CIM tooling exists.
- No claim that IEC 62325 is mandatory for every Swedish market process without process-specific evidence.
- No assumption that IEC/ENTSO-E model artifacts can be redistributed merely because tooling around them is open source.
- Keep source/profile/version/provenance explicit for every imported rule.
- Keep the LLM outside validation authority.
- Prefer machine-readable normative artifacts when legally and technically usable, but never treat convenience as authority.

## Current conclusion

CIMTool and OpenCGMES strengthen the thesis that Tydel can eventually support a second standards world without abandoning its Validator First architecture.

The near-term product remains:

```text
Swedish Ediel vertical slice
→ deterministic validation
→ structured evidence-backed diagnostics
```

The future research direction is:

```text
Ediel / EDIFACT
        +
IEC 62325 / ENTSO-E ESMP / XML-CIM
        ↓
shared Tydel validation-result model
```

That future direction is now explicit, but intentionally **not implementation scope yet**.
