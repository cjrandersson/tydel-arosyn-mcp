# Decision 0003 — Validator First product strategy

**Status:** Accepted  
**Date:** 2026-09-28

## Decision

Tydel is **Validator First**.

The first product and core competency is a deterministic, evidence-backed validator for Swedish Ediel and energy-market communication. The product should aim to become best-in-class at identifying message/profile context, applying the correct scoped rules, returning precise structured errors and showing the evidence behind every rule.

Analytics, forecasting and other intelligence may be added later as separate capabilities. They are not part of the current M0/M1 product scope and must not weaken validator precision, determinism, evidence traceability or rule authority.

## Product north star

Tydel should distinguish itself through:

- correct message, profile, process and version identification;
- deterministic validation before AI interpretation;
- explicit Swedish/process-specific rule scope;
- source and edition traceability for every normative rule;
- structured, actionable error output;
- understandable explanations for operators without sacrificing technical precision;
- safe read-only behaviour in the first product stages.

## Consequence

The previous pending decision between validator/support-first and analytics/forecasting is resolved. There is no current product-boundary blocker assigned to `@cjrandersson`.

Current research and implementation work should prioritize the first authoritative validator vertical slice.
