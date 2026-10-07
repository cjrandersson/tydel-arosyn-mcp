# TYDEL: ECONOMIC-PAIN SCORECARD (M0-CD)

Detta verktyg används för att kvantifiera den faktiska ekonomiska kostnaden för informationsstörningar (negativa APERAK/CONTRL, försenade eller felaktiga mätvärden) hos marknadens aktörer.

## Kärnformeln för beräkning av smärta (Ekonomisk förlust per år)
För att beräkna den totala årliga kostnaden för ett specifikt fel används följande struktur:

   (Frekvens per år × Genomsnittlig felsökningstid i timmar × Specialistkostnad per timme) 
   + Direkta följdekostnader (Skadestånd, förlorad ränta, manuell hantering av kundtjänst)
   = Total årlig finansiell blödning

---

## Metrik och poängsättning (Scorecard)

### 1. Frekvens (Hur ofta uppstår felet?)
*   [1 poäng] **Låg:** Enstaka fall per månad eller kvartal.
*   [3 poäng] **Medium:** Flera gånger i veckan. Kräver löpande uppmärksamhet.
*   [5 poäng] **Hög:** Dagligen/Konstant. Integrationsköer fastnar regelbundet.

### 2. Felsökningstid (Investigation Time per incident)
*   [1 poäng] **Kort (< 30 min):** Felet syns direkt i en logg och kan åtgärdas direkt.
*   [3 poäng] **Medium (2–8 timmar):** Kräver att man gräver i EDIFACT-filer, jämför masterdata mot eSett/Hubben och bollar ärendet mellan IT och affärssidan.
*   [5 poäng] **Lång (> 1 dygn / veckor):** Asynkrona fel där man måste vänta på svar från motpartens IT-support. Kräver möten mellan flera organisationer.

### 3. Resurskostnad (Vem felsöker?)
*   [Standardvärde Handläggare]: ~450 kr / timme (inkl. overhead)
*   [Standardvärde Specialist/Konsult/Arkitekt]: ~1 000 kr / timme (inkl. overhead)

### 4. Affärskonsekvens & Följdekostnader
*   [1 poäng] **Minimal:** Endast internt IT-brus. Inga externa effekter.
*   [3 poäng] **Måttlig:** Försenad fakturering för en mindre grupp kunder. Några arga samtal till kundtjänst.
*   [5 poäng] **Kritisk:** Totalstopp i fakturering, avtalsbrott vid leverantörsbyte med skadeståndskrav, eller felaktiga timprisavräkningar som leder till regulatoriska straffavgifter från Energimarknadsinspektionen (Ei).

---

## Exempelsenario (Försening/Fel i MSCONS till Elhandlare)
*   **Frekvens:** 20 incidenter per månad (240 per år) -> **[3] Medium**
*   **Felsökningstid:** 4 timmar per incident -> **[3] Medium**
*   **Resurs:** Senior integrationsutvecklare (1 000 kr/h)
*   **Beräkning:** 240 × 4 × 1 000 = **960 000 kr / år i ren utvecklingstid.**
*   **Följdekostnad:** Ränteförlust och likviditetsproblem på grund av 3 veckors försenad fakturering av 5 000 000 kr = **~50 000 kr**.
*   **Total finansiell smärta för detta enda fel: 1 010 000 kr / år.**
