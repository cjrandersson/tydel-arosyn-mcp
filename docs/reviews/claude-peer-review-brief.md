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
5. `docs/decisions/0003-validator-first-product-strategy.md`
6. `docs/decisions/0005-post-dhv-conformance-strategy.md`
7. `docs/product/positioning.md`
8. `docs/product/post-dhv-roadmap.md`
9. `docs/product/customer-discovery.md`
10. `docs/research/dhv-strategic-watch.md`
11. `docs/research/utilts-aperak-current-evidence.md`
12. `docs/research/cim-iec62325-tooling.md`
13. `docs/research/openedi-evaluation.md`
14. `docs/research/reading-guide.md`
15. `reference/README.md` and relevant source catalogues

## Important current-state facts

- Tydel is still in M0. There is no finished production validator or MCP service.
- The product strategy remains **Validator First**, but Decision 0005 broadens the category to **Energy Market Conformance & Diagnostics**.
- Swedish Ediel is the first wedge; UTILTS/APERAK is the first planned M1 vertical slice.
- Parsing, rule resolution and validation must remain deterministic, versioned and testable.
- An LLM may explain verified results but must not decide `PASS/FAIL` or publish normative rules without review.
- MCP is an access/integration layer, not the validation authority or product moat.
- Rule IR is intentionally preferred before designing a custom DSL.
- RulePack lifecycle, temporal validity and provenance are now first-class concerns.
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
5. whether Rule IR / RulePack abstractions are justified by real rule diversity or already over-engineered;
6. whether the M1 boundary is still narrow enough;
7. whether the architecture accidentally implements a generic multi-protocol framework before product evidence;
8. hidden coupling to OpenEDI, CIMTool, OpenCGMES or another external representation;
9. provenance, temporal-resolution, security or auditability gaps;
10. whether Change Impact / Migration Assurance are stated as hypotheses rather than completed product claims;
11. whether customer-discovery gates are falsifiable without inventing market facts;
12. whether SI/vendor-first distribution is treated as a hypothesis rather than certainty;
13. whether the RulePack lifecycle could become a consulting bottleneck;
14. what would make the current venture/product thesis false within 90 days.

## Do not assume

Do not assume:

- that an LLM is the validator;
- that Tydel already supports multiple formats;
- that Tydel auto-fixes production messages;
- that OpenEDI is a Swedish market authority;
- that CIM/IEC 62325 is the decided Swedish DHV format;
- that the DHV proposal has a final legislated implementation date;
- that one APERAK version/profile applies globally;
- that RulePacks are defensible simply because they exist;
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

### C. New risks not currently captured
Especially RulePack scalability, source authority, DHV dependency and GTM/channel assumptions.

### D. Commercial hypotheses to validate externally
Keep these distinct from code/architecture defects.

### E. M1 readiness
State exactly what must be true before Codex should implement the first vertical slice.

### F. 90-day falsification
Identify the single most falsifiable product assumption and concrete evidence that would kill/pivot the current thesis.

## Review standard

Be adversarial but precise. Do not reward the repository merely for having extensive documentation. Challenge whether the abstractions correspond to real validated needs and whether the product can escape consultancy-heavy RulePack authoring.
