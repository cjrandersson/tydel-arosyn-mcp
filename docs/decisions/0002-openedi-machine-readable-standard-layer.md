# Decision 0002 — Evaluate OpenEDI as machine-readable base standard layer

**Status:** Accepted  
**Date:** 2026-09-25

## Problem

Tydel needs deterministic, versioned and testable knowledge of EDIFACT message structure without manually re-encoding every directory, message, segment and data element from human-readable implementation guides.

The Swedish Ediel layer also needs to remain separate from the generic UN/EDIFACT layer so that national and process-specific rules can be traced to their authoritative sources.

## Decision

Tydel will evaluate the OpenEDI specification as a machine-readable base representation for generic EDI/EDIFACT structure.

The intended layering is:

```text
Raw EDIFACT
    ↓
Tydel parser
    ↓
Canonical message
    ↓
OpenEDI base specification
    ↓
Swedish Ediel / process-profile overlay
    ↓
Tydel deterministic validation rules
    ↓
ValidationResult
    ↓
MCP / operator explanation
```

OpenEDI is not an authority for Swedish Ediel business rules. Svenska kraftnät, eSett and other applicable official publishers remain authoritative for national/profile-specific requirements.

Tydel will not depend on EdiNation's validator at runtime. The goal is to evaluate OpenEDI definitions as structured input to Tydel's own deterministic parser/rules pipeline.

## M0 evaluation spike

Before the first validator vertical slice is locked, Tydel should test whether an OpenEDI model for the candidate EDIFACT message/version can be used to:

1. resolve message, loop, segment, composite and data-element structure;
2. preserve cardinality and ordering;
3. extract datatype/code constraints where available;
4. extract `x-openedi-syntax` and `x-openedi-situational` constraints;
5. map those constraints into Tydel's internal rule model;
6. layer Swedish Ediel-specific rules on top without modifying the generic base model;
7. produce traceable validation output pointing to both the violated rule and its source layer.

## Source and licensing boundary

The OpenEDI specification repository is MIT licensed. That does not automatically establish redistribution rights for every generated or downloadable EDI model in the EdiNation specification library.

Until model-specific reuse/redistribution rights are confirmed, downloaded specification models must be treated as local research inputs (`cache` or `link-only`) rather than vendored public-repository assets.

## Consequences

- Tydel may avoid hand-authoring a large amount of generic EDIFACT structure.
- The generic standard layer and Swedish Ediel overlay remain independently versioned and attributable.
- The canonical schema/rule-engine design must be able to ingest structured specifications without becoming OpenEDI-specific internally.
- OpenEDI remains replaceable. Tydel's internal rule model is the product boundary.

## Revisit when

Revisit this decision after the M0 OpenEDI spike if:

- required Ediel constraints cannot be represented cleanly;
- the selected OpenEDI model is incomplete or inconsistent with official directories;
- licensing prevents the intended development/test workflow;
- importing OpenEDI creates more coupling than manually maintaining the first narrow profile.
