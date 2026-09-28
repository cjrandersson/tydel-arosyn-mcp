# Tydel

> **Tyda el**

## Etymologi

**Tyda**  
*fornsvenska* **þyþa**

Av äldre germanskt ursprung, besläktat med ord för **folk**. Den ursprungliga innebörden kan ungefär förstås som:

> 🟡 **”att göra något begripligt för folket”**

Därifrån har ordet utvecklat betydelser som *tolka*, *förklara*, *meddela innebörden av* och *betyda*.

**Kärnbetydelse:** att göra något förståeligt eller tydligt.

---

## Tydel

### Tydel validerar energimarknadens meddelanden mot rätt marknadsregler och visar exakt vad som är fel, varför det är fel och vad som bör undersökas härnäst.

**Validator First.** Tydels kärna är en deterministisk, evidensbaserad validator för energimarknadskommunikation, med svensk Ediel som första produkt-wedge.

AI får förklara verifierade resultat, men avgör inte om ett meddelande är giltigt. MCP är ett access-/integrationslager, inte själva produkten.

Se [`docs/product/positioning.md`](docs/product/positioning.md) och [`Decision 0003`](docs/decisions/0003-validator-first-product-strategy.md).

---

# 🧭 DEVELOPMENT COCKPIT

> **Operativ source of truth för projektets aktuella läge.** `project-status.yml` är statuskällan. README och den visuella cockpiten ska spegla samma statusmodell och får inte bära motstridiga pending-, blocker- eller owner-värden.

![Tydel Development Cockpit](assets/graphics/development-cockpit.svg)

| | Aktuellt läge |
|---|---|
| **Nuvarande milestone** | **M0 — Research foundation & första validator-scope** |
| **Status** | 🟡 **PÅGÅR** |
| **Nuvarande mål** | Låsa en smal, auktoritativ och testbar svensk Ediel-slice och parallellt förbereda kunddiscovery |
| **Exakt nästa tekniska uppgift** | Extrahera normativa revision-3 UTILTS/APERAK-regler för en smal kandidat-slice och håll dem separerade från processguide/exempel |
| **Parallellt discovery-spår** | Förbered intervju-guide, target-list-struktur, failure-case intake template och discovery scorecard |
| **Nästa owner** | **ChatGPT** |
| **Blockerat / väntar på teamet** | **Inget produktgränsbeslut väntar. Validator First är låst.** |
| **Codex** | ⏸ **VÄNTAR** — implementation börjar först när första message/profile och validator contract är låsta |
| **Peer review** | ✅ **READY** — **@gonzalolorcakeabit-bit** kör Claude enligt [`docs/reviews/claude-peer-review-brief.md`](docs/reviews/claude-peer-review-brief.md) |
| **Nästa milestone** | **M1 — Första deterministiska validator vertical slice** |
| **Senast uppdaterad** | **2026-09-28** |

### Aktivt ansvar / pending

| Owner | Pending nu | Läge |
|---|---|---|
| **@cjrandersson** | Ingen outreach krävs innan discovery-underlagen är klara | ⚪ **CLEAR** |
| **ChatGPT** | Normativa rev-3 UTILTS/APERAK-regler + customer discovery preparation | 🟢 **ACTIVE** |
| **Codex** | Vänta med produktionskod tills första validator-slice och contract är låsta | ⏸ **WAITING** |
| **@gonzalolorcakeabit-bit** | Kör Claude peer-to-peer review enligt review-briefen | 🟡 **READY / NEXT REVIEW** |

> **Ownership rule:** inget får markeras `pending`, `blocked`, `waiting` eller `next` utan explicit owner. Om Robin behöver agera ska det stå `🚨 @cjrandersson — <åtgärd>`.

### Milestone progress

