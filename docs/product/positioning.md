# Tydel — Product positioning

**Status:** Canonical post-DHV positioning  
**Approved direction:** 2026-10-05  
**Supersedes:** the narrower 2026-09-28 wording where Tydel could be read primarily as a Swedish Ediel validator.

## Canonical positioning

> **Tydel är ett lokalt först, utvecklarcentrerat Conformance & CI/CD Layer för energimarknadens integrationer. Den deterministiska kärnan avgör vilka tekniska och marknadsmässiga regler som gäller för en transaktion, validerar den mot rätt process/profile/version och visar exakt vad som är fel, varför och vilken evidens som stöder resultatet.**

Kort engelsk version:

> **Tydel is a local-first deterministic conformance and CI/CD layer for energy-market integrations.**

Kundnära version:

> **Tydel validates energy-market integrations against the correct technical and market rules before they reach external test or production systems, showing exactly what failed, why, which version applies and the evidence behind the result.**

Developer promise:

> **Catch energy-market integration errors before the market does.**

## Vad Validator First betyder nu

`Validator First` behålls som produktstrategi, men tolkas bredare än "Ediel validator".

Det betyder att Tydel först bygger en pålitlig, deterministisk kärna för:

1. process/profile/version resolution;
2. versionerade executable RulePacks;
3. deterministisk validation/conformance;
4. exakt strukturerad failure output;
5. normative provenance och tidsmässig giltighet;
6. reproducerbara resultat över local CLI/CI och senare API/UI/MCP.

AI får förklara verifierade resultat. AI är inte validation authority.

## Första wedge och långsiktig kategori

Första wedge:

> **Swedish Ediel, med UTILTS/APERAK som första M1 vertical slice.**

Långsiktig kategori:

> **Energy Market Conformance & Diagnostics**

Initial delivery wedge:

> **Developer Infrastructure / Conformance & CI/CD**

Ediel är ett konkret sätt att bevisa kärnan mot verkliga, versionsstyrda marknadsregler. Det ska inte bli ett arkitektoniskt eller kommersiellt fängelse.

## Post-DHV thesis

Ei och Svenska kraftnät lämnade 2026-09-30 ett förslag om ett centralt datahanteringsverktyg för elmarknaden. För Tydel betyder detta:

- en Ediel-only thesis blir svagare långsiktigt;
- behovet av migration, pre-validation, regression och change-impact tooling kan bli starkare;
- Tydel ska inte anta att dagens decentraliserade Ediel-topologi består oförändrad;
- Tydel ska inte heller anta att ett visst DHV-interface, schema, CIM-profile eller cutover-datum är beslutat innan auktoritativa specs finns.

Därför positioneras Tydel mot **marknadsregler och integrationskontrakt**, inte mot en viss nätverkstopologi.

Korrekt framtidsformulering är:

> **Tydel starts with Swedish Ediel and is designed to extend to future DHV-era and CIM/IEC 62325 interfaces when authoritative contracts exist.**

Inte att DHV redan har valt ett specifikt CIM-kontrakt.

## Det Tydel ska vara bäst på

Tydel ska konkurrera på **regelresolution, spårbar marknadsbetydelse och developer ergonomics**, inte på generell syntaxkontroll.

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

## Local-first / Shift-Left

Primär produktupplevelse:

```text
developer changes integration
        ↓
local Tydel CLI
        ↓
resolved schemas + RulePack
        ↓
deterministic validation
        ↓
source-linked diagnostics
        ↓
process exit code
        ↓
CI / GitHub Action passes or fails
```

Local/offline execution minskar beroendet av externa sandlådor och gör Tydel användbart i privata utvecklings- och CI-miljöer.

Arkitektonisk inspiration hämtas selektivt från Conftest/OPA, Argo CD, Ruff/Biome och kubeconform. Dessa är inspirationsmönster, inte val av deras domänmodell eller policy-language.

`<15 ms` är ett performance target för en definierad warm local benchmark. Det är inte ett marknadsclaim innan benchmarken är reproducerbart definierad och mätt.

## Rule IR v0

Rule IR v0 är nu låst som internt M1-kontrakt:

- `../architecture/rule-ir-v0.md`
- `../../schemas/rule-ir-v0.schema.json`
- `../decisions/0006-rule-ir-v0.md`

Rule IR innehåller bounded deterministic primitives, explicit temporal applicability och provenance. Det finns ingen arbitrary-code escape hatch. Mandatory rule semantics som inte kan representeras måste synliggöras som `unsupported` i stället för att döljas i specialkod.

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

Därför används den låsta interna **Rule IR v0** före eventuell egen DSL.

```text
Normative source
→ importer / curated extraction
→ Rule IR v0
→ source/human verification
→ versioned executable RulePack
→ runtime
```

En DSL ska endast införas om verkliga regelmönster och authoring-behov visar att den behövs.

## AI och MCP

MCP är ett access- och integrationslager. Samma deterministic core ska kunna användas från:

- local CLI;
- CI / GitHub Action;
- API;
- operator UI;
- local/private MCP;
- framtida agentiska utvecklarflöden.

MCP är särskilt intressant för systemintegratörer och utvecklingsteam eftersom en coding agent kan få ett verifierat conformance-resultat istället för att själv tolka en marknadsspecifikation.

MCP är däremot inte ett krav för att en utility ska kunna använda Tydel, och extern cloud-MCP ska inte antas vara accepterad i säkerhetskänsliga miljöer.

## Commercial wedge

Discovery delas i två spår:

1. **Operators / utilities** — finns den verkliga, återkommande och ekonomiskt betydande smärtan?
2. **SI / software vendors** — kan Tydel distribueras som developer/QA infrastructure till flera slutkunder?

Developer infrastructure är den initiala distributions-wedgen. Större enterprise workflows kan byggas ovanpå samma core senare om kundbehov och budget stöder det.

## Expansionsriktning

```text
Swedish Ediel / UTILTS-APERAK
        ↓
Rule IR v0 + versioned RulePack + conformance core
        ↓
local CLI / CI / GitHub Action
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
- `../decisions/0006-rule-ir-v0.md`
- `../decisions/0007-local-first-developer-conformance.md`
- `../../ARCHITECTURE.md`
