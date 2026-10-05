# Documentation

This folder contains Tydel's product, research, architecture-decision and review material.

## Product

- [Product positioning](product/positioning.md) — canonical post-DHV positioning: Energy Market Conformance & Diagnostics.
- [Post-DHV roadmap](product/post-dhv-roadmap.md) — gated 90-day and 6–24 month execution roadmap.
- [Customer & channel discovery](product/customer-discovery.md) — operator/utility + SI/software-vendor discovery, evidence gates and kill/pivot logic.

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

## Reviews

- [Claude M0 peer review brief](reviews/claude-peer-review-brief.md) — repository-grounded independent review instructions. Review should now challenge the post-DHV reset as well as the original validator scope.

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
