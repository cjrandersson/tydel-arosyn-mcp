# Strategisk watch — centralt datahanteringsverktyg för elmarknaden

**Status:** WATCH / EXTERNAL DEPENDENCY  
**Rapporteringsdeadline:** 2026-09-30  
**Owner för Tydel-analys:** ChatGPT  
**Hard blocker för M0-research:** Nej  
**Decision gate för långsiktig produkt-/arkitekturthesis:** Ja

## Varför Tydel följer detta

Energimarknadsinspektionen (Ei) och Svenska kraftnät har regeringens uppdrag att ta fram förslag till ett centralt datahanteringsverktyg för elmarknaden. Utfallet kan påverka vilka marknadsprocesser som centraliseras, hur aktörer ansluter, vilka format och gränssnitt som används, var validering sker och hur länge dagens Ediel-flöden lever parallellt med nya lösningar.

Det kan därför påverka Tydels långsiktiga marknad, integrationspunkt och expansionsplan. Det ändrar däremot inte behovet av källbaserad validator-research i M0.

## Verifierad deadline

Regeringsuppdraget anger att **Energimarknadsinspektionen senast den 30 september 2026 ska lämna redovisningen till Regeringskansliet (Klimat- och näringslivsdepartementet)**.

Ingen offentlig källa som kontrollerats 2026-09-29 anger en exakt klockslag för publicering eller garanterar att rapporten publiceras öppet samma minut som den lämnas in.

## Primära källor att bevaka

1. **Energimarknadsinspektionen (Ei)** — samordnar uppdraget och lämnar redovisningen.
   - https://ei.se/
   - Ärendenummer i Ei:s konsultationsmaterial: `2025-103808`
2. **Svenska kraftnät** — gemensam uppdragspart och har en särskild sida för regeringsuppdraget.
   - https://www.svk.se/om-oss/verksamhet/vara-regeringsuppdrag/centralt-datahanteringsverktyg-for-elmarknaden/
   - Svenska kraftnäts ärendenummer: `Svk 2025/5201`
3. **Regeringen / Klimat- och näringslivsdepartementet** — mottagare av redovisningen.
   - https://www.regeringen.se/regeringsuppdrag/2025/09/uppdrag-till-energimarknadsinspektionen-och-svenska-kraftnat-att-ta-fram-forslag-till-ett-centralt-datahanteringsverktyg-for-elmarknaden/
   - Regeringens diarienummer: `KN2023/01385`, `KN2024/02551`, `KN2025/01781`

## Förväntade publiceringskanaler

Följ i första hand:

- Ei:s nyheter, rapporter och dokument;
- Svenska kraftnäts sida för regeringsuppdraget och nyheter;
- Regeringen.se för eventuell publicering av redovisning, pressmeddelande eller fortsatt beredning;
- Ei:s registratur om rapporten är inlämnad men ännu inte publicerad öppet.

Ei:s webbplats anger registraturens vardagstider som 08:00–17:00, men detta ska **inte** tolkas som en utlovad publiceringstid för rapporten.

## Tydel-frågor när rapporten finns

Rapporten ska analyseras innan Tydel låser långsiktiga antaganden om svensk marknadskommunikation:

1. Vilka marknadsprocesser föreslås centraliseras?
2. Vad föreslås hända med befintlig Ediel-kommunikation?
3. Vilka format, API:er, XML/CIM-profiler eller transportmekanismer föreslås?
4. Var ska teknisk och affärsmässig validering ske?
5. Hur modelleras fel, acknowledgements och avvisningar?
6. Vilken migrations-/övergångsperiod föreslås och vilka legacy-flöden består?
7. Vilka nya test-, onboarding- och integrationskrav läggs på marknadsaktörer?
8. Påverkas Tydels buyer, första validator-slice, roadmap eller nordiska expansionshypotes?

## Projektregel fram till analys

Fortsätt:

- normativa Ediel-/UTILTS-/APERAK-regler;
- taxonomi och evidence model;
- customer discovery-förberedelser;
- read-only validator-arkitektur som inte låser sig till ett enda transportformat.

Vänta med irreversibla beslut som förutsätter att dagens bilaterala svenska Ediel-landskap förblir oförändrat långsiktigt.

När rapporten publiceras ska Tydel göra en **strategisk checkpoint**: uppdatera product thesis, roadmap, architecture assumptions, customer-discovery questions och investeringsbedömning utifrån rapportens faktiska innehåll.