- [ ] **M0 — Research foundation & första validator-scope** ← **CURRENT**
  - [x] Read-only första versionsgräns definierad
  - [x] Deterministisk parser/validator definierad som source of truth
  - [x] MCP definierat som kontrollerat access-/förklaringslager
  - [x] Arkitektur dokumenterad på svenska
  - [x] Auktoritativ käll- och editionsseparation etablerad
  - [x] OpenEDI utvärderat som kandidat för generiskt maskinläsbart EDIFACT-baslager
  - [x] Svensk taxonomigrund etablerad: `Actor → Process → Transaction → Message → MessageVersion → Rule → Acknowledgement → Error → Resolution`
  - [x] Processgrund verifierad för leverantörsbyte, mätvärdesrapportering och balansavräkning
  - [x] Formatlandskap dokumenterat med `CURRENT`, `CURRENT_SCOPED`, `TRANSITIONAL`, `LEGACY`, `UNVERIFIED`
  - [x] FCR-kedja kartlagd till `QUOTES`, `DELFOR`, `UTILTS S08/S01` och message-specifik `APERAK`
  - [x] Produktstrategi låst: **Validator First**
  - [x] Canonical product positioning förenklad och låst
  - [x] Aktuell UTILTS/APERAK-edition identifierad: revision 3 / E5SE5A, giltig från 2025-06-01; revision 4 future-effective 2026-10-01
  - [ ] Separera `example evidence` från `normative rule evidence` på regel-/segmentnivå — **ChatGPT**
  - [ ] Välj första stödda svenska message/profile — **ChatGPT rekommendation → @cjrandersson endast om produktval krävs**
  - [ ] Definiera första validator contract + strukturerad error output — **ChatGPT / Codex**
  - [ ] Definiera auktoritativa positiva och negativa fixtures — **ChatGPT / Codex**

- [ ] **M0-CD — Customer Discovery** ← **PARALLELLT SPÅR**
  - [x] Discovery-plan och kill/pivot-kriterier definierade
  - [ ] Intervju-guide — **ChatGPT**
  - [ ] Target-list-struktur — **ChatGPT**
  - [ ] Failure-case intake template — **ChatGPT**
  - [ ] Discovery scorecard — **ChatGPT**
  - [ ] 10–15 kvalitativa operatorintervjuer — **start först när outreach-upplägg är klart**
  - [ ] 20–50 anonymiserade real-world failure cases när sekretess och dataskydd tillåter
  - [ ] Första design partner under M0/M1

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

- [ ] **M3 — Observability & scale-up**
  - [ ] Validation history/trends
  - [ ] Kontrollerade alerts
  - [ ] Bredda representativa operator workflows
  - [ ] Mät tidsbesparing och diagnostisk precision i pilot

**Regel:** en meningsfull projektförändring är inte färdigdokumenterad förrän `project-status.yml`, README-cockpit och den visuella cockpiten visar samma verkliga läge och korrekt owner för varje pending action.

---

## Problemet

Energimarknadens aktörer utbyter affärskritisk information via bland annat Ediel. När ett meddelande är felaktigt, avvisas eller försenas behöver specialister ofta läsa EDIFACT-segment, implementationsanvisningar, loggar och flera system manuellt.

Tydel ska minska den felsökningstiden utan att låta en språkmodell gissa om standardregler.

## Vad Tydel ska vara bäst på

En generisk EDI-validator kan säga att ett segment eller dataelement är ogiltigt.

Tydel ska kunna säga:

```text
Detta är message/profile X i process Y och edition Z.
Regel R gäller här.
Det mottagna värdet bryter mot regeln.
Här är källan.
Här är nästa säkra felsökningssteg.
```

Det är skillnaden mellan syntaktisk EDIFACT-validering och **marknadsprocessmedveten diagnostik**.

## Första versionen

Den första användbara versionen ska kunna ta emot ett kopierat Ediel-meddelande eller dokumenterat fel och:

1. identifiera message/profile/version och relevant process;
2. parsa och validera med fasta, testbara regler;
3. peka ut exakt fel och tillämplig regel;
4. visa source/edition/evidence;
5. förklara problemet begripligt;
6. föreslå ett säkert nästa felsökningssteg.

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
BASE STANDARD + MARKET / PROCESS OVERLAY
    ↓
DETERMINISTIC VALIDATION
    ↓
