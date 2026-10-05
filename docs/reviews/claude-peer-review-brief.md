# Claude peer review brief — Tydel M0 post-DHV reset

**Review target:** entire public repository  
**Repository:** `cjrandersson/tydel-arosyn-mcp`  
**Milestone:** M0 — Research foundation + post-DHV product reset  
**Review type:** independent architecture / research / product / commercial-consistency review

## Read first

1. `project-status.yml`
2. `README.md`
3. `ARCHITECTURE.md`
4. `AGENTS.md`
5. `docs/architecture/rule-ir-v0.md`
6. `schemas/rule-ir-v0.schema.json`
7. `docs/decisions/0003-validator-first-product-strategy.md`
8. `docs/decisions/0005-post-dhv-conformance-strategy.md`
9. `docs/decisions/0006-rule-ir-v0.md`
10. `docs/decisions/0007-local-first-developer-conformance.md`
11. `docs/product/positioning.md`
12. `docs/product/post-dhv-roadmap.md`
13. `docs/product/customer-discovery.md`
14. `docs/research/dhv-strategic-watch.md`
15. `docs/research/utilts-aperak-current-evidence.md`
16. `docs/research/cim-iec62325-tooling.md`
17. `docs/research/openedi-evaluation.md`
18. `docs/research/reading-guide.md`
19. `reference/README.md` and relevant source catalogues

## Important current-state facts

- Tydel is still in M0. There is no finished production validator or MCP service.
- The product strategy remains **Validator First**, but Decision 0005 broadens the category to **Energy Market Conformance & Diagnostics**.
- The approved delivery direction is **local-first developer conformance / CI/CD**, with local CLI, CI and GitHub Action as primary initial surfaces.
- `<15 ms` is a performance target for a future defined warm local benchmark, not an achieved capability or public claim.
- Swedish Ediel is the first wedge; UTILTS/APERAK is the first planned M1 vertical slice.
- Rule IR v0 is now a **locked architecture contract** for M1. It is intentionally bounded, contains no arbitrary-code escape hatch and exposes unsupported mandatory semantics explicitly.
- Parsing, rule resolution and validation must remain deterministic, versioned and testable.
- An LLM may explain verified results but must not decide `PASS/FAIL` or publish normative rules without review.
- MCP is an access/integration layer, not the validation authority or product moat.
- RulePack lifecycle, temporal validity and provenance are first-class concerns.
- Change Impact and Migration Assurance are explicit product hypotheses, not shipped capabilities.
- The 2026-09-30 DHV report is treated as a proposal/strategic signal, not as proof of a final DHV technical contract.
- The repo must not assume a final DHV protocol, IEC 62325 requirement, cutover date or validation responsibility without primary evidence.
- OpenEDI, CIMTool and OpenCGMES are evaluation/reference tooling, not Swedish market authorities.
- Current research distinguishes `NORMATIVE`, `PROCESS_GUIDE`, `EXAMPLE` and `SECONDARY` evidence.

## Review objective

Stress-test the repository for:

1. contradictions between README, architecture, decisions, research and status files;
2. unsupported or over-broad DHV/CIM/product claims;
3. places where example/process-guide evidence becomes normative rule evidence;
4. version / edition / validity ambiguities;
5. whether **Rule IR v0** is a sound bounded M1 contract or already over-engineered;
6. whether any Rule IR primitive is too generic, underspecified or creates a hidden DSL/expression-engine path;
7. whether `business_state` is sufficiently constrained to avoid becoming an arbitrary callback escape hatch;
8. whether `unsupported` semantics and RulePack completeness rules are strong enough to prevent false conformance claims;
9. whether canonical selectors can support precise EDIFACT source-location diagnostics without coupling the rule model back to parser-specific structures;
10. whether the M1 boundary is still narrow enough;
11. whether the architecture accidentally implements a generic multi-protocol framework before product evidence;
12. hidden coupling to OpenEDI, CIMTool, OpenCGMES or another external representation;
13. provenance, temporal-resolution, security or auditability gaps;
14. whether local-first CLI/CI is justified as a delivery wedge while remaining a commercial hypothesis;
15. whether `<15 ms` is kept correctly at benchmark-target level rather than stated as achieved performance;
16. whether Change Impact / Migration Assurance are stated as hypotheses rather than completed product claims;
17. whether customer-discovery gates are falsifiable without inventing market facts;
18. whether SI/vendor-first distribution is treated as a hypothesis rather than certainty;
19. whether the RulePack lifecycle could become a consulting bottleneck;
20. what would make the current venture/product thesis false within 90 days.

## Do not assume

Do not assume:

- that an LLM is the validator;
- that Tydel already supports multiple formats;
- that Tydel already achieves `<15 ms`;
- that local CLI/CI is proven to be the buyer's preferred workflow;
- that Tydel auto-fixes production messages;
- that OpenEDI is a Swedish market authority;
- that CIM/IEC 62325 is the decided Swedish DHV format;
- that the DHV proposal has a final legislated implementation date;
- that one APERAK version/profile applies globally;
- that RulePacks are defensible simply because they exist;
- that Rule IR v0 necessarily fits all future rule families;
- that customers will share production failures;
- that utilities will accept cloud MCP;
- that vendors/SIs will welcome vendor-neutral tooling;
- that public availability of a document implies redistribution or model-training rights.

## Required review format

For every substantive finding, include:

- **Severity:** Critical / Major / Moderate / Minor
- **Type:** Architecture / Research evidence / Product scope / Security / Documentation / Commercial hypothesis / Rule Operations
- **Exact evidence:** file path and relevant heading or short fragment
- **Finding**
- **Why it matters**
- **Recommended action**
- **Confidence:** High / Medium / Low

Separate the final output into:

### A. Verified repository problems
Concrete contradictions, unsupported claims or architecture gaps.

### B. Open questions already acknowledged
Do not report documented unknowns as accidental omissions.

### C. Rule IR v0 challenge
Assess the contract itself: primitive boundaries, canonical path model, provenance, temporal applicability, unsupported semantics, RulePack completeness and implementation risk.

### D. New risks not currently captured
Especially RulePack scalability, source authority, DHV dependency, local-first distribution and GTM/channel assumptions.

### E. Commercial hypotheses to validate externally
Keep these distinct from code/architecture defects.

### F. M1 readiness
State exactly what must be true before Codex should implement the first vertical slice.

### G. 90-day falsification
Identify the single most falsifiable product assumption and concrete evidence that would kill/pivot the current thesis.

## Review standard

Be adversarial but precise. Do not reward the repository merely for having extensive documentation. Challenge whether the abstractions correspond to real validated needs and whether the product can escape consultancy-heavy RulePack authoring.
