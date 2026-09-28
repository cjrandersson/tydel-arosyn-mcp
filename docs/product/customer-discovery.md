# Tydel — Customer Discovery

**Status:** Aktivt parallellt M0-spår  
**Start:** 2026-09-28  
**Förberedelse owner:** ChatGPT  
**@cjrandersson action required now:** Nej

## Syfte

Tydel får inte bara tekniskt verifiera att svenska energimarknadsregler kan modelleras och valideras. Projektet måste också verifiera att riktiga operatörer har ett återkommande, dyrt och köpstarkt problem som Tydel löser bättre än befintliga arbetssätt och verktyg.

Målet med discovery-spåret är därför att besvara:

> **Finns det återkommande marknadsmeddelandefel där processmedveten, deterministisk och spårbar diagnostik sparar tillräckligt mycket tid, specialistkapacitet eller risk för att en organisation vill köpa Tydel?**

## Discovery-princip

Intervjuerna ska börja med verkliga arbetsflöden och fel, inte med en pitch.

Be personen visa eller beskriva de senaste faktiska incidenterna och kartlägg:

- message/process/profile om känt;
- vilket fel som syntes först;
- vilka system och dokument som behövde konsulteras;
- vilka personer som deltog;
- time-to-diagnosis och time-to-resolution;
- om ärendet eskalerades till specialist, systemleverantör eller extern konsult;
- affärs- eller driftkonsekvens;
- vad befintliga verktyg lyckades respektive misslyckades med;
- vad som skulle krävas för att de skulle lita på en validator;
- vem som kan köpa eller godkänna ett sådant verktyg.

## Första målgruppen

Prioritera personer som faktiskt arbetar med eller nära marknadsmeddelanden:

- Ediel-/EDI-specialister;
- integrationsingenjörer;
- mätvärdes- och avräkningsteam;
- market operations;
- elnätsföretag och elleverantörer;
- systemleverantörer och konsulter med Ediel-ansvar.

Svenska aktörer är första discovery-wedgen. Enskilda bolag, exempelvis Upplands Energi, kan användas som konkreta testfall men ska inte definiera Tydels generella modell.

## M0 discovery-gates

### Gate 1 — Problem evidence

Mål: 10–15 starka intervjuer.

Vi vill se flera oberoende organisationer beskriva återkommande problem med minst några av följande egenskaper:

- manuell läsning av messages/loggar/specifikationer;
- flera system måste korsrefereras;
- specialistberoende;
- lång eller varierande diagnostid;
- återkommande eskalering;
- tydlig kostnad eller operativ konsekvens.

### Gate 2 — Failure corpus

Mål: 20–50 anonymiserade verkliga failure cases, när juridik, sekretess och dataskydd tillåter.

Varje case ska så långt möjligt få en strukturerad modell:

```text
case_id
process
message
profile/version
observed_error
root_cause
systems_consulted
people_involved
original_diagnosis_time
resolution
business_impact
evidence_quality
```

Rå kunddata, personuppgifter eller konfidentiella produktionsmeddelanden ska inte committas till det publika repot.

### Gate 3 — Product evidence

Bygg en enda end-to-end validator-slice och testa den mot verkliga fel.

Mät minst:

- korrekt identifierad process/profile/version;
- korrekt regel;
- korrekt root-cause-diagnos;
- evidence coverage;
- false positive / false negative;
- operator time-to-diagnosis med och utan Tydel;
- om nästa föreslagna felsökningssteg är användbart.

### Gate 4 — Commercial evidence

Starkare signaler än “det här verkar bra” är:

- design-partner-åtagande;
- tillgång till anonymiserade failure cases;
- pilot;
- LOI;
- procurement-introduktion;
- betalad pilot eller trovärdig årlig prisdiskussion.

## Kill / pivot criterion

Efter cirka 15 kvalitativa intervjuer ska projektet aktivt ifrågasättas om flera av följande gäller:

- felen är sällsynta;
- befintliga verktyg löser dem snabbt;
- specialistberoendet är litet;
- diagnostiden saknar ekonomisk betydelse;
- de intervjuade användarna saknar väg till budget eller buyer;
- ingen vill dela realistiska failure cases eller pilotera;
- Tydel kan inte ge bättre process-/regelkontext än befintliga generiska validatorer.

Motsatsen är ett starkt fortsättningssignal: flera oberoende organisationer visar återkommande manuella felutredningar, specialistberoende och vilja att pilotera en deterministisk validator.

## Design partner timing

Design partner ska sökas under **M0/M1**, inte först i M3.

Den första piloten behöver inte vara en komplett produkt. Ett CLI, API eller enkelt operatorflöde är tillräckligt om Tydel kan demonstrera:

`exact failure → applicable rule → source → explanation → next investigation step`

## Nästa förberedelse

ChatGPT förbereder innan outreach:

1. intervju-guide;
2. target-list-struktur;
3. failure-case intake template;
4. discovery scorecard;
5. förslag på första typer av svenska aktörer att kontakta.

Ingen outreach behöver göras av `@cjrandersson` innan dessa underlag är klara och har granskats.
