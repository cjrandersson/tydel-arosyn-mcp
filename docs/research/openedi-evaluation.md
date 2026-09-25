# OpenEDI evaluation for Tydel

**Status:** M0 research spike  
**Owner:** ChatGPT → Codex implementation support after scope lock  
**Date:** 2026-09-25

## Why this matters

Tydel needs a machine-readable representation of generic EDIFACT structure so that the validator does not depend on manually retyping every message directory into application code.

OpenEDI extends OpenAPI Schema Objects with EDI-specific attributes for messages, loops, segments, composites, elements, syntax rules and situational rules. That makes it a candidate input format for Tydel's generic standard layer.

The key architectural principle remains:

> Generic UN/EDIFACT structure and Swedish Ediel business/profile rules are separate evidence layers.

## Hypothesis

A suitable OpenEDI model can provide most of the generic structural constraints for the first selected EDIFACT message/version, while Tydel applies Swedish Ediel-specific constraints as a separately versioned overlay.

If true, the first validator can be built around a reusable rule importer rather than a message-specific hard-coded object graph.

## Evaluation target

The spike should use the same candidate message/version selected for Tydel's first Swedish validator vertical slice. Do not select a different message merely because a convenient OpenEDI sample exists.

## Required tests

### 1. Load and resolve

- Load the OpenEDI JSON definition.
- Resolve internal OpenAPI `$ref` references.
- Identify the requested message ID and edition/release.
- Fail explicitly on missing/ambiguous message/version identifiers.

### 2. Structural extraction

Confirm that Tydel can deterministically extract:

- message identity and version;
- ordered loops/segment groups;
- ordered segments;
- minimum/maximum occurrence;
- composites;
- data-element positions;
- primitive type/length/pattern constraints where present;
- enumerated/code values where present.

### 3. Rule extraction

Inspect and map:

- `x-openedi-syntax`;
- `x-openedi-situational`;
- Not Used / conditional required / exclusion semantics;
- any additional ordering/sequence metadata required for EDIFACT.

Every imported rule must receive a stable Tydel rule ID and provenance pointer to the exact imported schema object.

### 4. Swedish overlay

Compare the generic model with the authoritative Swedish implementation guide/profile.

Classify each first-slice rule as one of:

- `BASE_STANDARD` — generic EDIFACT/OpenEDI-derived constraint;
- `SWEDISH_PROFILE` — national/profile-specific constraint;
- `BUSINESS_PROCESS` — process-specific rule derived from an authoritative market guide;
- `TYDEL_SAFETY` — parser/runtime guardrail, not an external compliance rule.

The Swedish overlay must not rewrite the imported base file. It should add/override constraints in Tydel's own rule representation with explicit provenance.

### 5. Validation output

A failing synthetic message should be able to produce a result equivalent to:

```json
{
  "status": "invalid",
  "messageType": "APERAK",
  "messageVersion": "D04A",
  "ruleId": "...",
  "layer": "SWEDISH_PROFILE",
  "segment": "...",
  "element": "...",
  "expected": "...",
  "observed": "...",
  "source": {
    "publisher": "...",
    "edition": "...",
    "section": "..."
  }
}
```

Exact fields remain to be locked in the validator contract.

## Success criteria

The spike passes if:

1. one real candidate EDIFACT message/version can be imported without hand-authoring its full generic structure;
2. Tydel can generate deterministic internal rules from the imported model;
3. Swedish/profile-specific rules can be layered independently;
4. a positive synthetic fixture passes and intentionally broken fixtures fail at the expected segment/element/rule;
5. every result can explain whether the rule came from base standard, Swedish profile, business process or Tydel safety logic;
6. the runtime validator is not dependent on an EdiNation validation service.

## Failure / stop criteria

Do not force OpenEDI into the architecture if:

- the required message/version is materially incomplete;
- crucial EDIFACT semantics are lost during import;
- official Swedish profile rules cannot be represented cleanly as overlays;
- rights/licensing prevent a reproducible development workflow;
- a simple first-slice hard-coded representation would be substantially safer and easier while preserving future migration.

## Licensing / storage rule

The OpenEDI specification itself is MIT licensed. Downloadable EDI models must be reviewed separately before redistribution.

Until cleared:

- record the source URL and version;
- keep downloaded models in the local Git-ignored reference cache;
- checksum the exact bytes used for evaluation;
- do not vendor them into the public repository;
- do not treat availability on the web as permission for model training, redistribution or sublicensing.

## Expected output

At the end of the spike, publish a short decision note with:

- selected message/version;
- OpenEDI model/source used;
- compatibility findings;
- missing semantics;
- rule-layer mapping examples;
- licensing/storage conclusion;
- recommendation: `ADOPT`, `ADOPT_WITH_LIMITS`, or `DO_NOT_ADOPT` for the first validator slice.
