# Decision 0005 — Post-DHV conformance strategy

**Status:** Accepted  
**Date:** 2026-10-05  
**Related:** Decision 0003 — Validator First product strategy

## Context

On 2026-09-30 Energimarknadsinspektionen (Ei) and Svenska kraftnät submitted their proposal for a central data-management tool for the Swedish electricity market, Ei R2026:08 / Svk 2025/5201.

The public authority summary states that:

- a central data-management tool is proposed;
- Svenska kraftnät is proposed to develop, operate and maintain it;
- Ei is proposed to have a central governance/regulatory role;
- the current market model is the starting point and is not proposed to be replaced by an electricity-supplier-centric model;
- implementation should be prepared and introduced stepwise;
- experiences from other countries show material challenges during development and migration.

At the same time, the final Swedish technical interface, schema/protocol choices, validation/error contracts, migration milestones and any process-specific IEC 62325 use must not be treated as locked Tydel facts until authoritative specifications exist.

This weakens a long-term company thesis defined as "an Ediel validator for today's bilateral Swedish market topology". It does not weaken the need for deterministic market-rule validation itself.

## Decision

Tydel remains **Validator First**, but the product category is now explicitly:

> **Energy Market Conformance & Diagnostics**

The product north star is:

> **Given an energy-market transaction, its market/process/profile context and an as-of date, Tydel resolves the applicable rule version, validates deterministically and returns exact evidence-backed findings.**

Swedish Ediel remains the first wedge. UTILTS/APERAK remains the first planned M1 vertical slice.

Ediel is not the permanent product boundary.

## Architecture decisions

### Rule resolution is the core competency

The core is not EDIFACT parsing, XML parsing, MCP or AI. Those are adapters/surfaces.

The core sequence is:

```text
transaction + context + as-of date
→ resolve exact RulePack
→ deterministic execution
→ structured result + provenance
```

### Rule IR before DSL

Tydel will define an internal Rule IR against real normative rule diversity before designing a custom DSL.

A DSL may be added later only if observed rule-authoring needs justify it.

### RulePack lifecycle is first-class

A RulePack must be versioned, immutable at publication and carry explicit scope/effective dates/provenance.

The company-level scaling question is whether RulePacks can be created and updated fast enough without turning the business into consulting-heavy bespoke rule coding.

### Temporal validity is first-class

Rules are resolved for an explicit point in time. Historical rule versions are preserved rather than overwritten.

### Multi-protocol compatibility, not multi-protocol M1

The architecture must not couple the core to EDIFACT, but M1 implements only what the UTILTS/APERAK vertical slice requires.

No generic XML/CIM/DHV implementation is added merely to demonstrate abstraction.

### MCP remains an access layer

MCP can expose deterministic tools to developer/AI workflows. It is neither validation authority nor moat and must not be required for utility deployments.

Local/private CLI, API, CI and UI are equal first-class future access surfaces over the same core.

## Product hypotheses added

The following are explicit post-DHV product hypotheses above the same conformance core:

1. **Pre-validation** — catch failures before partner/test/production submission.
2. **Diagnostics** — exact rule, provenance, expected/observed and safe next step.
3. **Change Impact** — compare RulePack/spec versions and show affected rules/tests/integrations.
4. **Migration Assurance** — validate legacy and target representations during market-interface transitions.

Change Impact and Migration Assurance are hypotheses, not current product claims.

## Commercial decision

Customer discovery is split into two tracks:

- **operators/utilities** to prove the pain and economic consequence;
- **SI/software vendors** to test developer-infrastructure distribution and channel leverage.

Initial discovery target: 5 + 5 interviews, then extend if evidence is mixed.

The project will not use invented universal thresholds such as a fixed SEK/year pain number or arbitrary throughput target as market truth.

Economic pain should be measured from real workflows:

`incident frequency × investigation time × people/specialist cost × business consequence`

## M1 decision

M1 remains **UTILTS/APERAK** because current source/evidence readiness is stronger there and it is sufficient to prove the architecture.

PRODAT/supplier switching is a candidate for Commercial Slice 2 but is not selected until discovery supports that choice.

## Moat hypothesis

No single element is assumed to be defensible alone.

The moat hypothesis to test is the compound asset:

```text
rule ingestion pipeline
+ verified executable RulePacks
+ temporal version history
+ normative provenance
+ cross-version mappings
+ validated failure corpus
+ resolution knowledge
+ customer regression suites
+ workflow integration
```

A cross-system failure corpus may be valuable, but customer confidentiality and sharing constraints mean it cannot be assumed to exist at scale.

## DHV guardrails

Tydel must not state as fact that:

- the Swedish DHV has been finally legislated/implemented;
- today's Ediel traffic ends on a specific date;
- DHV will use a specific CIM/IEC 62325 profile;
- a specific API/XML contract is final;
- all validation will be centralised inside DHV.

When authoritative DHV technical contracts are published, Tydel may evaluate them as another market-interface/profile family.

## Consequences

### Continue now

- authoritative UTILTS/APERAK normative extraction;
- Rule IR v0;
- first versioned RulePack;
- deterministic validator contract;
- golden fixtures;
- operator + SI/vendor discovery.

### Do not do now

- generic multi-protocol framework implementation;
- full CIM platform;
- speculative DHV adapter;
- AI-generated normative rules without review;
- forecasting/analytics scope expansion;
- production routing or retransmission.

## 90-day evidence gate

Continue strongly if the project can show:

- end-to-end UTILTS/APERAK supported-scope validation;
- Rule IR handles meaningful real normative rule diversity without repeated runtime special cases;
- at least one edition-to-edition change represented by RulePack versioning;
- at least 10 relevant interviews across the two discovery tracks;
- repeated evidence of costly or specialist-dependent diagnosis;
- at least two parties willing to share safe cases/test data;
- at least one credible pilot candidate.

Pivot or stop the current thesis if real workflows show low incident frequency, trivial diagnosis with existing tooling, little migration/change-impact pain and no willingness to pilot.

## Revisit conditions

Revisit this decision when one or more of the following happens:

- government adopts a concrete DHV implementation programme;
- authoritative DHV technical specifications are published;
- customer discovery contradicts the current buyer/problem thesis;
- M1 Rule IR cannot represent real rules without excessive bespoke code;
- a dominant free/official validator eliminates the proposed value layer;
- a different process provides substantially stronger commercial evidence than UTILTS/APERAK.
