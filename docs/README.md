# Documentation

This folder contains Tydel's product, research, architecture-decision and review material.

## Product

- [Product positioning](product/positioning.md) — canonical post-DHV positioning: Energy Market Conformance & Diagnostics with a local-first developer/CI delivery wedge.
- [Post-DHV roadmap](product/post-dhv-roadmap.md) — gated 90-day and 6–24 month execution roadmap.
- [Customer & channel discovery](product/customer-discovery.md) — operator/utility + SI/software-vendor discovery, evidence gates and kill/pivot logic.

## Architecture

- [Rule IR v0](architecture/rule-ir-v0.md) — locked internal rule contract for M1, including bounded assertion primitives, provenance, temporal applicability, unsupported-semantics handling and RulePack v0 envelope.
- [Machine-readable Rule IR v0 schema](../schemas/rule-ir-v0.schema.json) — JSON Schema mirror of the Rule IR contract.
- [Validator Result Contract v0](architecture/validator-result-v0.md) — locked deterministic M1 result shape, PASS/FAIL invariants, provenance and safe next-step semantics.
- [Machine-readable Validator Result v0 schema](../schemas/validator-result-v0.schema.json) — strict JSON Schema used by CLI/CI and golden contract tests.
- [Validator Result golden fixtures](../fixtures/m1/validator-result/) — first PASS and source-backed APERAK 313 FAIL contract fixtures.

## Research

- [Research reading guide](research/reading-guide.md) — source order, format boundaries and open questions.
- [UTILTS / APERAK current evidence](research/utilts-aperak-current-evidence.md) — edition status, FCR evidence boundaries and unresolved rule extraction.
- [DHV strategic checkpoint](research/dhv-strategic-watch.md) — reviewed 2026-09-30 report implications plus follow-up watch.
- [CIM / IEC 62325 tooling](research/cim-iec62325-tooling.md) — future XML/CIM research track covering IEC 62325/ENTSO-E ESMP, CIMTool, OpenCGMES and SHACL/RDFS.
- [OpenEDI evaluation](research/openedi-evaluation.md) — machine-readable generic EDI/EDIFACT base-layer evaluation.
- [Source permissions](research/source-permissions.md) — local reference use, public copies and model-use boundaries.
- [Reference collection log](research/collection-log.md) — what was collected and checked.
- [Reference library](../reference/README.md) — catalogues, originals and download commands.

## Decisions

- [Decision 0001 — Live Development Cockpit](decisions/0001-live-development-cockpit.md)
- [Decision 0002 — OpenEDI machine-readable standard layer](decisions/0002-openedi-machine-readable-standard-layer.md)
- [Decision 0003 — Validator First product strategy](decisions/0003-validator-first-product-strategy.md) — reaffirmed with broader meaning after DHV.
- [Decision 0004 — Validator result and delivery contract](decisions/0004-validator-result-and-delivery-contract.md)
- [Decision 0005 — Post-DHV conformance strategy](decisions/0005-post-dhv-conformance-strategy.md) — Ediel remains wedge; Rule IR/RulePacks, temporal resolution, Change Impact and Migration Assurance become explicit strategic direction.
- [Decision 0006 — Lock Rule IR v0 before M1](decisions/0006-rule-ir-v0.md) — bounded deterministic internal rule representation; no custom DSL or arbitrary executable predicates in M1.
- [Decision 0007 — Local-first developer conformance delivery](decisions/0007-local-first-developer-conformance.md) — local CLI/CI/GitHub Action first; API/UI/MCP remain secondary surfaces over the same core; `<15 ms` remains a benchmark target until measured.

## Reviews

- [Claude M0 peer review brief](reviews/claude-peer-review-brief.md) — repository-grounded independent review instructions. Review should challenge the post-DHV reset, Rule IR v0 and the developer-first/local-first direction before M1 runtime implementation.

## Repository documentation rules

Only create a subfolder when it has real content. Link important documents from the main README or `ARCHITECTURE.md`.

Architecture/product decisions should state:

1. the problem/context;
2. verified facts vs assumptions;
3. options considered where relevant;
4. the decision;
5. consequences and guardrails;
6. what could make us revisit it.

A meaningful status change is not finished until `project-status.yml`, the README Development Cockpit and `assets/graphics/development-cockpit.svg` agree.
