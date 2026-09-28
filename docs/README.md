# Documentation

This folder contains material that is too detailed for the main README.

Available now:

- [Product positioning](product/positioning.md) — canonical description of where Tydel sits in the energy-market stack and what the first product is not.
- [Claude M0 peer review brief](reviews/claude-peer-review-brief.md) — repository-grounded instructions for the independent review.
- [Research reading guide](research/reading-guide.md) — source order, format boundaries and open questions.
- [UTILTS / APERAK current evidence](research/utilts-aperak-current-evidence.md) — current edition status, FCR evidence boundaries and unresolved rule extraction.
- [OpenEDI evaluation](research/openedi-evaluation.md) — M0 spike for a machine-readable generic EDI/EDIFACT base layer.
- [Source permissions](research/source-permissions.md) — local reference use, public copies and model-use boundaries.
- [Reference collection log](research/collection-log.md) — what was collected and checked.
- [Reference library](../reference/README.md) — catalogues, originals and download commands.
- [Decision 0001 — Live Development Cockpit](decisions/0001-live-development-cockpit.md) — README cockpit is the operational project source of truth.
- [Decision 0002 — OpenEDI machine-readable standard layer](decisions/0002-openedi-machine-readable-standard-layer.md) — evaluate OpenEDI as structured base-standard input while keeping Swedish Ediel rules separate.
- [Decision 0003 — Validator First product strategy](decisions/0003-validator-first-product-strategy.md) — deterministic evidence-backed validation is the first product and core competency.

Planned sections:

- `research/` — Ediel and energy-market research with source evidence and review status;
- `decisions/` — architecture decision records;
- `security/` — threat models and deployment requirements;
- `product/` — product positioning, scope, users and validated use cases;
- `reviews/` — independent review briefs and, when appropriate, reviewed findings.

Only create a subfolder when it has real content. Link important documents from the main README or `ARCHITECTURE.md`.

Architecture decisions should state:

1. the problem;
2. the options considered;
3. the decision;
4. the consequences;
5. what could make us revisit it.
