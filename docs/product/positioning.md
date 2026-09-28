# Tydel — product positioning

**Status:** Canonical product positioning  
**Approved:** 2026-09-28

## Canonical positioning

> **Tydel validerar energimarknadens meddelanden mot rätt marknadsregler och visar exakt vad som är fel, varför det är fel och vad som bör undersökas härnäst.**

Detta är den primära produktbeskrivningen. Den ska användas före tekniska implementationstermer som MCP, TypeScript, AI eller cloud när Tydel förklaras för en kund eller extern part.

## Vad detta betyder

Tydel arbetar i lagret där energimarknadens strukturerade meddelanden utbyts mellan marknadsaktörer och deras system. Första produkt-wedgen är svensk Ediel, men arkitekturen ska inte låsas permanent till ett enda land, protokoll eller syntaxformat.

Den första produkten är **Validator First**: deterministisk och evidensbaserad validering där rätt process, message/profile, version och regelverk identifieras innan AI får förklara resultatet.

Den avsedda produktkedjan är:

```text
ENERGY-MARKET MESSAGE
        ↓
IDENTIFY PROCESS / PROFILE / VERSION
        ↓
APPLY SCOPED MARKET RULES
        ↓
DETERMINISTIC VALIDATION
        ↓
EXACT FAILURE + EVIDENCE
        ↓
HUMAN EXPLANATION + NEXT INVESTIGATION STEP
```

## Det Tydel ska vara bäst på

Tydel ska konkurrera på marknadsbetydelse och felsökningsprecision, inte på generell EDIFACT-syntaxkontroll.

En generisk validator kan säga att ett segment eller dataelement är ogiltigt. Tydel ska kunna förklara att ett meddelande är fel för en specifik svensk eller nordisk marknadsprocess, message/profile och edition, visa den tillämpliga regeln och hjälpa operatören till nästa säkra felsökningssteg.

Den långsiktiga moat-hypotesen är därför:

`market-specific executable rules + version history + process context + error taxonomy + real failure cases + resolution knowledge + provenance`

AI är ett förklarings- och accesslager ovanpå denna kunskap, inte själva valideringsauktoriteten.

## Produktgränser

Tydel är inte:

- ett fysiskt smart-grid- eller OT-control-system;
- ett transportnät för Ediel;
- en generell EDIFACT-validator utan marknadskontext;
- en automatisk produktionsreparatör i första produktstadiet;
- en LLM som själv avgör om ett meddelande är giltigt;
- en OpenEDI-wrapper;
- permanent begränsad till EDIFACT.

MCP är ett access- och integrationslager, inte produktens enda användargränssnitt. Framtida klienter kan vara operator UI, API, CLI eller andra kontrollerade gränssnitt över samma deterministiska kärna.

## Kommersiell hypotes

Den första kommersiella hypotesen är att spårbar, processmedveten diagnostik kan minska felsökningstid, eskalering till knappa specialister och beroende av odokumenterad expertkunskap.

Detta är ännu inte kommersiellt validerat. Därför ska kunddiscovery ske parallellt med M0/M1 och mäta bland annat:

- hur ofta verkliga Ediel-/marknadsmeddelandefel uppstår;
- faktisk time-to-resolution;
- hur många system och personer som krävs för diagnos;
- expertberoende och eskaleringsgrad;
- affärskonsekvens;
- buyer, budget och willingness-to-pay;
- om en design partner vill bidra med anonymiserade failure cases och pilotera Tydel.

Se [`customer-discovery.md`](customer-discovery.md).

## Expansionsriktning

Den nuvarande arbetshypotesen är:

```text
Swedish Ediel
    ↓
Nordic market-message validation
    ↓
EDIFACT + XML/CIM diagnostics
    ↓
Broader European energy-market interoperability
```

Detta är en riktning, inte ett löfte om framtida scope. Expansion sker först när validatorns kvalitet och kommersiella efterfrågan är belagda.

## Relation till arkitekturen

Positioneringen ändrar inte den deterministiska arkitekturprincipen eller M0/M1-scope. Den förtydligar varför arkitekturen finns och stöder besluten i:

- `../../ARCHITECTURE.md`
- `../decisions/0002-openedi-machine-readable-standard-layer.md`
- `../decisions/0003-validator-first-product-strategy.md`
