# Claude peer review brief — Tydel M0

**Review target:** entire public repository  
**Repository:** `cjrandersson/tydel-arosyn-mcp`  
**Milestone:** M0 — Research foundation + first validator scope  
**Review type:** independent architecture / research / product consistency review

## Read first

1. `project-status.yml`
2. `README.md`
3. `ARCHITECTURE.md`
4. `AGENTS.md`
5. `docs/decisions/`
6. `docs/research/reading-guide.md`
7. `docs/research/ediel-taxonomi.md`
8. `docs/research/utilts-aperak-current-evidence.md`
9. `docs/research/openedi-evaluation.md`
10. `docs/product/positioning.md`
11. `reference/README.md` and the relevant source catalogues

## Important current-state facts

- Tydel is still in M0. There is no finished production validator or MCP service.
- The product strategy is **Validator First**.
- Parsing and validation must remain deterministic, versioned and testable.
- An LLM may explain verified results but must not decide whether a message is valid.
- The first stages are read-only; production correction and retransmission are outside current scope.
- MCP is an access/integration layer, not necessarily the primary product UI.
- OpenEDI is being evaluated only as a machine-readable representation/import source for generic EDI/EDIFACT structure. It is not the Swedish rule authority and must not become Tydel's internal domain model.
- Swedish Ediel is the first product wedge, not a claim that Tydel will permanently support only EDIFACT.
- Current research deliberately distinguishes `NORMATIVE`, `PROCESS_GUIDE`, `EXAMPLE` and `SECONDARY` evidence.
- A publisher example must not silently become a validator rule.

## Review objective

Stress-test the repository for:

1. contradictions between README, architecture, decisions, research and status files;
2. unsupported or over-broad claims;
3. places where example evidence is accidentally treated as normative evidence;
4. version / edition / validity ambiguities;
5. hidden coupling between external formats such as OpenEDI and Tydel's internal models;
6. architecture gaps that would prevent a deterministic first vertical slice;
7. unclear product boundaries or terminology;
8. security, provenance or auditability gaps relevant to read-only validation;
9. assumptions that are technical facts versus assumptions that require customer validation;
10. unnecessary scope that should be removed before M1.

## Do not assume

Do not infer functionality from the repository name, the word MCP or the product pitch alone.

Do not assume:

- that an LLM is the validator;
- that Tydel auto-fixes production messages;
- that OpenEDI is a market messaging protocol or authority;
- that a validator already exists because its contract is being researched;
- that Swedish Ediel rules generalize to all Nordic markets;
- that one APERAK version/profile applies globally;
- that public availability of a document means it may be redistributed or used for model training.

## Required review format

For every substantive finding, include:

- **Severity:** Critical / Major / Moderate / Minor
- **Type:** Architecture / Research evidence / Product scope / Security / Documentation / Commercial hypothesis
- **Exact evidence:** file path and relevant heading or quoted short fragment
- **Finding:** what is wrong, ambiguous or risky
- **Why it matters**
- **Recommended action**
- **Confidence:** High / Medium / Low

Separate the final output into:

### A. Verified repository problems
Concrete contradictions, unsupported claims or architectural gaps.

### B. Open questions already acknowledged by the repository
Do not report documented unknowns as if they were accidental omissions.

### C. New risks not currently captured
Only risks genuinely missing from the repository.

### D. Commercial hypotheses to validate externally
Clearly distinguish these from architecture defects.

### E. M1 readiness
State what must be true before the first deterministic vertical slice should begin. Do not invent a score unless it is supported by explicit criteria.

## Review standard

Be adversarial but precise. A useful review should make the repository more correct, not merely more pessimistic. Prefer one well-supported finding over five speculative ones.
