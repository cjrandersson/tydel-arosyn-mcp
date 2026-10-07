# Validator Result Contract v0

**Status:** Locked for M1 contract implementation  
**Date:** 2026-10-07  
**Machine-readable schema:** `schemas/validator-result-v0.schema.json`

## Purpose

Tydel emits one deterministic machine-readable result from the validation core. CLI, CI, GitHub Action, API, UI and MCP must consume this same result rather than inventing their own validation semantics.

For the same input, validation context, exact RulePack version, engine version and optional local state artifact, the deterministic finding set must be stable.

## Locked root shape

```text
schemaVersion
resultId
status
context
rulePack
error[]
execution
```

`status` is exactly `PASS` or `FAIL`.

The field name `error` is intentionally retained for M1 because it is the explicitly approved contract surface, even though it is an array. A `FAIL` result MUST contain at least one item with `severity: ERROR`. A `PASS` result MUST NOT contain an `ERROR`; it may carry `WARNING` items.

## Locked error item

Each item contains:

```text
ruleId
severity
ruleLayer
segmentPath
canonicalPath
observed
expected
provenance[]
originalResponse?
nextStep
```

### `segmentPath`

For M1, input syntax is EDIFACT, so every finding points to the exact segment path in the original file, for example:

```text
UNB[1]/UNH[1]/BGM[1]
```

`canonicalPath` is also required so the result can later survive non-EDIFACT adapters without losing semantic identity.

### `provenance`

Every deterministic market finding carries source provenance. Provenance explicitly distinguishes:

- `NORMATIVE`
- `PROCESS_GUIDE`
- `EXAMPLE`
- `SECONDARY`

Tydel MUST NOT label a process guide or example as normative merely because it is useful evidence.

### `nextStep`

`nextStep` is a safe troubleshooting action. It must not silently modify, reroute or resend a production market message.

## Execution metadata

`execution.durationMs` is measured output only. It MUST NOT be used as proof of the `<15 ms` product target until a reproducible benchmark fixes payload size, active rule count, warm/cold state, hardware, iterations and percentile.

M1 local execution is represented as:

```json
{
  "mode": "LOCAL",
  "offline": true
}
```

## Golden contract fixtures

The first fixtures are:

- `fixtures/m1/validator-result/pass.json`
- `fixtures/m1/validator-result/fail-aperak-313.json`

The negative fixture is deliberately based on source-backed acknowledgement semantics instead of inventing an unverified control-digit or date rule. Svenska kraftnät's FCR implementation guide shows the UTILTS APERAK profile `D:04A:UN:E5SE9B`, with `312` as positive and `313` as negative in Appendix C. Svensk Elmarknadshandbok 26A §10.3.2 states that negative APERAK means the controlled Ediel message is erroneous and must trigger further troubleshooting.

These fixtures lock the result contract and serializer behaviour. They do **not** claim that `TEST_FCR_APERAK_E5SE9B` is a published production RulePack.

## Codex implementation boundary

Codex may now implement:

1. the Validator Result v0 types/model;
2. JSON Schema validation;
3. deterministic serialization;
4. PASS/FAIL invariant tests;
5. the two golden contract fixture tests;
6. CLI/CI exit mapping based on `status`.

Codex MUST NOT yet invent missing UTILTS/APERAK market rules or widen the RulePack scope. The first production M1 RulePack/profile remains a separate evidence-lock task.

## Exit semantics

Initial M1 mapping:

```text
PASS -> process exit 0
FAIL -> process exit 1
contract/schema/runtime failure -> process exit 2
```

Warnings do not change PASS to FAIL unless a verified RulePack rule explicitly has `severity: ERROR`.

## Revisit conditions

Revisit v0 when:

- the first verified M1 RulePack exposes missing result fields;
- a non-EDIFACT adapter proves `segmentPath` needs a generalized source-location envelope;
- stateful validation requires explicit StateSnapshot identity in the root contract;
- design-partner CI requirements need a stronger stable error taxonomy.
