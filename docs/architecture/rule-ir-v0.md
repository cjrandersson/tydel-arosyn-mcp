# Tydel Rule IR v0

**Status:** Locked for M1 implementation  
**Date:** 2026-10-05  
**Scope:** Internal deterministic rule representation, first exercised by the UTILTS/APERAK M1 slice

## Purpose

Rule IR is Tydel's internal, tool-neutral representation of an executable conformance rule.

It exists to separate four things that must never collapse into each other:

```text
normative source
      ↓
curated/imported interpretation
      ↓
Rule IR
      ↓
versioned RulePack
      ↓
deterministic runtime
```

Rule IR is **not** a user-facing DSL, not a copy of an external schema language and not permission for arbitrary executable code inside a rule.

The v0 contract is intentionally small. It is designed to be sufficient for the first UTILTS/APERAK vertical slice while making unsupported rule semantics visible instead of hiding them in bespoke runtime code.

---

## Design goals

Rule IR v0 MUST be:

- deterministic;
- serialisable as JSON/YAML;
- independent of OpenEDI, XSD, SHACL, CIMTool or any future DHV representation;
- explicit about jurisdiction, process, profile/version and effective period;
- traceable to source evidence;
- testable with positive and negative fixtures;
- safe to diff between RulePack versions;
- unable to execute arbitrary scripts or LLM-generated logic;
- able to report `UNSUPPORTED_RULE_SEMANTICS` when the runtime cannot faithfully represent a verified rule.

Rule IR v0 MUST NOT become a generic policy language during M1.

---

## Top-level RuleIR record

```yaml
schema_version: tydel.rule-ir/v0
rule_id: SE.EDIEL.UTILTS.EXAMPLE.001
title: Example scoped rule
layer: MARKET_PROFILE
severity: error

scope:
  jurisdiction: SE
  market: electricity
  process: example-process
  transaction: null
  message: UTILTS
  profile: E5SE5A
  message_version: D02B
  syntax: EDIFACT
  actor_roles: []

applicability:
  effective_from: 2026-10-01
  effective_to: null

selector:
  model: canonical
  path: document.example_field

assertion:
  kind: allowed_value
  values:
    - EXAMPLE

evidence:
  - source_id: se-ediel-3364
    publisher: Svenska kraftnät / Edielportalen
    evidence_level: NORMATIVE
    source_edition: revision-4
    source_location: "section/page to be recorded during rule extraction"
    source_checksum: null
    note: "Illustrative shape only; this record is not a published validator rule."

review:
  status: candidate
  reviewed_by: []
  reviewed_at: null
  notes: null

tests:
  positive: []
  negative: []

execution:
  support: supported
```

The example above demonstrates the contract only. It MUST NOT be treated as a normative UTILTS rule.

---

## Stable identity

### `schema_version`

For this contract:

```text
tydel.rule-ir/v0
```

Changing the semantics of an existing field requires a new Rule IR schema version.

### `rule_id`

A stable Tydel identifier. It MUST NOT encode mutable prose such as a human-readable title.

Recommended structure:

```text
<JURISDICTION>.<FAMILY>.<MESSAGE/PROCESS>.<CATEGORY>.<NUMBER>
```

The exact naming convention can evolve, but once a published RulePack contains a `rule_id`, that identifier must remain stable across non-semantic editorial changes.

---

## Rule layers

`layer` is one of:

```text
BASE_STANDARD
MARKET_PROFILE
BUSINESS_PROCESS
TYDEL_SAFETY
```

Meaning:

- `BASE_STANDARD`: generic structural/syntax constraints independent of Swedish market usage;
- `MARKET_PROFILE`: explicit market/profile constraints, for M1 primarily Swedish Ediel profile rules;
- `BUSINESS_PROCESS`: process/state/correlation rules that depend on market workflow context;
- `TYDEL_SAFETY`: Tydel-side validation safety constraints, clearly separated from normative market authority.

A Tydel safety rule MUST NOT be presented as an official market rule.

---

## Scope

Every executable rule has explicit scope.

```yaml
scope:
  jurisdiction: SE
  market: electricity
  process: meter-data
  transaction: null
  message: UTILTS
  profile: E5SE5A
  message_version: D02B
  syntax: EDIFACT
  actor_roles: []
```

Fields may be `null` only when the rule is genuinely broader and the source supports that breadth.

Missing scope is never interpreted as global applicability.

The resolver may refuse to select a rule when required context is unknown or ambiguous.

---

## Temporal applicability

