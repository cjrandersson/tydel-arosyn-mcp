# Decision 0006 — Lock Rule IR v0 before M1

**Status:** Accepted  
**Date:** 2026-10-05  
**Related:** Decision 0003, Decision 0005

## Context

Tydel's post-DHV strategy makes rule resolution, versioned RulePacks and provenance-backed deterministic validation the core competency.

The project therefore needs a stable internal rule representation before Codex implements the first M1 runtime. At the same time, designing a custom DSL before real rule diversity is understood would risk over-engineering and hidden coupling to one syntax or external tool.

## Decision

Tydel adopts **Rule IR v0** as the internal, JSON/YAML-serialisable rule contract for M1.

Canonical specification:

- `docs/architecture/rule-ir-v0.md`
- `schemas/rule-ir-v0.schema.json`

Rule IR v0 is not a public authoring DSL.

It is the execution/interchange boundary between source-derived rule curation and the deterministic runtime.

## Core constraints

Rule IR v0:

- carries explicit scope, effective period and provenance;
- evaluates against canonical transaction/context paths;
- supports a deliberately bounded set of assertion primitives;
- contains no arbitrary scripts or opaque custom callbacks;
- exposes unsupported semantics explicitly;
- links published rules to deterministic tests;
- is distributed through immutable/versioned RulePacks;
- preserves old versions for historical `as_of` validation.

## Supported primitive families

The initial contract includes:

- presence;
- cardinality;
- datatype;
- pattern;
- allowed value;
- code list;
- literal equality;
- reference equality;
- restricted conditional presence;
- sequence;
- temporal relation;
- explicitly reviewed business-state model references.

These primitives are a bounded M1 contract, not a claim that all future energy-market rules fit v0.

## No arbitrary expression engine

Rule IR v0 deliberately excludes embedded JavaScript/TypeScript/Python, general Rego/CEL/JMESPath execution, network calls and LLM-generated predicates.

If a verified mandatory rule cannot be represented faithfully, it is marked `unsupported` and becomes architecture evidence. It must not be hidden in untraceable runtime special code.

## RulePack implication

Published RulePacks are versioned and immutable.

A RulePack must state:

- jurisdiction/market/process/profile scope;
- syntax/message/profile identity;
- effective period;
- source manifest;
- Rule IR schema version;
- executable rules;
- publication state.

Content signing is deferred. Historical identity and reproducibility are not deferred.

## Consequences

### Allowed now

- lock the M1 UTILTS/APERAK supported profile;
- extract verified normative rules into Rule IR v0;
- define the M1 validator result contract against stable rule IDs/RulePack identity;
- build golden fixtures;
- let Claude peer-review the abstraction before runtime implementation.

### Still blocked

Codex must not implement M1 production runtime until:

1. the exact supported UTILTS/APERAK profile/scope is locked;
2. verified normative rules are populated into the first RulePack;
3. validator result/error contract is locked;
4. positive/negative golden fixtures are defined.

## Revisit conditions

Revisit Rule IR v0 if:

- mandatory M1 rules repeatedly require bespoke runtime code;
- the bounded conditional model proves insufficient for common normative rules;
- a second market/syntax family cannot map cleanly without semantic distortion;
- RulePack change-impact cannot distinguish semantic and editorial changes;
- measured performance shows the representation is a material bottleneck;
- a dedicated authoring DSL becomes justified by measured rule-operations needs.