STRUCTURED RESULT + EVIDENCE
    ↓
MCP / API / UI
    ↓
OPERATOR
```

Parsern och validatorn är source of truth. AI-lagret får förklara ett verifierat resultat men inte avgöra om ett meddelande är giltigt.

Se [`ARCHITECTURE.md`](ARCHITECTURE.md).

## Taxonomi

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

Varje regel eller profil måste bära scope, källa, edition/giltighet och evidensstatus:

`CURRENT` · `CURRENT_SCOPED` · `TRANSITIONAL` · `LEGACY` · `UNVERIFIED`

`CURRENT_SCOPED` betyder att något är verifierat som aktuellt inom en uttryckligen avgränsad process. Det får inte automatiskt upphöjas till generell svensk Ediel-regel.

## Customer Discovery

Den tekniska hypotesen och den kommersiella hypotesen ska valideras parallellt.

Vi behöver verifiera om riktiga operatörer har återkommande felutredningar med hög diagnostid, flera system, specialistberoende eller tydlig affärskonsekvens, och om de vill pilotera eller köpa en deterministisk diagnosmotor.

Se [`docs/product/customer-discovery.md`](docs/product/customer-discovery.md).

## Expansionsriktning

Arbetshypotesen är:

```text
Swedish Ediel
    ↓
Nordic market-message validation
    ↓
EDIFACT + XML/CIM diagnostics
    ↓
Broader European energy-market interoperability
```

Sverige är första wedge, inte nödvändigtvis slutmarknaden.

## OpenEDI

Tydel utvärderar OpenEDI som maskinläsbar representation av den generella EDI/EDIFACT-basstandarden:

```text
UN/EDIFACT / OpenEDI base
          +
Swedish Ediel / process-profile overlay
          ↓
Tydel deterministic validator
```

OpenEDI ersätter inte Svenska kraftnät, Ei, eSett eller andra auktoritativa marknadskällor.

## Säkerhetsregler

- Read-only som standard.
- Deterministiska validation rules före AI-tolkning.
- Inga standardpåståenden utan dokumenterad källa och scope.
- Human approval för framtida åtgärder som ändrar data eller påverkar drift.
- Synthetic eller korrekt anonymiserad testdata.
- Least privilege och auditability.
- Inga compliance-påståenden utan separat dokumenterad bedömning.

## Projektfiler

| Path | Innehåll |
| --- | --- |
| [`project-status.yml`](project-status.yml) | Gemensam statuskälla för Development Cockpit |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Systemdesign, gränser och dataflöde |
| [`docs/product/`](docs/product/) | Positionering och customer discovery |
| [`docs/reviews/`](docs/reviews/) | Oberoende review-briefs och findings |
| [`docs/research/`](docs/research/) | Källbaserad Ediel- och marknadsresearch |
| [`docs/decisions/`](docs/decisions/) | Låsta tekniska/produktrelaterade beslut |
| [`reference/`](reference/) | Källkatalog och referensmaterial |
| [`AGENTS.md`](AGENTS.md) | Instruktioner för coding assistants |
| [`assets/graphics/`](assets/graphics/) | Diagram och Development Cockpit |
| [`fixtures/edifact/`](fixtures/edifact/) | Synthetic EDIFACT fixtures |
| [`tests/`](tests/) | Offline tests |
| `src/` | Framtida implementation; skapas först när M1-scope är låst |

## Primära källor

- Svenska kraftnät, Aktörsportalen / Ediel / implementationsguider
- Energimarknadsinspektionen (Ei), föreskrifter och marknadsregler
- eSett, Nordic Imbalance Settlement Handbook och relaterad dokumentation
- Edielportalen, aktuella svenska implementationsanvisningar

Externa tekniska projekt som OpenEDI är stödmaterial för maskinläsbar struktur, inte auktoritet för svenska marknadsregler.

## Disclaimer

Tydel är ett oberoende research- och utvecklingsprojekt. Det är inte anslutet till, godkänt av eller certifierat av Svenska kraftnät, Ei, eSett, EdiNation/EdiFabric eller någon marknadsaktör.
