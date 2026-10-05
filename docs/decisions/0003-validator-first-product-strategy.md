# Decision 0003 — Validator First product strategy

**Status:** Accepted, reaffirmed and broadened by Decision 0005  
**Original date:** 2026-09-28  
**Reaffirmed:** 2026-10-05

## Decision

Tydel is **Validator First**.

The first product and core competency is deterministic, evidence-backed validation of energy-market communication. Swedish Ediel is the first wedge and the first implementation remains intentionally narrow.

After the 2026-09-30 DHV report, `Validator First` must **not** be interpreted as "Tydel is permanently an Ediel-only validator".

Decision 0005 defines the broader category as **Energy Market Conformance & Diagnostics** and makes rule resolution, versioned RulePacks, temporal validity and provenance the long-term core.

Analytics, forecasting and other intelligence may be added later as separate capabilities. They are not part of the current M0/M1 scope and must not weaken validator precision, determinism, evidence traceability or rule authority.

## Product north star

Tydel should distinguish itself through:

- correct market/process/message/profile/version identification;
- deterministic validation before AI interpretation;
- explicit market/process-specific rule scope;
- source, edition and effective-period traceability for every normative rule;
- structured, actionable error output;
- understandable explanations without sacrificing technical precision;
- safe read-only behaviour in the first product stages;
- the ability to preserve and resolve historical rule versions.

## Consequence

The previous pending decision between validator/support-first and analytics/forecasting remains resolved.

Current implementation work should prioritize the first authoritative validator vertical slice. Broader format compatibility is an architectural constraint, not permission to implement every future protocol in M1.

See [`0005-post-dhv-conformance-strategy.md`](0005-post-dhv-conformance-strategy.md) for the post-DHV product and architecture reset.
