# Decision 0004 — Validator result and delivery contract

**Status:** Accepted  
**Date:** 2026-09-28

## Problem

Tydel ska kunna förklara samma valideringsfel för olika mottagare utan att skapa flera konkurrerande versioner av sanningen. En operatör behöver ett begripligt nästa steg, ett integrationsteam behöver teknisk detalj, ett system behöver stabil maskinläsbar data och en AI-klient behöver kontrollerad åtkomst till samma verifierade resultat och evidens.

Samtidigt får Tydel inte ersätta eller förvanska den ursprungliga marknadssignalen, exempelvis en APERAK-kod eller annan acknowledgement/error code.

## Decision

Tydels validator producerar **ett gemensamt strukturerat validation result**. Det resultatet är source of truth för all presentation och vidare distribution.

Ett fel är inte färdigkommunicerat förrän resultatet kan svara på:

1. **Vad är fel?**
2. **Var finns felet?**
3. **Varför är det fel?**
4. **Hur vet Tydel det?**
5. **Vad är ett säkert nästa steg?**
6. **Vem är rekommenderad owner när det går att avgöra deterministiskt eller med verifierad routinglogik?**

### Originalsignal + Tydel-kod

Tydel ska alltid bevara originalkoden och originalsvaret oförändrat när sådant finns.

Exempel:

```text
Original response: APERAK 313
Tydel code: TYD-ACK-001
```

Tydel-koden är ett normaliserat lager ovanpå originalsignalen, inte en ersättning för den.

### Stabilt strukturerat resultat

Första validator-contractet ska minst kunna bära:

```json
{
  "code": "TYD-REF-004",
  "severity": "error",
  "message": "UTILTS",
  "message_version": "D02B",
  "profile": "E5SE9B",
  "process": "FCR Activated Energy",
  "location": "RFF+ACW",
  "original_response": "APERAK 313",
  "rule_id": "SE-FCR-UTILTS-RFF-004",
  "rule_layer": "SWEDISH_PROFILE",
  "expected": "reference to original message id",
  "observed": "missing or mismatched reference",
  "evidence": [],
  "recommended_owner": "mapping",
  "next_action": "Verify original message reference and mapping"
}
```

Fältnamn och exakt schema låses först i validator-contractet för M1, men principen ovan är accepterad.

## Audience-specific presentation

Samma validation result får olika presentation beroende på mottagare:

| Mottagare | Primärt behov | Leverans |
| --- | --- | --- |
| Operatör / support | Begripligt fel, påverkan, evidens, nästa steg | Web UI över HTTPS |
| EDI-/integration-/mappingteam | Message/profile, segment, expected/observed, rule ID, provenance | REST API + JSON och teknisk UI-vy |
| Automatiska system | Stabil kod, severity, location, rule ID, correlation identifiers | REST API / webhook över HTTPS |
| AI-klient / agent | Kontrollerad åtkomst till verifierat resultat och godkända referenser | MCP |
| Team lead / verksamhet | Trender, återkommande rotorsaker och påverkan | Senare observability/reporting-lager |
| Marknadens motpart | Befintligt marknadsmeddelande enligt aktuell process | Befintlig Ediel/marknadstransport, inte Tydels interna output-protokoll |

## System boundary

I Validator First-fasen ligger Tydel **bredvid produktionsflödet** och arbetar read-only med kopior av messages, acknowledgements, fel och loggar.

```text
MARKNADSFLÖDE
Actor A ── EDIFACT / XML / CIM / etablerad transport ──► Actor B
   │
   └── copy / message / log ──► TYDEL VALIDATOR
                                  │
                                  ├── Web UI
                                  ├── REST / JSON
                                  ├── Webhook
                                  └── MCP
```

Tydel ska i denna fas inte automatiskt korrigera, routa om eller återsända produktionsmeddelanden.

## Error-code namespaces

Tydels egna felkoder ska vara stabila och kategoriserbara. Följande namespace är utgångspunkt:

```text
TYD-SYN-xxx   syntax
TYD-PRO-xxx   profile/version
TYD-SEG-xxx   segment/data
TYD-BIZ-xxx   business rule
TYD-ACK-xxx   acknowledgement
TYD-REF-xxx   references/correlation
TYD-TIME-xxx  time/period
TYD-ROLE-xxx  actor/role
```

Exakt kodkatalog definieras tillsammans med första låsta validator-profile och test-fixtures.

## Consequences

- Validatorn behöver bara producera ett auktoritativt resultatformat.
- UI, API, webhook och MCP blir adapters/presentationer ovanpå samma resultat.
- Originala marknadskoder förblir synliga och spårbara.
- Mänskliga förklaringar får aldrig förändra validatorns deterministiska utfall.
- Nya kundkanaler, exempelvis Teams, ServiceNow eller andra integrationsytor, kan läggas till utan att ändra valideringskärnan.
- Routing till rekommenderad owner är ett separat lager och får inte förväxlas med själva valideringsregeln.

## Revisit when

- första M1 validator-contractet låses;
- en kund kräver write-back eller automatisk retransmission;
- Tydel börjar arbeta inline i produktionsflödet;
- nya marknadsformat kräver andra correlation- eller acknowledgement-modeller.
