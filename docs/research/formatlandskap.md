# Formatlandskap för svensk Ediel-kommunikation

**Status:** Researchunderlag. Senast verifierat 2026-09-26.

Det här dokumentet skiljer på **Ediel som informationsutbyte** och de konkreta syntax-/transportformat som används i olika processer. Målet är att förhindra att Tydel bygger in antagandet `Ediel = EDIFACT`.

## Verifierad nulägesbild

Svenska kraftnät beskriver Ediel som systemet för standardiserat elektroniskt informationsutbyte mellan elmarknadens aktörer, bland annat för mätvärden, handelsvärden och leverantörsbyten.

Svenska kraftnäts aktuella information om reservmarknader visar samtidigt att Edielanvisningar kan avse flera formatfamiljer:

- traditionella **EDIFACT**-meddelanden, med exempel som `QUOTES`, `APERAK` och `DELFOR`;
- **XML**, ofta CIM-baserat enligt ENTSO-E;
- olika transportkanaler beroende på process, exempelvis SMTP och ECP.

Det betyder att Tydels framtida modell måste separera **affärsprocess**, **message/profile**, **syntax/format** och **transport**.

## Balansavräkning och eSett

eSetts NBS Handbook version 5.4, uppdaterad juni 2026, beskriver Messaging Service för informationsutbyte i balansavräkningen. För svenska marknadsaktörer anges SMTP som kommunikationskanal till/från eSett. Handbook hänvisar till Edielportalen för svenska detaljer och anger uttryckligen att eSett tillhandahåller `UTILTS`-data packages för svensk profiling/reconciliation, definierade tillsammans med `APERAK` i svensk Ediel-anvisning.

Detta ger oss starkare evidens än tidigare för att `UTILTS` och `APERAK` fortfarande har en **aktuell roll i åtminstone den avgränsade svenska profiling/reconciliation-processen**. Det bevisar däremot inte att samma profiler gäller för all svensk mätvärdesrapportering eller alla balansavräkningsflöden.

### Klassificering

| Område | Message / format | Status | Vad källan faktiskt stödjer |
|---|---|---|---|
| Ediel generellt | EDIFACT | `CURRENT_FAMILY` | Används fortfarande i vissa processer |
| Ediel generellt | XML / CIM | `CURRENT_FAMILY` | Används i moderna processer |
| Reservmarknad, FCR | EDIFACT via SMTP | `CURRENT_PROCESS` | Svenska kraftnät anger detta explicit |
| Reservmarknad, mFRR bud/avrop | CIM via ECP | `CURRENT_PROCESS` | Svenska kraftnät anger detta explicit |
| Svensk profiling/reconciliation via eSett | UTILTS | `CURRENT_SCOPED` | NBS Handbook 5.4 anger UTILTS data packages för Sverige |
| Svensk profiling/reconciliation | APERAK | `CURRENT_SCOPED_REFERENCE` | Handbook hänvisar till aktuell UTILTS & APERAK-guide i Edielportalen |
| All svensk mätvärdesrapportering | UTILTS | `UNVERIFIED` | Får inte generaliseras från profiling/reconciliation |
| Exakt UTILTS-version/implementation profile | ? | `UNVERIFIED` | Kräver aktuell Ediel-anvisning |
| Exakt APERAK-version/qualifiers | ? | `UNVERIFIED` | Kräver aktuell Ediel-anvisning |

## Konsekvens för taxonomin

Den tidigare kedjan behöver kompletteras utan att förstöra kärnmodellen:

```text
Actor
  → Process
    → Transaction
      → Message
        → MessageVersion
          → SyntaxFormat
          → TransportProfile
          → Rule
            → Acknowledgement
              → Error
                → Resolution
```

`SyntaxFormat` och `TransportProfile` bör vara egna dimensioner, inte härledas implicit från meddelandenamnet.

Exempel på framtida representation:

```yaml
message:
  id: se.reconciliation.utilts
  status: CURRENT_SCOPED
  scope: Swedish profiling/reconciliation
  syntax_format: EDIFACT
  transport_profile:
    channel: SMTP
    status: CURRENT_FOR_SWEDISH_ESETT_PARTIES
  acknowledgement:
    message: APERAK
    version: UNVERIFIED
```

Exemplet ovan är en **modellskiss**, inte en färdig regelpost. Versions- och qualifierdata ska inte fyllas i innan den aktuella Ediel-anvisningen är verifierad.

## Övergångar: legacy / current / transitional

Tydel bör inte använda en enda etikett `legacy` för EDIFACT. Dagens källor visar ett parallellt landskap där EDIFACT fortfarande är aktuellt i vissa processer medan CIM/XML används i andra. Klassificering ska därför göras per process/profile:

- `CURRENT` — verifierat aktuellt för specificerad process;
- `CURRENT_SCOPED` — aktuellt, men bara inom uttryckligen avgränsad process;
- `TRANSITIONAL` — verifierad pågående övergång där gammalt och nytt samexisterar;
- `LEGACY` — verifierat historiskt/ersatt för den specifika processen;
- `UNVERIFIED` — otillräckligt källstöd.

## Källor

1. Svenska kraftnät, **Använda Ediel** — https://www.svk.se/aktorsportalen/it-systemsupport/anvanda-ediel/
2. Svenska kraftnät, **Finns det möjlighet att lämna bud via annat än EDIEL nu eller är något sådant på gång?** — https://www.svk.se/aktorsportalen/bidra-med-reserver/fragor-och-svar-om-reserver/ediel/finns-mojlighet-att-lamna-bud-via-annat-an-ediel-nu-eller-ar-nagot-sadant-pa-gang/
3. eSett, **NBS Handbook 5.4**, uppdaterad juni 2026 — https://www.esett.com/handbook/

## Nästa verifieringssteg

1. Hämta aktuell `UTILTS & APERAK`-anvisning från Edielportalen.
2. Lås exakt profile/version, relevanta qualifiers och acknowledgement-semantik.
3. Separera svensk profiling/reconciliation från generell mätvärdesrapportering i taxonomin.
4. Kartlägg därefter fler processer med samma `Process → Message → Format → Transport`-disciplin.
