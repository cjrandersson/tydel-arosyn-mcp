# Tydel — Customer & Channel Discovery

**Status:** Active parallel M0 track  
**Updated:** 2026-10-05  
**Preparation owner:** ChatGPT  
**@cjrandersson action required now:** No

## Purpose

Tydel must prove two different things in parallel:

1. **Problem evidence:** operators/utilities actually suffer recurring, costly or specialist-dependent diagnosis around market integrations.
2. **Distribution evidence:** SI/software vendors can use Tydel as developer/QA infrastructure or channel it to multiple customers.

The technical project is not commercially validated merely because a deterministic validator can be built.

## Core discovery questions

### Operator / utility track

> **Does the current workflow contain recurring integration failures where process-aware, deterministic and traceable diagnostics materially reduce time, risk or specialist dependency?**

### SI / software-vendor track

> **Can Tydel become a repeatable conformance/QA layer in development and migration work rather than a one-off customer-specific consulting tool?**

---

## First discovery round: 5 + 5

### Track A: 5 operators / utilities

Prioritise people close to actual market-message or integration operations:

- Ediel/EDI specialists;
- integration engineers;
- meter-data/settlement teams;
- market operations;
- technical application owners;
- IT/integration leads who understand escalation and supplier dependency.

The goal is to reconstruct recent real incidents, not pitch Tydel.

### Track B: 5 SI / software vendors

Prioritise:

- energy-system vendors;
- integration consultancies;
- teams building/maintaining DSO/supplier market integrations;
- consultants responsible for test/certification/migration work.

The goal is to test developer-infrastructure distribution, not assume vendors will welcome vendor-neutral diagnostics.

---

## Operator interview: evidence to capture

Ask about the most recent real failure or rejected message/process and reconstruct:

```text
process
message/profile/version if known
first visible symptom
systems consulted
documents/specs consulted
people involved
external supplier/consultant involved?
time to first diagnosis
time to full resolution
root cause
business/operational consequence
repeat frequency
what existing tooling did/did not reveal
how the issue was verified as solved
```

Then ask:

- What changes when a market specification/version is updated?
- How are regression tests maintained today?
- How do you know which rule version applies to a historical incident?
- Which integrations are hardest to test before production?
- How do you expect centralised DHV work to affect your integration/test workload?
- What would make you trust or reject a third-party conformance result?
- Who owns the budget for this type of tooling or project work?

Do not lead with "Would you buy an Ediel validator?".

---

## SI/vendor interview: evidence to capture

Ask:

- How many energy-market integrations/profiles do you maintain across customers?
- How do you turn specifications into tests/rules today?
- How much customer-specific validation logic is duplicated?
- What happens when a profile/spec changes?
- Is validation embedded in product code, integration middleware, tests, or manual QA?
- How are source/provenance and effective dates tracked?
- How are cross-vendor failures diagnosed?
- Would a neutral CLI/API/CI conformance layer save work, or expose your product in an uncomfortable way?
- Would you consume third-party verified RulePacks, embed a runtime, resell it, or avoid it?
- What deployment/security model would be acceptable?

Specifically test whether:

```text
CLI / API / CI
```

is more attractive than another standalone SaaS UI.

---

## Economic-pain model

Do not impose a universal invented threshold such as `>200,000 SEK/year`.

Estimate observed pain from real workflow evidence:

```text
incident frequency
× investigation time
× people / specialist cost
× escalation / consulting cost
× business consequence
```

Also record whether the pain is already covered by:

- fixed vendor support contract;
- managed service;
- internal specialist team;
- integration platform features;
- official market tooling.

A high theoretical cost does not imply willingness to pay if the budget owner perceives the problem as already outsourced.

---

## Failure corpus

Target: **20–50 safe real-world cases** over time, when contracts, confidentiality and data protection permit.

Possible structured case model:

```text
case_id
jurisdiction
process
message/profile/version
as_of
observed_symptom
validation_findings
root_cause
systems/vendors involved where legally safe
people/roles involved
original_diagnosis_time
resolution
business_impact
evidence_quality
rulepack_version
```

### Hard boundary

Do not commit raw customer production messages, PII, secrets or confidential vendor data to the public repository.

A failure corpus is a moat hypothesis, not an entitlement to customer data.

---

## Product evidence gates

### Gate 1: supported-scope correctness

M1 must correctly validate its explicitly supported UTILTS/APERAK scope with deterministic repeated output.

Golden fixtures should show:

- known-valid → expected PASS;
- known-invalid → expected exact failure(s);
- no unexpected findings;
- rule + source + edition + effective period for normative failures.

### Gate 2: Rule Operations

Prove that Rule IR represents meaningful real rule diversity without continuous runtime special-casing.

Track:

- time from source to candidate Rule IR;
- review effort;
- tests per rule;
- number of custom runtime exceptions;
- edition-to-edition changes that can be represented as RulePack changes.

### Gate 3: workflow value

Measure real diagnosis outcome where possible:

- correct process/profile/version identification;
- correct rule/root-cause finding;
- evidence coverage;
- false positives / false negatives;
- operator diagnosis time with/without Tydel;
- whether the result avoids escalation.

### Gate 4: commercial signal

Strong signals:

- safe failure/test-data sharing;
- design-partner commitment;
- pilot;
- procurement or vendor-channel introduction;
- credible pricing conversation;
- request for CLI/API/CI integration;
- willingness to use a RulePack/change-impact workflow.

---

## 90-day evidence gate

The current thesis gains credibility if, within roughly 90 days of focused work:

1. UTILTS/APERAK works end-to-end on the declared supported scope.
2. Rule IR handles enough normative diversity to expose stable primitives.
3. At least one edition-to-edition change is represented via versioned RulePacks rather than runtime forks.
4. At least 10 strong interviews are completed across the 5 + 5 tracks.
5. At least 3 interviewees show recurring costly or specialist-dependent diagnosis/migration work.
6. At least 2 are willing to provide safe anonymised cases or test fixtures.
7. At least 1 is willing to explore an active pilot.

These are project management gates, not universal market laws.

---

## Kill / pivot logic

### Kill or materially rethink the current problem thesis if

Across strong interviews we repeatedly hear:

- failures are rare;
- existing logs/tools identify the root cause immediately;
- specialist escalation is negligible;
- spec/version changes are easy to absorb;
- DHV/migration testing creates little incremental pain;
- no one will share safe fixtures or pilot;
- Tydel adds no meaningful context beyond existing validators.

### Pivot toward Developer Infrastructure if

The pain is real but buyers consistently reject another standalone SaaS/UI while vendors and development teams ask for:

- CLI;
- API;
- CI/CD integration;
- embedded/local runtime;
- versioned RulePacks;
- spec-change/regression tooling.

### Expand enterprise surfaces later if

A shared core is proven and customers ask for:

- audit/history;
- governance;
- migration dashboards;
- team workflows;
- approval/review of RulePacks;
- private deployment management.

---

## First technical slice vs first commercial slice

### M1 technical slice

**UTILTS/APERAK** remains first because source/evidence readiness is currently stronger.

### Commercial Slice 2

**PRODAT/supplier switching is a candidate, not a decision.**

Select the next slice using evidence from:

- pain frequency/severity;
- source/spec readiness;
- rule richness;
- fixture access;
- migration relevance;
- buyer/budget signal;
- channel reuse.

Do not assign fake numeric certainty to unknown WTP.

---

## Next preparation work

ChatGPT prepares:

1. operator interview guide;
2. SI/vendor interview guide;
3. economic-pain scorecard;
4. failure-case intake template;
5. target-list structure;
6. pilot qualification checklist.

`@cjrandersson` begins outreach after reviewing that pack.
