# Tydel

**Ett tydligare sätt att förstå, validera och felsöka Ediel-meddelanden.**

Tydel är ett planerat read-only validerings- och supportlager för svensk energimarknadskommunikation. Målet är att hjälpa operatörer hitta meddelandefel, förstå vad de betyder och se ett säkert nästa steg, utan att ersätta befintlig EDI/Ediel-infrastruktur.

> 🚨 **Produktgräns som ännu inte är låst:** tidigare material nämner även förbrukningsavvikelser och prognostisering av nätkapacitet. Det är inte del av det verifierade validator-scope som dokumentationen nedan bygger på. En sådan utvidgning kräver separat beslut av **@cjrandersson**.

---

# 🧭 DEVELOPMENT COCKPIT

> **Operativ source of truth för projektets aktuella läge.** Uppdatera denna sektion när researchstatus, arkitektur, milestone, ansvar eller exakt nästa steg förändras. Den visuella tavlan och tabellerna ska alltid vara synkroniserade.

![Tydel Development Cockpit](assets/graphics/development-cockpit.svg)

| | Aktuellt läge |
|---|---|
| **Nuvarande milestone** | **M0 — Research foundation & första validator-scope** |
| **Status** | 🟡 **PÅGÅR** |
| **Nuvarande mål** | Låsa en smal, auktoritativ och testbar svensk Ediel-slice utan att göra globala standardantaganden |
| **Exakt nästa uppgift** | Editionsbestäm aktuell UTILTS–APERAK-anvisning och skilj normativa profilregler från FCR-guidens exempel |
| **Nästa owner** | **ChatGPT** |
| **Blockerat / väntar på teamet** | 🚨 **@cjrandersson — besluta senare om Tydel ska förbli validator/support-first eller även omfatta analytics/forecasting. Detta blockerar inte M0-research.** |
| **Codex** | ⏸ **VÄNTAR** — implementation börjar först när första message/profile och validator contract är låsta |
| **Nästa milestone** | **M1 — Första deterministiska validator vertical slice** |
| **Senast uppdaterad** | **2026-09-26** |

### Aktivt ansvar / pending

| Owner | Pending nu | Läge |
|---|---|---|
| **@cjrandersson** | Produktgräns: validator/support-first kontra senare analytics/forecasting | 🚨 **BESLUT KRÄVS, men blockerar inte research** |
| **ChatGPT** | Fortsätt auktoritativ Ediel-kartläggning, editionsbestäm UTILTS/APERAK och håll taxonomi/cockpit synkroniserade | 🟢 **ACTIVE** |
| **Codex** | Vänta med produktionskod tills första validator-slice och contract är låsta | ⏸ **WAITING** |
| **@gonzalolorcakeabit-bit** | Ingen uppgift tilldelad | ⚪ **CLEAR** |

> **Ownership rule:** inget får markeras `pending`, `blocked`, `waiting` eller `next` utan explicit owner. Om Robin behöver agera ska det stå `🚨 @cjrandersson — <åtgärd>`.

### Milestone progress

- [ ] **M0 — Research foundation & första validator-scope** ← **CURRENT**
  - [x] Read-only första versionsgräns definierad
  - [x] Deterministisk parser/validator definierad som source of truth
  - [x] MCP definierat som kontrollerat access-/förklaringslager, inte valideringsauktoritet
  - [x] Arkitektur dokumenterad på svenska
  - [x] Auktoritativ käll- och editionsseparation etablerad
  - [x] OpenEDI utvärderat som kandidat för generiskt maskinläsbart EDIFACT-baslager
  - [x] Svensk taxonomigrund etablerad: `Actor → Process → Transaction → Message → MessageVersion → Rule → Acknowledgement → Error → Resolution`
  - [x] Processgrund verifierad för leverantörsbyte, mätvärdesrapportering och balansavräkning
  - [x] Formatlandskap dokumenterat med `CURRENT`, `CURRENT_SCOPED`, `TRANSITIONAL`, `LEGACY`, `UNVERIFIED`
  - [x] FCR-kedja kartlagd till `QUOTES`, `DELFOR`, `UTILTS S08/S01` och message-specifik `APERAK`
  - [x] Evidens visar att APERAK-version/koder måste scope-bindas till message family/process/profile
  - [ ] Editionsbestäm aktuell fullständig UTILTS–APERAK-anvisning — **ChatGPT**
  - [ ] Separera `example evidence` från `normative rule evidence` — **ChatGPT**
  - [ ] Välj första stödda svenska message/profile — **ChatGPT rekommendation → @cjrandersson endast om produktval krävs**
  - [ ] Definiera första validator contract + strukturerad error output — **ChatGPT / Codex**
  - [ ] Definiera auktoritativa positiva och negativa fixtures — **ChatGPT / Codex**

