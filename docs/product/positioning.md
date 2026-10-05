# Tydel — Product positioning

**Status:** Canonical post-DHV positioning  
**Approved direction:** 2026-10-05  
**Supersedes:** the narrower 2026-09-28 wording where Tydel could be read primarily as a Swedish Ediel validator.

## Canonical positioning

> **Tydel är en deterministisk conformance- och diagnostikmotor för energimarknadens datautbyte. Den avgör vilka tekniska och marknadsmässiga regler som gäller för en transaktion, validerar den mot rätt process/profile/version och visar exakt vad som är fel, varför och vilken evidens som stöder resultatet.**

Kort engelsk version:

> **Tydel is a deterministic conformance and diagnostics layer for energy-market interoperability.**

Kundnära version:

> **Tydel validates energy-market transactions against the correct technical and market rules, showing exactly what failed, why, which version applies and the evidence behind the result.**

## Vad Validator First betyder nu

`Validator First` behålls som produktstrategi, men tolkas bredare än "Ediel validator".

Det betyder att Tydel först bygger en pålitlig, deterministisk kärna för:

1. process/profile/version resolution;
2. versionerade executable RulePacks;
3. deterministisk validation/conformance;
4. exakt strukturerad failure output;
5. normative provenance och tidsmässig giltighet;
6. reproducerbara resultat över CLI/API/UI/MCP/CI.

AI får förklara verifierade resultat. AI är inte validation authority.

## Första wedge och långsiktig kategori

Första wedge:

> **Swedish Ediel, med UTILTS/APERAK som första M1 vertical slice.**

Långsiktig kategori:

> **Energy Market Conformance & Diagnostics**

Ediel är ett konkret sätt att bevisa kärnan mot verkliga, versionsstyrda marknadsregler. Det ska inte bli ett arkitektoniskt eller kommersiellt fängelse.

## Post-DHV thesis

Ei och Svenska kraftnät lämnade 2026-09-30 ett förslag om ett centralt datahanteringsverktyg för elmarknaden. För Tydel betyder detta:

- en Ediel-only thesis blir svagare långsiktigt;
- behovet av migration, pre-validation, regression och change-impact tooling kan bli starkare;
- Tydel ska inte anta att dagens decentraliserade Ediel-topologi består oförändrad;
- Tydel ska inte heller anta att ett visst DHV-interface, schema, CIM-profile eller cutover-datum är beslutat innan auktoritativa specs finns.

Myndigheternas offentliga sammanfattning beskriver DHV som ett förslag till regeringen, anger att den nuvarande marknadsmodellen är utgångspunkt och betonar stegvis införande samt migrationsutmaningar. Därför positioneras Tydel mot **marknadsregler och integrationskontrakt**, inte mot en viss nätverkstopologi.

## Det Tydel ska vara bäst på

Tydel ska konkurrera på **regelresolution och spårbar marknadsbetydelse**, inte på generell syntaxkontroll.

North-star capability:

```text
transaction
+ jurisdiction / market
+ process
+ profile
+ as-of date
        ↓
applicable rules + exact versions
        ↓
deterministic conformance result
        ↓
structured failure + normative evidence
```

Det innebär att Tydel ska kunna svara på både:

> Är detta giltigt enligt rätt marknadsregler nu?

och:

> Var detta giltigt enligt den regelversion som gällde vid ett tidigare datum?

Temporal versioning och provenance är därför kärnfunktioner, inte metadata i efterhand.

## Produkt-hypoteser ovanpå samma core

### 1. Pre-validation

Testa en transaction eller fixture mot rätt RulePack innan den når en partner, testmiljö eller produktion.

### 2. Diagnostics

Lokalisera exakt regelbrott, source, expected/observed och nästa säkra felsökningssteg.

### 3. Change Impact

Jämför två RulePacks/spec-versioner och visa vilka regler, fixtures eller integrationer som påverkas.

### 4. Migration Assurance

Verifiera legacy och target implementations under en övergång mellan marknadsgränssnitt.

`Change Impact` och `Migration Assurance` är strategiska produkt-hypoteser. De får inte marknadsföras som färdiga capabilities innan de är implementerade och validerade.

## Moat-hypotes

Varken parsern, XML-schema validation, MCP eller en snygg UI är tillräcklig som moat.

Den defensible asset-hypotes som ska testas är kombinationen:

`rule ingestion pipeline + executable RulePacks + temporal version history + normative provenance + cross-version mappings + validated failure corpus + resolution knowledge + customer regression suites + workflow integration`

Failure corpus kan bli särskilt värdefullt om det representerar verkliga cross-system failures, men får inte byggas på antagandet att kunder kan eller vill dela konfidentiell produktionsdata. Juridik, sekretess, avtal och dataskydd är explicita constraints.

## Rule Operations som företagsrisk

Den centrala tekniska skalbarhetsfrågan är:

> **Kan Tydel skapa, verifiera och uppdatera RulePacks snabbare än marknadsreglerna förändras utan att verksamheten blir konsulttung?**

Därför används en intern **Rule IR** före eventuell egen DSL.

```text
Normative source
→ importer / curated extraction
→ Rule IR
→ source/human verification
→ versioned executable RulePack
→ runtime
```

En DSL ska endast införas om verkliga regelmönster visar att den behövs.

## AI och MCP

MCP är ett access- och integrationslager. Samma deterministic core ska kunna användas från:

- CLI;
- API;
- CI/CD;
- operator UI;
- local/private MCP;
- framtida agentiska utvecklarflöden.

MCP är särskilt intressant för systemintegratörer och utvecklingsteam eftersom en coding agent kan få ett verifierat conformance-resultat istället för att själv tolka en marknadsspecifikation.

MCP är däremot inte ett krav för att en utility ska kunna använda Tydel, och extern cloud-MCP ska inte antas vara accepterad i säkerhetskänsliga miljöer.

## Commercial wedge

Discovery delas i två spår:

1. **Operators / utilities** — finns den verkliga, återkommande och ekonomiskt betydande smärtan?
2. **SI / software vendors** — kan Tydel distribueras som developer/QA infrastructure till flera slutkunder?

Developer infrastructure kan bli distributions-wedge, medan större enterprise workflows kan byggas ovanpå samma core senare.

## Expansionsriktning

```text
Swedish Ediel / UTILTS-APERAK
        ↓
versioned RulePack + conformance core
        ↓
CLI / API / CI / MCP
        ↓
Change Impact + Migration Assurance
        ↓
selected XML/CIM/IEC 62325 market process
        ↓
future DHV interfaces when official contracts exist
        ↓
selected Nordic rule packs where discovery supports expansion
```

Detta är en gated roadmap, inte ett löfte om att stödja alla standarder.

## Produktgränser

Tydel är inte:

- ett centralt datahanteringsverktyg eller konkurrerande marknadshubb;
- ett EDI-transportnät;
- ett grid-control/OT-system;
- en generell syntaxvalidator utan marknadskontext;
- en LLM som avgör validitet;
- ett system som gissar framtida DHV-specifikationer;
- permanent bundet till EDIFACT;
- en compliance- eller certifieringsmyndighet.

## Current evidence boundary

Det är verifierat att DHV-rapporten är ett myndighetsförslag och att Svenska kraftnät föreslås få ett centralt utvecklings-/driftansvar. Exakta framtida technical contracts behandlas som öppna tills de publiceras auktoritativt.

Se:

- `../research/dhv-strategic-watch.md`
- `../research/cim-iec62325-tooling.md`
- `../decisions/0005-post-dhv-conformance-strategy.md`
- `../../ARCHITECTURE.md`
