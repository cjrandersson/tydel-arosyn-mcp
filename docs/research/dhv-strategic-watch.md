# Strategisk watch — centralt datahanteringsverktyg för elmarknaden

**Status:** REVIEWED / FOLLOW-UP WATCH  
**Report date:** 2026-09-30  
**Tydel checkpoint completed:** 2026-10-05  
**Owner:** ChatGPT  
**Hard blocker for M0:** No  
**Long-term product decision gate:** Completed for current public evidence; continue monitoring implementation decisions and technical specifications.

## Source boundary

Primary public identifiers:

- Ei report: **Ei R2026:08**
- Svenska kraftnät case: **Svk 2025/5201**
- Government assignment references: `KN2023/01385`, `KN2024/02551`, `KN2025/01781`

Primary public pages:

- Svenska kraftnät: https://www.svk.se/press-och-nyheter/nyheter/elmarknad-allmant/2026/forslag-infor-ett-centralt-datahanteringsverktyg-for-elmarknaden/
- Svenska kraftnät, completed government assignments: https://www.svk.se/om-oss/verksamhet/vara-regeringsuppdrag/genomforda-regeringsuppdrag/
- Government assignment: https://www.regeringen.se/regeringsuppdrag/2025/09/uppdrag-till-energimarknadsinspektionen-och-svenska-kraftnat-att-ta-fram-forslag-till-ett-centralt-datahanteringsverktyg-for-elmarknaden/

This document distinguishes public verified conclusions from Tydel hypotheses. Do not promote an implementation assumption to fact merely because it is strategically plausible.

## Verified public conclusions relevant to Tydel

From the public authority summary of the 2026-09-30 report:

1. Ei and Svenska kraftnät **propose** that a central data-management tool be introduced for the Swedish electricity market.
2. Svenska kraftnät is proposed to be responsible for development, operation and maintenance.
3. Ei is proposed to have a central role in governance/follow-up, including regulations concerning functions and cost review.
4. The proposal is based on **retaining the current market model**. The report is about common data handling, not a return to the earlier supplier-centric market-model proposal.
5. The tool is intended to make handling of information such as meter values, agreements and supplier switching more uniform and efficient.
6. Publicly described function areas include master/basic data, market processes/coordination, calculation/verification and customer interfaces/authorisation management.
7. The authorities state that centralised solutions in other countries have produced benefits such as standardised market processes and improved data quality, while development and migration have been challenging.
8. The authorities explicitly describe implementation as something that needs to be well prepared and introduced stepwise.

## What is NOT treated as verified for Tydel

The following remain open until authoritative implementation material exists:

- final government/political decision to implement the proposal;
- final programme dates and mandatory cutover milestones;
- exact external API/protocol model;
- whether one or more interfaces use EDIFACT, XML, JSON, CIM/IEC 62325 or other representations;
- exact acknowledgement/error contract;
- division of technical/business validation between DHV and market actors;
- certification/onboarding requirements;
- exact legacy coexistence periods;
- which process migrates first;
- whether all current Ediel flows disappear, and when.

Therefore Tydel must not use phrases such as "DHV will definitely replace Ediel on date X" or "DHV will use IEC 62325" without process-specific primary evidence.

## Strategic impact on Tydel

### Ediel-only thesis

**Weakened.**

A company whose permanent value proposition depends on today's decentralised Swedish Ediel topology faces structural risk if more data/process coordination moves into a central national tool.

### Validator/conformance thesis

**Strengthened, if broadened correctly.**

The difficult problem moves from partner-specific message rejection toward:

- readiness for new market contracts;
- versioned rule interpretation;
- legacy/target coexistence;
- pre-validation;
- regression testing;
- change impact;
- evidence-backed diagnosis across migration phases.

### Product conclusion

Tydel should not optimise to be the best at one file format.

Tydel should optimise to be the best at:

> **resolving which market rules apply to a transaction at a given point in time, executing those rules deterministically and proving the result.**

This conclusion is recorded in Decision 0005.

## Tydel architecture consequences

Continue:

- UTILTS/APERAK first vertical slice;
- deterministic validation;
- source/edition/effective-date provenance;
- process/profile/version resolver;
- internal Rule IR and versioned RulePacks;
- read-only deployment model;
- format adapters separated from domain/runtime;
- CLI/API/CI/MCP as surfaces over the same core.

Add as first-class concerns:

- RulePack lifecycle;
- temporal rule resolution;
- cross-version diffability;
- Change Impact product hypothesis;
- Migration Assurance product hypothesis.

Do not add yet:

- speculative DHV adapter;
- full CIM implementation;
- generic multi-protocol framework beyond what M1 naturally needs;
- claims about DHV certification/pre-validation before a real contract exists.

## Commercial consequences

Discovery is now split into two tracks.

### Operator / utility track

Validate:

- actual frequency of integration/message incidents;
- investigation time;
- specialist dependency;
- business consequence;
- current tools;
- migration/change-management concerns;
- buyer and budget path.

### SI / software-vendor track

Validate:

- whether a deterministic conformance engine would improve internal QA;
- whether CLI/API/CI is more useful than another standalone UI;
- whether vendor teams would use RulePack/change-impact tooling;
- channel/reseller/embedded potential;
- whether vendor neutrality is an advantage or perceived threat.

## Follow-up watch

Monitor, in this order:

1. Swedish government response/decision to Ei R2026:08.
2. Svenska kraftnät implementation programme or programme organisation.
3. Formal functional requirements and process scope.
4. Technical interface specifications and schemas.
5. Error/acknowledgement and validation responsibilities.
6. Testing/certification/onboarding model.
7. Migration phases and legacy coexistence rules.
8. Any explicit mapping to IEC 62325/ENTSO-E ESMP or other standards.

Each future update should be classified as one of:

- `CONFIRMED`
- `PROPOSED`
- `UNSPECIFIED`
- `FUTURE_DECISION`
- `TYDEL_IMPACT`

## Current Tydel conclusion

The 2026-09-30 report is not a reason to stop Tydel.

It is a reason to stop defining Tydel's future as "a Swedish Ediel validator".

The current strategic sequence is:

```text
Swedish Ediel / UTILTS-APERAK
        ↓
prove deterministic RulePack runtime
        ↓
developer conformance surfaces
        ↓
Change Impact + Migration Assurance
        ↓
future DHV / XML-CIM market contracts when authoritative specs exist
```
