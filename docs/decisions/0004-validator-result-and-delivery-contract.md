# Decision 0004 — Validation result and delivery contract

**Status:** Accepted; M1 field names locked  
**Original date:** 2026-09-28  
**Refined:** 2026-10-05  
**M1 contract locked:** 2026-10-07

## Problem

Tydel must explain the same conformance finding to different audiences without creating competing versions of truth.

An operator needs a clear next step, an integration team needs technical detail, a system needs stable machine-readable data and an AI client needs controlled access to the same verified result and evidence.

The result contract must also survive expansion beyond Ediel without becoming tied to EDIFACT field names.

## Decision

Tydel produces **one canonical structured validation/conformance result**. It is the source of truth for every presentation and access surface.

A finding should be able to answer:

1. **What failed?**
2. **Where in the original input is it?**
3. **Why is it invalid for this process/profile/version?**
4. **Which rule applied at the relevant point in time?**
5. **What normative evidence supports the rule?**
6. **What was expected and observed?**
7. **What is a safe next investigation step?**
8. **What original market acknowledgement/error signal exists, if any?**

### Preserve original market signals

Tydel preserves original acknowledgement/error codes and responses when present.

Example:

```text
Original response: APERAK 313
Tydel finding code: TYD-ACK-001
```

A Tydel code normalises diagnostics. It does not replace the original market response.

## Contract direction

M1 field names are now locked by:

- `docs/architecture/validator-result-v0.md`
- `schemas/validator-result-v0.schema.json`
- `fixtures/m1/validator-result/pass.json`
- `fixtures/m1/validator-result/fail-aperak-313.json`

The canonical result supports at least:

```json
{
  "result_id": "...",
  "code": "TYD-REF-004",
  "severity": "error",
  "jurisdiction": "SE",
  "process": "...",
  "message_or_profile": "UTILTS / E5SE5A",
  "syntax": "EDIFACT",
  "resolved_rulepack": "SE_EDIEL_UTILTS_E5SE5A_REV3",
  "as_of": "2026-09-01",
  "location": {
    "source_path": "...",
    "raw_reference": "RFF+..."
  },
  "original_response": "APERAK 313",
  "rule_id": "SE-...",
  "rule_layer": "MARKET_PROFILE",
  "expected": "...",
  "observed": "...",
  "evidence": [
    {
      "source_id": "...",
      "edition": "...",
      "location": "...",
      "effective_from": "...",
      "effective_to": null
    }
  ],
  "next_action": "..."
}
```

For the EDIFACT-only M1 slice, the locked error item includes an exact `segmentPath` plus a semantic `canonicalPath`. The former gives developers an exact wire location such as `UNB[1]/UNH[1]/BGM[1]`; the latter prevents rule identity from becoming permanently EDIFACT-bound. A later non-EDIFACT slice may generalize source-location representation without changing the deterministic finding semantics.

A `FAIL` result must contain at least one `ERROR`. A `PASS` result must not contain an `ERROR`; warnings may coexist with `PASS`.

## Determinism requirement

For the same:

```text
raw input
+ explicit/resolved validation context
+ exact RulePack version
```

Tydel must return the same conformance result.

Human explanations and AI summaries may change wording. The underlying result may not.

## Audience-specific delivery

| Audience | Primary need | Potential surface |
| --- | --- | --- |
| Operator/support | clear finding, source, impact, next step | Web/operator UI |
| Integration/developer | profile/version, exact rule, expected/observed, provenance | CLI + API + technical UI |
| CI/build system | stable machine result and exit status | CLI/API/CI runner |
| AI/client agent | controlled access to verified findings/evidence | MCP |
| Team lead/governance | history, rule/version changes, migration impact | later enterprise layer |
| Market counterparty | official market message/acknowledgement | existing market infrastructure, not Tydel internal protocol |

All surfaces consume the same result contract.

## System boundary

In the first product stages Tydel works read-only beside production flows:

```text
MARKET SYSTEM / INTEGRATION
        │
        ├── production flow continues through official channel
        │
        └── copy / fixture / log / test payload
                    ↓
             TYDEL CONFORMANCE CORE
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
         CLI       API       UI/MCP
```

Tydel does not automatically correct, reroute or retransmit production transactions in this phase.

## Finding-code namespaces

Initial direction:

```text
TYD-SYN-xxx    syntax/parse
TYD-CTX-xxx    unresolved/ambiguous context
TYD-PRO-xxx    profile/version/rulepack resolution
TYD-STR-xxx    structural rule
TYD-DAT-xxx    data/value constraint
TYD-BIZ-xxx    business/process rule
TYD-ACK-xxx    acknowledgement
TYD-REF-xxx    reference/correlation
TYD-TIME-xxx   temporal/period
TYD-ROLE-xxx   actor/role
TYD-EVD-xxx    evidence/provenance problem
```

The exact catalogue is defined with the M1 contract and golden fixtures.

## Change Impact compatibility

Future RulePack comparison must be able to reference stable `rule_id` values and distinguish:

- rule added;
- rule removed;
- rule semantics changed;
- scope/effective period changed;
- evidence/source changed.

Stable rule identity is therefore part of the broader product architecture.

## Consequences

- One authoritative result format serves UI/API/CLI/CI/MCP.
- The result contract is market/syntax-neutral while retaining syntax-specific source locations.
- Original market signals remain visible.
- Temporal rule resolution and RulePack identity are explicit.
- AI explanations cannot alter deterministic findings.
- New delivery surfaces do not require new business logic.

## Revisit when

- the M1 validator contract is implemented and tested;
- the first non-EDIFACT vertical slice exposes missing abstractions;
- a design partner requires inline/write-back behaviour;
- Change Impact needs stronger stable-rule identity semantics;
- official DHV or another market infrastructure defines a validation/result model Tydel needs to interoperate with.