```yaml
applicability:
  effective_from: 2026-10-01
  effective_to: null
```

Dates use ISO-8601 calendar dates unless the authoritative source requires finer precision.

Rules are selected against an explicit validation `as_of` value.

Rules from older editions remain addressable after a new edition becomes current. Publication of a new RulePack never mutates an already-published historical RulePack.

---

## Selectors

Rule IR v0 evaluates rules against Tydel's canonical transaction/context, not directly against arbitrary parser-specific object shapes.

```yaml
selector:
  model: canonical
  path: document.reference.original_message_id
```

`path` is a stable canonical field path defined by the supported M1 contract.

The parser separately preserves source locations so a finding can map the canonical target back to the exact EDIFACT segment/data element.

### Why not raw EDIFACT paths in the core rule?

A market rule may survive a future syntax migration even when its wire representation changes. Keeping the assertion bound to canonical meaning prevents the Rule IR from becoming an EDIFACT-only language.

M1 may still store syntax-specific source hints outside the assertion for diagnostics.

---

## Assertion primitives

Rule IR v0 locks the following primitive families.

### `presence`

Target must exist or must be absent.

```yaml
assertion:
  kind: presence
  required: true
```

### `cardinality`

```yaml
assertion:
  kind: cardinality
  min: 1
  max: 1
```

`max: null` means unbounded only when the source explicitly supports it.

### `datatype`

```yaml
assertion:
  kind: datatype
  type: string
```

Initial types:

```text
string
integer
decimal
boolean
date
datetime
```

Wire-format parsing rules remain in the format adapter/base-standard layer where appropriate.

### `pattern`

```yaml
assertion:
  kind: pattern
  regex: "^[A-Z0-9]+$"
```

Patterns must be deterministic and use a runtime-supported regular-expression subset. Pattern semantics must not depend on locale or external network state.

### `allowed_value`

```yaml
assertion:
  kind: allowed_value
  values:
    - A
    - B
```

### `code_list`

```yaml
assertion:
  kind: code_list
  code_list_id: SE.EDIEL.EXAMPLE.CODES.V1
```

Code lists are versioned artifacts with their own provenance and effective periods. Large code lists should not be duplicated inline across rules.

### `equals`

Compare the selected target with a literal value.

```yaml
assertion:
  kind: equals
  value: S01
```

### `reference_equals`

Compare the selected target with another canonical field.

```yaml
assertion:
  kind: reference_equals
  other_path: document.original_message_id
```

This primitive exists for correlation/reference integrity without introducing a general expression language.

### `conditional_presence`

A restricted conditional primitive.

```yaml
assertion:
  kind: conditional_presence
  when:
    path: document.message_type
    operator: equals
    value: EXAMPLE
  then:
    path: document.reference
    required: true
```

`when.operator` in v0 is limited to:

```text
equals
not_equals
exists
not_exists
in
```

Nested arbitrary boolean expression trees are intentionally excluded from v0.

### `sequence`

Used only when ordering is itself normatively significant in the supported canonical sequence.

```yaml
assertion:
  kind: sequence
  before: document.a
  after: document.b
```

### `temporal_relation`

For deterministic relations between two canonical timestamps/periods.

```yaml
assertion:
  kind: temporal_relation
  left_path: period.start
  operator: before_or_equal
  right_path: period.end
```

Initial operators:

```text
before
before_or_equal
after
after_or_equal
equal
```

### `business_state`

`business_state` is **not** an arbitrary callback. It identifies a separately specified finite-state rule known to the runtime.

```yaml
assertion:
  kind: business_state
  model_id: SE.EXAMPLE.PROCESS.V1
  transition: replace_previous_document
```

A new `model_id` requires explicit architecture/review support and tests. M1 must not use `business_state` as an escape hatch for logic that should be represented with simpler primitives.

---

## Explicit non-feature: arbitrary expressions

Rule IR v0 does not support:

- embedded JavaScript/TypeScript/Python;
- arbitrary Rego/CEL/JMESPath execution;
- LLM-generated executable predicates;
- network calls;
- filesystem access;
- dynamic imports;
- opaque "custom validator" callbacks hidden in a RulePack.

If a verified normative rule cannot be represented, use:

```yaml
execution:
  support: unsupported
  reason: "semantic gap description"
```

A RulePack cannot claim complete conformance for a scope while a mandatory rule in that scope is `unsupported`.

This is deliberate. Unsupported semantics are product evidence, not something to conceal.

---

## Evidence and provenance

Every normative executable rule must contain at least one evidence record.

