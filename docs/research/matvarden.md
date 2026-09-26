# Mätvärdesrapportering i svensk Ediel

> Status: **RESEARCH / PARTIALLY VERIFIED**  
> Senast verifierad: **2026-09-26**

Det här dokumentet beskriver endast sådant om svensk mätvärdesrapportering som kan beläggas med öppna, auktoritativa källor. Exakta Ediel-message profiles, segmentregler och versionsnummer markeras `UNVERIFIED` tills motsvarande aktuell Ediel-anvisning har verifierats.

## Verifierad processgrund

Svenska kraftnät beskriver Ediel som det standardiserade elektroniska informationsutbyte som används av elmarknadens aktörer, bland annat för **mätvärden**, **handelsvärden** och information om leverantörsbyten.

Energimarknadsinspektionen (Ei) anger i EIFS 2025:1 att rapportering av mätvärden, andelstal samt vissa anmälningar och underrättelser till elleverantör, balansansvarig, nätföretag och Svenska kraftnät, eller den som Svenska kraftnät utsett, ska ske elektroniskt i Ediel-format.

## Aktörer som kan beläggas

| Actor | Roll i den verifierade processgrunden | Status |
| --- | --- | --- |
| Nätföretag | Ansvarar för mätning och rapporterar mätvärden enligt tillämpliga regler | VERIFIED |
| Elleverantör | Mottagare i Ediel-rapporteringsprocesser enligt EIFS 2025:1 | VERIFIED |
| Balansansvarig (BRP) | Mottagare i Ediel-rapporteringsprocesser enligt EIFS 2025:1 | VERIFIED |
| Svenska kraftnät / utsedd part | Mottagare i Ediel-rapporteringsprocesser enligt EIFS 2025:1 | VERIFIED |
| Elanvändare / elproducent | Kan få mätvärden/underrättelser via nätföretagets Mina sidor; Ediel används om användaren eller producenten begär det enligt föreskriften | VERIFIED |

## Kvittenskrav

EIFS 2025:1 anger att mottagaren av Ediel-meddelanden ska kvittera mottagna meddelanden **inom 30 minuter** efter att rapporter och underrättelser kommit mottagaren tillhanda.

Avsändaren ska kontrollera att meddelandet har kvitterats. Vid saknad kvittens ska mottagaren uppmärksammas på detta **inom tre vardagar**.

Detta är ett verifierat **business/communication requirement**. Det innebär inte i sig att vi har verifierat vilket specifikt EDIFACT- eller XML-meddelande som används som kvittens i varje process.

```yaml
ack_requirement:
  status: VERIFIED
  deadline: PT30M
  missing_ack_followup: P3_BUSINESS_DAYS
ack_message_profile:
  status: UNVERIFIED
```

## Format och versioner

Ei anger att mottagare och avsändare ska rapportera i format som vid var tid är godkända av Svenska kraftnät. Svenska kraftnät hänvisar till Ediel-portalen och dess Ediel-anvisningar för de aktuella meddelandena.

Därför gäller följande i Tydel:

- `Ediel` kan markeras `CURRENT` som kommunikations-/meddelanderam för de processer som föreskriften omfattar.
- Ett specifikt message name, exempelvis `UTILTS`, får **inte** markeras `CURRENT` enbart därför att namnet förekommer i äldre material eller befintliga fixtures.
- Message version, profile, qualifiers och segmentregler ska vara `UNVERIFIED` tills aktuell Svenska kraftnät-anvisning har verifierats.

## Kvartsmätning och tidsupplösning

Ei:s tillsyn 2025 visar att den svenska marknaden gick över till kvartsmätvärden som en central del av övergången till 15-minuters handel. Detta styr vilken tidsupplösning Tydel måste kunna representera, men bevisar inte på egen hand vilket Ediel-message profile som bär värdena.

```yaml
measurement_resolution:
  quarter_hour_values:
    status: VERIFIED_MARKET_REQUIREMENT
message_profile_for_quarter_hour_values:
  status: UNVERIFIED
```

## Taxonomisk representation

```text
Actor
  Nätföretag
      ↓
Process
  Mätning och rapportering av överförd el
      ↓
Transaction
  Rapportera mätvärden
      ↓
Message
  UNVERIFIED
      ↓
MessageVersion
  UNVERIFIED
      ↓
Rule
  Använd av Svenska kraftnät godkänt format
      ↓
Acknowledgement
  Kvittens inom 30 minuter
      ↓
Error
  Saknad kvittens / format- eller profilfel
      ↓
Resolution
  Uppmärksamma mottagaren vid saknad kvittens inom tre vardagar;
  övrig resolution kräver verifierad profilregel
```

## Öppna frågor

1. Vilket eller vilka Ediel-meddelanden är aktuellt godkända för respektive svensk mätvärdesprocess?
2. Vilka versioner/profiler gäller för kvartsvärden 2026?
3. Vilket meddelande används för teknisk respektive affärsmässig kvittens i varje profil?
4. Vilka qualifiers skiljer uttag, produktion, gränspunkter och andra mätserier?
5. Vilka delar av äldre EDIFACT-flöden är `CURRENT`, `TRANSITIONAL` respektive `LEGACY`?

Dessa frågor ska lösas mot aktuell Ediel-anvisning eller annan uttryckligt auktoritativ källa innan de blir validatorregler.

## Källor

- Svenska kraftnät, **Använda Ediel**: https://www.svk.se/aktorsportalen/it-systemsupport/anvanda-ediel/
- Svenska kraftnät, **Elektronisk kommunikation**: https://www.svk.se/aktorsportalen/for-nya-aktorer/elektronisk-kommunikation/
- Energimarknadsinspektionen, **EIFS 2025:1 om mätning och rapportering av överförd el**, särskilt 1 kap. 4–5 §§: https://ei.se/download/18.5094606019684fe27e01895/1746156902909/EIFS-2025-1-om-m%C3%A4tning-och-rapportering-av-%C3%B6verf%C3%B6rd-el.pdf
- Energimarknadsinspektionen, **Mätning av el**: https://ei.se/bransch/matning-av-el
- Energimarknadsinspektionen, **Ei har granskat elnätsföretagens förmåga att mäta och rapportera kvartsmätvärden**, 2025-05-21: https://ei.se/om-oss/nyheter/2025/2025-05-21-ei-har-granskat-elnatsforetagens-formaga-att-mata-och-rapportera-kvartsmatvarden
