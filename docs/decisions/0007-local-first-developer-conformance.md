# Decision 0007 — Local-first developer conformance delivery

**Status:** Accepted  
**Date:** 2026-10-05  
**Related:** Decision 0003, Decision 0005, Decision 0006

## Context

Tydel has moved from a reactive Ediel troubleshooting concept toward a developer-first conformance layer for energy-market integrations.

The product should catch integration and market-rule failures before changes reach external test, partner or production systems. That implies a shift-left delivery model rather than a cloud UI as the first product surface.

At the same time, future Swedish DHV technical contracts and CIM/IEC 62325 usage are not yet treated as fixed facts. The first implementation remains UTILTS/APERAK and EDIFACT-based.

## Decision

Tydel adopts a **local-first, offline-capable, CI-native** delivery model.

Primary product surfaces:

1. local CLI;
2. CI/CD gate;
3. GitHub Action.

Secondary surfaces over the same core may later include API, operator UI and MCP.

The local runtime must use the same deterministic validation core and RulePack semantics as every other surface.

## Developer promise

> **Catch energy-market integration errors before external test or production systems do.**

The external category remains **Energy Market Conformance & Diagnostics**. Developer infrastructure is the initial distribution/delivery wedge, not a claim that utilities can never become direct enterprise buyers.

## Validator First

The delivery pivot does not change validation authority:

```text
payload / transaction
→ parser + canonical context
→ resolved versioned RulePack
→ deterministic Rule IR execution
→ structured findings + provenance
→ optional human/AI explanation
```

AI never decides `PASS/FAIL`.

## Architecture inspiration

Tydel may selectively learn from established developer tooling patterns:

- **Conftest / OPA**: local policy evaluation, deterministic exit semantics and CI workflows;
- **Argo CD**: declarative desired-vs-actual comparison, reproducibility and version-aware diff thinking;
- **Ruff / Biome**: fast startup, concise source-linked terminal diagnostics and one core behind multiple developer surfaces;
- **kubeconform**: offline schema resolution/cache and parallel validation patterns.

These projects are architectural inspiration only. Tydel does not inherit their domain models or policy languages by default.

## Performance target

`<15 ms` is accepted as a **performance target** for a defined warm local benchmark.

It is not an achieved capability or public product claim until the benchmark fixes and reports at least:

- payload type and size;
- active rule count;
- schema/cache state;
- cold vs warm execution;
- hardware/CPU;
- number of iterations;
- percentile statistic.

Correctness, determinism and provenance take priority over premature language/runtime optimization.

The project will not switch to Rust/Go merely because reference tools use compiled languages. Runtime-language decisions require measured evidence.

## DHV/CIM boundary

Tydel is designed for a market moving toward more centralised and modern interfaces, including future CIM/IEC 62325-based processes where authoritative profiles support them.

Tydel must not state that Swedish DHV has already selected a specific CIM profile or final interface contract.

The correct positioning is:

> local-first conformance for energy-market integrations, starting with Swedish Ediel and designed to extend to future DHV-era and CIM/IEC 62325 interfaces when authoritative contracts exist.

## Consequences

### M1 priorities

- local/offline execution;
- excellent terminal diagnostics with exact source locations;
- stable process exit codes;
- deterministic RulePack resolution;
- benchmark harness after correctness is proven;
- CI/GitHub Action adapter over the same core.

### Not M1 requirements

- hosted SaaS control plane;
- full operator dashboard;
- public cloud MCP service;
- generic CIM platform;
- speculative DHV adapter;
- Rust/Go rewrite solely for perceived speed.

## Revisit conditions

Revisit this delivery decision if:

- design partners require a hosted/operator-first workflow as the primary buying surface;
- local execution cannot meet security/deployment needs;
- benchmark evidence shows the current runtime cannot meet required throughput/latency;
- official DHV onboarding/certification tooling changes the most valuable integration point;
- customer discovery shows that CI/developer workflows are not where the economic pain or budget lives.
