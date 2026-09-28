# Tydel — product positioning

**Status:** Canonical product positioning  
**Approved:** 2026-09-28

## Canonical positioning

> **Tydel sits at the market-data and integration layer above the physical power grid, where meter data, trading information and other energy-market transactions must conform to versioned message standards and process rules. As Nordic market communication evolves across EDIFACT, XML/CIM and ECP-based exchange, Tydel provides deterministic validation and traceable diagnostics for the messages moving between market participants.**

## What this means

Tydel does not operate the physical grid and is not a grid-control system. It works with the structured market and integration data exchanged between energy-market participants and the systems that support those exchanges.

The first product is **Validator First**: deterministic, evidence-backed validation and diagnostics for Swedish Ediel and related energy-market communication. Swedish Ediel is the first narrow product wedge, not a permanent protocol boundary.

The intended product layer is therefore:

```text
Physical grid / smart meters
        ↓
Utility and market systems
        ↓
Market-message exchange
        ↓
Tydel validation + diagnostics
        ↓
Receiving market actor / operator workflow
```

## Product boundaries

Tydel is not:

- a physical smart-grid or OT control product;
- an Ediel transport network;
- an automatic production-message repair engine in the first product stages;
- an LLM deciding message validity;
- an OpenEDI wrapper;
- limited permanently to EDIFACT.

MCP is an access and integration layer, not the product's only user interface. Future clients may include an operator UI, API, CLI or other controlled interfaces over the same deterministic core.

## Commercial hypothesis

The first commercial hypothesis is that provenance-backed diagnostics can reduce message-investigation MTTR, escalation to scarce specialists and dependency on undocumented expert knowledge. This remains a hypothesis to validate with real operators and integration teams; it is not yet a proven market claim.

## Relationship to architecture

This positioning does not change Tydel's architecture or M0/M1 scope. It clarifies where the product sits in the energy ecosystem and supports the existing decisions in:

- `../../ARCHITECTURE.md`
- `../decisions/0002-openedi-machine-readable-standard-layer.md`
- `../decisions/0003-validator-first-product-strategy.md`