- [ ] **M1 — Första deterministiska validator vertical slice**
  - [ ] Skapa production `src/`-struktur
  - [ ] Implementera parser för vald message/profile
  - [ ] Importera maskinläsbart base-standard-lager om OpenEDI-spiken håller
  - [ ] Implementera separat versionerade svenska Ediel/profile-overlays
  - [ ] Implementera deterministiska validation rules
  - [ ] Returnera exakt segment, rule, evidence och safe next step
  - [ ] Lägg till positiva/negativa unit fixtures och offline tests
  - [ ] Ge en körbar lokal validerings-entry point

- [ ] **M2 — MCP assistant layer**
  - [ ] Exponera validator via MCP tools
  - [ ] Exponera godkänt referensmaterial via kontrollerade resources
  - [ ] Förklara verifierade validatorresultat på begripligt språk
  - [ ] Bevara evidence/source traceability
  - [ ] Behåll write/change actions utanför scope

- [ ] **M3 — Observability & verklig validering**
  - [ ] Validation history/trends
  - [ ] Kontrollerade alerts
  - [ ] Test med representativa operator workflows
  - [ ] Första design-partner/pilot
  - [ ] Mät tidsbesparing och diagnostisk precision

**Regel:** en meningsfull projektförändring är inte färdigdokumenterad förrän cockpit visar verkligt läge och korrekt owner för varje pending action.

---

## Problemet

Energimarknadens aktörer utbyter affärskritisk information via Ediel, exempelvis mätvärden, leverantörsbyten och avräkningsdata. När ett meddelande är felaktigt, avvisas eller försenas behöver specialister ofta läsa EDIFACT-segment, implementationsanvisningar och flera system manuellt.

Tydel ska minska den felsökningstiden utan att låta en språkmodell gissa om standardregler.

## Första versionen

Den första användbara versionen ska kunna ta emot ett kopierat Ediel-meddelande eller dokumenterat fel, parsa och validera det med fasta testbara regler, peka ut exakt segment och regel, förklara problemet begripligt, föreslå ett säkert nästa steg och visa evidensen bakom svaret.

Tydel ska **inte** ändra eller skicka om produktionsmeddelanden i denna fas.

## Arkitekturprincip

```text
MESSAGE / LOG
    ↓
INGEST
    ↓
PARSE
    ↓
CANONICAL MESSAGE
    ↓
BASE STANDARD + SWEDISH EDIEL/PROCESS OVERLAY
    ↓
DETERMINISTIC VALIDATION
    ↓
STRUCTURED RESULT + EVIDENCE
    ↓
MCP
    ↓
ASSISTANT / OPERATOR UI
```

Parsern och validatorn är source of truth. MCP ger kompatibla AI-klienter kontrollerad tillgång till verktyg och godkänt referensmaterial. AI-lagret får förklara ett verifierat resultat men inte avgöra om ett meddelande är giltigt.

Se [ARCHITECTURE.md](ARCHITECTURE.md) för den tekniska modellen.

## Ediel-taxonomin

Researchen byggs så att den senare kan bli maskinläsbar:

```text
Actor
→ Process
→ Transaction
→ Message
→ MessageVersion
→ SyntaxFormat / TransportProfile
→ Rule
→ Acknowledgement
→ Error
→ Resolution
```

Varje regel eller profil måste bära scope, källa, edition/giltighet och evidensstatus. Statusspråket är:

`CURRENT` · `CURRENT_SCOPED` · `TRANSITIONAL` · `LEGACY` · `UNVERIFIED`

