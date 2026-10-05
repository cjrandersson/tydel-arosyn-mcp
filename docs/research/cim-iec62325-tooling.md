# CIM / IEC 62325 tooling — future research track

> Status: **research / future evaluation**. Updated after the 2026-09-30 DHV checkpoint. This document records standards/tooling signals for Tydel's future XML/CIM capability. It does **not** select a production dependency, make CIM authoritative for Swedish Ediel, or claim that the future Swedish DHV will use IEC 62325.

## Why this matters

Tydel now positions itself as an energy-market conformance and diagnostics engine rather than a permanent Ediel-only validator.

That makes future XML/CIM support strategically relevant, but the implementation sequence remains gated:

```text
M1: Swedish Ediel / UTILTS-APERAK
        ↓
prove Rule IR + RulePack runtime
        ↓
prove developer/customer value
        ↓
one selected XML/CIM market-process slice
```

The architectural goal is one validation/result model across multiple syntax/profile families:

```text
PROCESS
→ MESSAGE / PROFILE
→ SYNTAX
→ VERSION
→ EFFECTIVE PERIOD
→ RULEPACK
→ VALIDATION
→ EVIDENCE
```

Potential families include:

```text
EDIFACT / Ediel
XML / CIM / IEC 62325 / ENTSO-E ESMP
future DHV interface families when officially specified
```

## Post-DHV evidence boundary

The 2026-09-30 Ei/Svenska kraftnät report strengthens the need to avoid permanent Ediel coupling, but it does **not** by itself prove:

- that the Swedish DHV will use IEC 62325;
- which CIM/ESMP profiles may be used;
- which processes migrate to which syntax;
- that all Ediel flows are replaced at once;
- a specific migration date.

Treat those as open until official implementation specifications exist.

## Standards boundary

CIM is a family of information models used across several IEC series. Keep these areas separate:

- **IEC 61970 / CGMES** — primarily grid-model and power-system model exchange.
- **IEC 61968** — distribution-system information exchange use cases.
- **IEC 62325 / ENTSO-E ESMP** — energy-market information exchange and market-message profiles; most directly relevant to Tydel's longer-term market-messaging scope.
- **Swedish / Nordic process rules** — separate market/profile overlays sourced from the appropriate authoritative actors and implementation guides.

Do not infer that a CGMES tool is automatically an IEC 62325 market-message validator.

---

## CIMTool

Sources:

- https://cimtool.ucaiug.io/
- https://github.com/cimug-org/CIMTool

CIMTool is open-source CIM profile/model tooling in the UCAIug/CIMug ecosystem. It is relevant because it can work with contextual profiles and generate machine-readable artifacts.

The CLI / SchemaOps direction is especially relevant as a reference pattern for treating profiles/schemas as versioned reproducible build artifacts.

### Potential future Tydel role

```text
Authoritative CIM / ESMP profile artifact
        ↓
CIMTool or equivalent profile tooling
        ↓
XSD / RDFS / schema/profile metadata
        ↓
Tydel importer
        ↓
Tydel Rule IR
        +
market/process overlay
        ↓
Versioned RulePack
        ↓
Deterministic conformance runtime
```

### Current classification

`REFERENCE / MACHINE-READABLE PROFILE TOOLING / EVALUATE LATER`

CIMTool is not a selected Tydel dependency or validation authority.

---

## OpenCGMES

Sources:

- https://github.com/SOPTIM/OpenCGMES
- https://opencgmes.soptim.de/

OpenCGMES is an Apache-2.0-licensed suite for CGMES / CIM (IEC 61970) RDF workflows.

Documented components include:

- **CIMXML** — Java parsing of IEC 61970-552 CIMXML into Apache Jena RDF graphs, including full and difference models;
- **CIMVocabCheck** — static SPARQL and SHACL validation against RDFS/CIM profile schemas;
- **CIMNotebook** — editor integrations around the same validation tooling.

The project is primarily focused on **CGMES / grid-model exchange**, not directly on IEC 62325 energy-market messages.

### What is useful for Tydel

OpenCGMES is useful as a technical reference for:

- profile-aware schema resolution;
- RDF/RDFS-based CIM representation;
- SHACL constraints;
- deterministic structured validation;
- machine-readable findings;
- CI/editor validation patterns.

A future pattern might be:

```text
CIM / ESMP profile
      ↓
RDFS / schema
      +
SHACL / market constraints where applicable
      ↓
Tydel importer / Rule IR
      ↓
Versioned RulePack
      ↓
Structured Tydel conformance result
```

### Current classification

`REFERENCE / CIM VALIDATION PATTERN / FUTURE EVALUATION`

OpenCGMES is not a planned production dependency at this stage.

---

## Relationship to OpenEDI

The architectural analogy is:

```text
EDIFACT side                    CIM side

OpenEDI / base schema    ↔      CIM / ESMP profile artifacts
Ediel market overlay     ↔      Nordic / market-process overlay
Tydel Rule IR            ↔      Tydel Rule IR
EDIFACT parser            ↔      XML/RDF/CIM parser

                ↓
        VERSIONED RULEPACKS
                ↓
      TYDEL CONFORMANCE RESULT
                ↓
       diagnostics + evidence
```

This is an analogy, not a requirement to force both standards worlds into identical source formats.

---

## Proposed future research spike

Do **not** activate this implementation work before the first Ediel vertical slice is proven.

When the track becomes active:

1. Select one concrete energy-market process.
2. Identify authoritative IEC 62325 / ENTSO-E ESMP profile(s) for that process.
3. Determine which machine-readable schema/profile artifacts are officially available and under what rights.
4. Evaluate profile/schema ingestion into Tydel Rule IR.
5. Evaluate CIMTool where it reduces profile-build/import work.
6. Evaluate XSD/RDFS/SHACL as deterministic constraint sources where appropriate.
7. Use OpenCGMES only as a reference for relevant CIM parsing/validation patterns, not as proof of market-message semantics.
8. Add Swedish/Nordic business-process rules as separately versioned constraints.
9. Test one synthetic market transaction end-to-end.
10. Confirm that the validation-result contract remains stable across the EDIFACT and selected CIM slice.

---

## Guardrails

- No scope creep into M1 solely because CIM tooling exists.
- No claim that IEC 62325 is mandatory for every Swedish market process without process-specific evidence.
- No claim that DHV uses IEC 62325 without an authoritative DHV specification.
- No assumption that IEC/ENTSO-E model artifacts can be redistributed merely because tooling is open source.
- Keep source/profile/version/effective period/provenance explicit for every imported rule.
- Keep the LLM outside validation authority.
- Prefer machine-readable normative artifacts when legally and technically usable, but never treat convenience as authority.
- Keep Tydel Rule IR/runtime independent from CIMTool/OpenCGMES-specific object models.

## Current conclusion

CIMTool and OpenCGMES strengthen the thesis that Tydel can support another standards world without abandoning Validator First.

Near-term:

```text
UTILTS / APERAK
→ Rule IR
→ versioned RulePack
→ deterministic conformance
→ structured evidence-backed diagnostics
```

Later:

```text
Ediel / EDIFACT
        +
selected IEC 62325 / ENTSO-E ESMP / XML-CIM process
        ↓
shared Tydel rule-resolution and validation-result model
```

Future DHV support is attached to authoritative interface specifications when they exist, not to an assumed format today.