```yaml
evidence:
  - source_id: se-ediel-3364
    publisher: Svenska kraftnät / Edielportalen
    evidence_level: NORMATIVE
    source_edition: revision-4
    source_location: "page/section"
    source_checksum: "sha256:..."
    note: null
```

`evidence_level` is one of:

```text
NORMATIVE
PROCESS_GUIDE
EXAMPLE
SECONDARY
```

A rule may use several evidence records, but an `EXAMPLE` alone cannot establish a normative market constraint.

Rule execution never depends on free-text `note`.

---

## Review state

```yaml
review:
  status: verified
  reviewed_by:
    - reviewer-id
  reviewed_at: 2026-10-05
  notes: null
```

States:

```text
candidate
verified
rejected
deprecated
```

Only `verified` normative rules may enter a published M1 RulePack.

Review metadata is audit information, not authority by itself. Source authority remains separate.

---

## Test linkage

Every published executable rule should link at least one positive and one negative test where meaningful.

```yaml
tests:
  positive:
    - fixture-id-valid-001
  negative:
    - fixture-id-invalid-001
```

A rule whose semantics cannot be exercised with a deterministic fixture should be reviewed explicitly before publication.

---

## Execution support state

```yaml
execution:
  support: supported
```

Allowed values:

```text
supported
unsupported
not_applicable
```

`unsupported` is a hard visibility mechanism. It must surface in RulePack publication/validation coverage reports.

---

# RulePack v0 envelope

Rule IR records are distributed/executed through a versioned RulePack.

```yaml
schema_version: tydel.rulepack/v0
pack_id: SE_EDIEL_UTILTS_E5SE5A_REV4
pack_version: 0.1.0
status: draft

scope:
  jurisdiction: SE
  market: electricity
  process: null
  message: UTILTS
  profile: E5SE5A
  message_version: D02B
  syntax: EDIFACT

applicability:
  effective_from: 2026-10-01
  effective_to: null

sources:
  - source_id: se-ediel-3364
    edition: revision-4
    checksum: null

rules: []

publication:
  published_at: null
  content_hash: null
```

The example envelope expresses identity only. It does not claim that a complete revision-4 RulePack has been extracted yet.

## Immutability

Once `status: published`:

- `pack_id + pack_version` content is immutable;
- corrections require a new `pack_version`;
- changes in normative market edition normally produce a distinct pack identity/version mapping;
- historical packs remain resolvable for historical `as_of` validation.

Cryptographic signing is deferred. Content hashing is planned but not required to implement the first runtime contract.

---

## Validation result linkage

A finding produced by Rule IR v0 must preserve:

```text
rule_id
rulepack_id
rulepack_version
rule_layer
validation_as_of
canonical_path
source_location_in_input
expected
observed
evidence references
effective period
```

Human explanation is derived after this result exists.

---

## M1 implementation contract

Codex/runtime implementation may begin against Rule IR v0 only after the supported UTILTS/APERAK profile is explicitly locked and verified rules are mapped into the contract.

The runtime must:

1. load a RulePack deterministically;
2. reject incompatible `schema_version` values;
3. resolve rules for `as_of`;
4. skip rules outside their effective period;
5. refuse to silently execute `unsupported` semantics;
6. evaluate supported primitives without network access;
7. return stable structured findings;
8. preserve source-location mappings from canonical fields to original input;
9. produce the same findings for the same input + context + RulePack;
10. expose coverage: supported rules / unsupported mandatory rules / executed rules.

---

## v0 acceptance criteria

Rule IR v0 is considered architecture-complete when:

- the contract above is committed and versioned;
- a machine-readable schema mirrors the contract;
- at least one real supported profile can be mapped without arbitrary rule callbacks;
- semantic gaps are represented explicitly rather than hidden in code;
- RulePack temporal/version identity is testable;
- Claude/peer review can challenge the abstraction before M1 runtime implementation.

The first three items after the contract itself belong to the next M0 task: populate and verify the actual UTILTS/APERAK RulePack and validator contract.

---

## Revisit conditions

Revisit Rule IR v0 if:

- normative UTILTS/APERAK rules require repeated bespoke runtime code;
- more than a small minority of mandatory rules remain `unsupported`;
- a second syntax/profile family cannot map to the same semantic primitives without distortion;
- change-impact needs cannot distinguish semantic from editorial rule changes;
- performance measurements show the representation itself is a material bottleneck;
- a custom DSL becomes justified by measured authoring/review needs rather than architectural preference.
