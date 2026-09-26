# Leverantörsbyte — verifierad processgrund

> **Status:** research under M0. Detta dokument skiljer uttryckligen på verifierade affärs-/rapporteringskrav och ännu ej verifierad teknisk Ediel message/profile.

## Vad vi kan slå fast nu

Aktuella svenska myndighetskällor visar att ett elleverantörsbyte är en Ediel-relevant process. När en elleverantör har ingått ett giltigt avtal ska elleverantören omedelbart meddela kundens nätföretag. Anmälan ska bland annat identifiera elleverantören med dess eget Ediel-id; ett ombuds Ediel-id får inte användas som ersättning för elleverantörens identitet.

Nätföretaget registrerar den nya elleverantören och ska i processen också informera kunden. Efter ett genomfört byte börjar nätföretaget rapportera kundens mätvärden till den nya elleverantören.

EIFS 2025:1 anger dessutom en generell kommunikationsregel för de rapporter, anmälningar och underrättelser som omfattas av föreskriftens 7–11 kapitel: de ska ske elektroniskt i Ediel-format. Mottagaren ska kvittera mottagna Ediel-meddelanden inom 30 minuter. Avsändaren ska kontrollera kvittensen och, om kvittens saknas, uppmärksamma mottagaren inom tre vardagar.

## Verifierade Actor-objekt

| Tydel actor | Svensk roll | Evidensstatus |
|---|---|---|
| `electricity_supplier_new` | Ny elleverantör / elhandelsföretag | `CURRENT` |
| `network_operator` | Nätföretag / elnätsföretag | `CURRENT` |
| `electricity_supplier_existing` | Befintlig elleverantör | `CURRENT` för nätföretagets efterföljande underrättelse, men teknisk message/profile ej verifierad här |
| `customer` | Elanvändare/kund | `CURRENT` som affärsroll; inte nödvändigtvis Ediel-part i varje transaction |

## Process och transactions

| Process | Transaction | Från | Till | Krav vi kan verifiera | Message/profile | Status |
|---|---|---|---|---|---|---|
| Leverantörsbyte | Anmälan om övertagande/byte | Ny elleverantör | Nätföretag | Ska skickas efter giltigt avtal; eget Ediel-id ingår i identiteten | **Ej verifierad ännu** | Affärsrelation `CURRENT`, teknisk profil `UNVERIFIED` |
| Leverantörsbyte | Meddelande om byte till kund | Nätföretag | Kund | Nätföretaget informerar kunden om registrerat byte | Kundkanal behandlas separat från Ediel B2B | `CURRENT` |
| Leverantörsbyte | Underrättelse till befintlig elleverantör | Nätföretag | Befintlig elleverantör | Aktuell föreskrift innehåller krav på meddelande efter fullständig anmälan | **Ej verifierad ännu** | Affärsrelation `CURRENT`, teknisk profil `UNVERIFIED` |
| Generell Ediel-kommunikation enligt EIFS 2025:1 | Kvittens | Mottagare | Avsändare | Kvittens inom 30 minuter för omfattade Ediel-meddelanden | Exakt ack-message/profile **ej verifierad ännu** | Krav `CURRENT`, teknisk profil `UNVERIFIED` |

## Fält som är relevanta men ännu inte validatorregler

Ei:s aktuella material stödjer att Ediel-id är centralt vid leverantörsbyte och att elleverantören ska ange sitt eget Ediel-id. Föreskriften beskriver dessutom informationsmängder för nätföretagets meddelanden i processen, exempelvis anläggningsidentitet, områdesidentitet, balansansvarigs identitet, orsak och sluttidpunkt i vissa transactions.

Dessa informationskrav får **inte** översättas direkt till segment-/elementregler förrän Tydel har kopplat dem till en aktuell, auktoritativ Ediel message/profile och dess implementation guide.

## Acknowledgement-modell

Tydel ska tills vidare modellera två separata saker:

1. `ack_requirement`: den rättsligt/processmässigt verifierade skyldigheten att kvittera inom 30 minuter.
2. `ack_message_profile`: den konkreta tekniska Ediel-meddelandetyp/version som används för kvittensen.

Den första är verifierad i EIFS 2025:1. Den andra lämnas `UNVERIFIED` tills en aktuell Svenska kraftnät-specifikation eller motsvarande auktoritativ profilkälla har verifierats.

Detta hindrar ett vanligt modellfel: att anta att en känd EDIFACT acknowledgement automatiskt är den aktuella svenska profilen.

## Nästa researchsteg

1. Hitta aktuell Svenska kraftnät/Ediel-specifikation för leverantörsbyte.
2. Verifiera exakt message name, directory/version och svensk profile för varje B2B-transaction.
3. Verifiera den tekniska acknowledgement/reject-relationen.
4. Koppla varje obligatoriskt informationsfält i EIFS 2025:1 till exakt segment/element först när implementation guide stödjer relationen.
5. Jämför med äldre profiler och märk dem `LEGACY` eller `TRANSITIONAL` där detta kan beläggas.

## Auktoritativa källor använda i detta researchpass

- Energimarknadsinspektionen, **EIFS 2025:1 — föreskrifter och allmänna råd om mätning och rapportering av överförd el**. Särskilt 1 kap. 4 § om Ediel-format, kvittens inom 30 minuter och hantering av saknad kvittens.
- Energimarknadsinspektionen, **Ei granskar fem elhandelsföretags rutiner vid leverantörsbyte**, 2026-04-13. Bekräftar aktuell tillämpning av leverantörsbytesprocessen och kravet på elleverantörens eget Ediel-id.
- Energimarknadsinspektionen, **Ei inleder tillsyn av byte av elleverantör och förtydligar krav i föreskrifter**, 2025-04-11. Beskriver flödet från elleverantör till nätföretag och att mätvärdesrapportering följer efter registrerat byte.
- Svenska kraftnät, **Använda Ediel**. Bekräftar Ediel som standardiserat informationsutbyte på elmarknaden och nämner leverantörsbyte samt mät-/handelsvärden som användningsfall.

## Säkerhetsnotering

Det här dokumentet innehåller ännu **ingen** godkänd segmentvalidator för leverantörsbyte. `CURRENT` på en affärsrelation betyder inte att Tydel känner den aktuella EDIFACT/XML-profilen. Den gränsen ska vara synlig i både dokumentation och framtida maskindata.
