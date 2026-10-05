# Tydel — Post-DHV roadmap

**Status:** Strategic roadmap, gated by evidence  
**Updated:** 2026-10-05

This roadmap translates Decision 0005 into execution. Dates are planning horizons, not promises about customer adoption or the Swedish DHV programme.

## Principle

Tydel should prove one narrow conformance engine before expanding across standards.

```text
prove rule resolution
→ prove deterministic runtime
→ prove customer pain
→ prove repeatable RulePack operations
→ add developer distribution surfaces
→ validate Change Impact / Migration Assurance
→ add one next-generation market-process slice
```

---

## 0–90 days

### Product

- Lock first supported UTILTS/APERAK profile/version.
- Define Rule IR v0 against real normative rules.
- Publish first immutable/versioned RulePack.
- Define stable validation-result contract.
- Build golden positive/negative fixtures.
- Prove deterministic repeated results.
- Prove at least one edition-to-edition rule change through RulePack versioning rather than bespoke runtime branching.

### Rule Operations

Measure:

- source → candidate rule time;
- candidate → reviewed rule time;
- tests required per rule;
- percentage represented by common primitives;
- number of custom runtime exceptions;
- provenance completeness.

### Discovery

- Prepare discovery pack.
- Interview 5 operators/utilities.
- Interview 5 SI/software vendors.
- Capture real economic-pain evidence.
- Seek at least two safe fixture/case contributors.
- Seek at least one credible pilot candidate.

### Do not build

- speculative DHV adapter;
- generic all-protocol abstraction framework;
- full CIM support;
- forecasting;
- production write/retransmission;
- AI-authored normative rules without human/source verification.

---

## 3–6 months

### M1 deliverable

A demonstrable end-to-end UTILTS/APERAK conformance slice:

```text
input
→ parse
→ context resolution
→ exact RulePack
→ deterministic findings
→ evidence
→ CLI/API output
```

### Developer surfaces

Add only when the core is stable:

- CLI;
- programmatic API;
- CI runner/integration;
- MCP adapter for controlled developer/AI workflows.

The objective is not feature count. It is to show the same validation result contract across different access surfaces.

### Commercial choice

Use discovery to choose Commercial Slice 2.

PRODAT/supplier switching is a current candidate because of potential migration relevance, but it is not pre-selected.

---

## 6–12 months

### Change Impact hypothesis

Prototype RulePack/spec diff:

```text
version N
vs
version N+1
→ added/removed/changed rules
→ code-list changes
→ cardinality/semantic changes
→ affected fixtures
```

Test whether customers pay attention to:

- impacted integrations;
- regression scope;
- migration readiness;
- historical rule resolution.

### Migration Assurance hypothesis

When a concrete target contract exists, test:

- legacy fixture against old RulePack;
- target representation against new RulePack;
- semantic compatibility where evidence permits;
- traceable readiness reports.

Do not call this "DHV certification" unless an authorised certification relationship actually exists.

### GTM

Possible channels to validate:

- SI/internal QA teams;
- energy-system vendors;
- technical application/integration teams;
- paid design partner;
- embedded/private runtime licensing.

---

## 12–18 months

### Selected XML/CIM/IEC 62325 vertical slice

Only after M1 and market evidence.

Choose **one** market process and evaluate:

- official ENTSO-E/IEC-profile artifacts;
- XSD/schema validation;
- RDFS/SHACL where appropriate;
- CIMTool as profile/build reference tooling;
- OpenCGMES patterns where relevant without conflating CGMES with IEC 62325 market messaging.

Success condition:

> The same Tydel RulePack/resolution/result model works across an EDIFACT slice and one selected XML/CIM market-process slice without rewriting the product core.

---

## 18–24 months

Potential product packaging if evidence supports it:

### Tydel Developer

- CLI;
- API;
- CI;
- MCP;
- RulePacks;
- regression/conformance testing.

### Tydel Enterprise

- operator UI;
- audit/history;
- RulePack governance;
- team workflows;
- private deployment;
- change-impact and migration dashboards.

### Tydel Migration

- cross-version regression;
- legacy/target readiness;
- impact reports;
- migration evidence packages.

These packages are hypotheses. Product packaging follows buyer evidence, not the other way around.

---

## DHV trigger conditions

Do not implement a DHV-specific adapter until there is enough authoritative material to answer:

1. Which process is in scope?
2. What is the interface/protocol?
3. What schema/profile/version applies?
4. What is the official validation/error contract?
5. What is the onboarding/test environment?
6. What is the effective/migration timeline?
7. Which legacy flows coexist?

When those conditions are met, add the relevant DHV interface/profile as a new adapter + RulePack family, not as a separate product core.

---

## 90-day decision gate

### Continue strongly

If technical correctness, RulePack repeatability and early customer/channel signals all improve.

### Pivot

If problem evidence is strong but buyers consistently want embedded CLI/API/CI rather than a standalone SaaS UI.

### Stop/rethink

If supported-scope correctness is hard to achieve, RulePack authoring remains bespoke, real diagnosis pain is weak, existing tools solve the problem sufficiently and no credible pilot emerges.