`CURRENT_SCOPED` betyder att något är verifierat som aktuellt inom en uttryckligen avgränsad process. Det får inte automatiskt upphöjas till generell svensk Ediel-regel.

## Vad researchen hittills har visat

Den svenska energimarknaden är inte ett enda EDIFACT-flöde. Olika processer använder parallellt Ediel/EDIFACT och nyare format/transportlösningar. Därför modellerar Tydel process, message, version, syntax och transport separat.

För FCR finns aktuell scope-bunden evidens från Svenska kraftnät för bland annat `QUOTES`, `DELFOR`, `UTILTS S08`, `UTILTS S01` och `APERAK`. Researchen visar dessutom att APERAK inte kan behandlas som en enda global kvittensprofil: versioner och koder varierar med message family/process/profile.

Detta är ännu research evidence, inte ett komplett validator contract. Exempel i implementationsguider får inte behandlas som normativa segmentregler förrän den relevanta standard-/profilanvisningen stödjer det.

Se [UTILTS och APERAK — aktuell verifierad evidens](docs/research/utilts-aperak-current-evidence.md).

## OpenEDI

Tydel utvärderar OpenEDI som maskinläsbar representation av den **generella EDI/EDIFACT-basstandarden**:

```text
UN/EDIFACT / OpenEDI base
          +
Swedish Ediel / process-profile overlay
          ↓
Tydel deterministic validator
```

OpenEDI ersätter inte Svenska kraftnät, Ei, eSett eller andra auktoritativa marknadskällor. Svenska och processpecifika regler versioneras separat och ska vara spårbara till sin källa.

## Säkerhetsregler

- Read-only som standard.
- Deterministiska validation rules före AI-tolkning.
- Inga standardpåståenden utan dokumenterad källa och scope.
- Human approval för framtida åtgärder som ändrar data eller påverkar drift.
- Synthetic eller korrekt anonymiserad testdata.
- Least privilege och auditability.
- Inga compliance-påståenden utan separat dokumenterad bedömning.

## Teknik

TypeScript och officiella MCP TypeScript SDK är nuvarande utgångspunkt, inte ett permanent produktbeslut. OpenEDI utvärderas som inputformat, inte som Tydels interna domänmodell. Den canonical message- och rule-representation som Tydel använder ska kunna bytas och ska inte låsas till en extern specifikationsmodell.

## Projektfiler

| Path | Innehåll |
| --- | --- |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Systemdesign, gränser och dataflöde |
| [`docs/research/`](docs/research/) | Källbaserad Ediel- och marknadsresearch |
| [`docs/decisions/`](docs/decisions/) | Låsta tekniska/produktrelaterade beslut |
| [`reference/`](reference/) | Källkatalog, tillåtna referensfiler och download-instruktioner |
| [`AGENTS.md`](AGENTS.md) | Instruktioner för Codex och andra coding assistants |
| [`assets/graphics/`](assets/graphics/) | Diagram och Development Cockpit |
| [`fixtures/edifact/`](fixtures/edifact/) | Synthetic EDIFACT fixtures |
| [`tests/`](tests/) | Offline tests |
| `src/` | Framtida implementation; skapas först när M1-scope är låst |

## Läsordning

Börja med [reading guide](docs/research/reading-guide.md), därefter [arkitekturen](ARCHITECTURE.md), [Ediel-taxonomin](docs/research/ediel-taxonomi.md) och de processpecifika researchdokumenten.

## Primära källor

- Svenska kraftnät, Aktörsportalen / Ediel / implementationsguider
- Energimarknadsinspektionen (Ei), föreskrifter och marknadsregler
- eSett, Nordic Imbalance Settlement Handbook och relaterad dokumentation
- Edielportalen, aktuella svenska implementationsanvisningar

Externa tekniska projekt som OpenEDI är stödmaterial för maskinläsbar struktur, inte auktoritet för svenska marknadsregler.

## Disclaimer

Tydel är ett oberoende research- och utvecklingsprojekt. Det är inte anslutet till, godkänt av eller certifierat av Svenska kraftnät, Ei, eSett, EdiNation/EdiFabric eller någon marknadsaktör.
