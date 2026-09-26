# UTILTS och APERAK — aktuell verifierad evidens

> Status: researchunderlag. Dokumentet beskriver endast sådant som kan beläggas i auktoritativa källor. Det är ännu inte ett komplett validator-kontrakt.

## Syfte

Det här dokumentet flyttar Tydels research från bred processnivå mot konkreta `Message`, `MessageVersion`, `Rule` och `Acknowledgement` för en avgränsad svensk Ediel-process.

## Primära källor och giltighet

Svenska kraftnäts **BSP – Implementation guide FCR**, ärende `Svk 2021/3931`, är daterad **5 mars 2025** och anger **Valid from 28 April 2025**. Guiden beskriver integration mellan BSP och Fifty MMS och är därför stark evidens för just FCR-processen.

Edielportalens aktuella sida **Edielanvisningar** visar samtidigt en aktiv huvudkategori **`6. UTILTS-APERAK`** och beskriver att UTILTS och dess APERAK används för utbyte av **mätvärden och avräkningsinformation** mellan branschens aktörer. Portalen har en separat kategori **`11. Äldre anvisningar`** för anvisningar som har utgått. Detta är viktig editions-evidens: UTILTS–APERAK är inte bara ett historiskt dokumentnamn, utan ligger i portalens aktuella anvisningsstruktur per 2026-09-26.

Detta bevisar däremot **inte** ännu vilken enskild underliggande UTILTS-/APERAK-fil, edition eller profil som är normerande för varje svensk process. Den detaljen måste hämtas från dokumenten under den aktiva kategorin innan segmentkrav kan göras till validatorregler.

Källor:
- https://www.svk.se/siteassets/aktorsportalen/dokument-for-aktorer/dokument-for-reserver/implementationsguide_fcr_en_2025.pdf
- https://www.ediel.se/Info/edielanvisningar

## Evidenshierarki

För att undvika att ett exempel blir en påhittad standardregel använder Tydel följande ordning:

1. **Normativ profil-/Edielanvisning** — kan bära obligatoriska, villkorade och kodspecifika regler när edition och scope är verifierade.
2. **Aktuell process-/implementationsguide från marknadsansvarig** — stark evidens för process, message family, transport och processpecifika krav.
3. **Exempelfil i aktuell guide** — evidens för att en konkret struktur/version förekommer i guidens scope, men inte ensam bevis för generell obligatorisk segmentstruktur.
4. **Sekundär teknisk källa** — stöd för syntax/basstandard, aldrig ensam auktoritet för svensk Ediel-profil.

En validatorregel får inte uppgraderas från `example evidence` till `normative rule evidence` utan stöd från nivå 1 eller ett uttryckligt normativt krav på nivå 2.

## Verifierad FCR-message map

Guiden visar att Ediel används som dataformat och SMTP som kommunikationsprotokoll mellan BSP och Fifty MMS. Följande dokumentflöden anges uttryckligen:

| Riktning | Affärsobjekt | Message | Scope/status |
| --- | --- | --- | --- |
| BSP → Fifty MMS | FCR-bud | `QUOTES` | `CURRENT_SCOPED` |
| BSP → Fifty MMS | FCR-planer | `DELFOR` | `CURRENT_SCOPED` |
| Fifty MMS → BSP | accepterade bud | `UTILTS S08` | `CURRENT_SCOPED` |
| Fifty MMS → BSP | committed plan | `UTILTS S01` | `CURRENT_SCOPED` |
| Fifty MMS → BSP | activated energy | `UTILTS S01` | `CURRENT_SCOPED` |

Detta bevisar inte att samma profiler gäller andra svenska Ediel-processer.

## Verifierade UTILTS-versioner och processkoder

Appendix B innehåller konkreta UTILTS-exempel. För activated energy visas:

```text
UNH+1+UTILTS:D:02B:UN:E5SE9B'
BGM+S01:SVK:260+DOCUMENTID+9+AB'
```

Det ger evidens för:

- `Message = UTILTS`
- directory/version `D:02B`
- svensk/profilspecifik identifierare `E5SE9B`
- `BGM` document type `S01` för den visade settlement/activated-energy-kedjan

Guiden anger dessutom tidsserieprodukterna:

- committed plan: `S195` FCR-N, `S197` FCR-D upp, `S437` FCR-D ned;
- activated energy: `S402` FCR-N, `S403` FCR-D upp/ned;
- accepted bids: `UTILTS S08`, med `S419/S420`, `S423/S424` och `S431/S432` för respektive produkt/auktion.

Alla dessa klassificeras `CURRENT_SCOPED` till FCR-guidens scope.

## Verifierade generella regler inom FCR-scope

Guidens avsnitt 2.4 ger flera regelkandidater som kan uttryckas deterministiskt när validator-scope låsts:

- datum och tider uttrycks i UTC;
- document identification ska vara unik för avsändaren;
- ett nytt mottaget dokument ersätter i normalfallet tidigare dokument enligt guidens update/cancel-principer;
- acknowledgement accepterar eller avvisar hela mottagna dokumentet, partial acceptance används inte;
- APERAK-exempel finns för `UTILTS`, `DELFOR` och `QUOTES`.

Dessa regler ska fortfarande scope-bindas till FCR/Fifty MMS och inte lyftas till globala svenska Ediel-regler utan separat stöd.

## Verifierad APERAK-relation för UTILTS

Appendix C visar:

```text
UNH+1+APERAK:D:04A:UN:E5SE9B'
BGM+312+99900033+9'
DOC+E31::260+205436160319'
ERC+100::260'
RFF+ACW:MD200205832134'
```

Guidens kommentarer anger:

- `312` = positiv APERAK;
- `313` = negativ APERAK;
- `DOC` refererar till UTILTS message type/message number;
- `RFF+ACW` refererar till UTILTS-transaktionen;
- `ERC+100` betyder i det positiva exemplet att transaktionen är godkänd.

Taxonomikedjan kan därför uttryckas:

```text
Process: FCR
→ Transaction: accepted bid | committed plan | activated energy
→ Message: UTILTS
→ MessageVersion: D:02B:UN:E5SE9B [belagd i activated-energy-exempel]
→ subtype: S08 | S01 [scope enligt transaktion]
→ TransportProfile: SMTP
→ Acknowledgement: APERAK
→ AcknowledgementVersion: D:04A:UN:E5SE9B
→ positive BGM: 312
→ negative BGM: 313
```

### APERAK skiljer sig mellan message-familjer

Samma Appendix C visar ett separat acknowledgement-exempel för `DELFOR/QUOTES`:

```text
UNH+1+APERAK:D:96A:UN:E2SE3B'
BGM+++29'
RFF+ACW:A438775'
```

Guiden anger `29` som positiv och `27` som negativ APERAK för detta exempel. Detta är viktig evidens för att Tydel **inte får modellera APERAK som en enda global version/koduppsättning**. Acknowledgement-regler måste bindas till message family/process/profile.

## Kandidater till deterministiska regler

| Rule candidate | Evidens | Status |
| --- | --- | --- |
| Aktiv Edielkategori `6. UTILTS-APERAK` används för mätvärden och avräkningsinformation | Edielportalen, aktuell Edielanvisningssida | `CURRENT` på kategorinivå; profil/edition ännu `UNVERIFIED` |
| FCR activated energy använder `UTILTS:D:02B:UN:E5SE9B` i guideexemplet | Svk FCR 2025 Appendix B | `CURRENT_SCOPED` |
| FCR committed plan/activated energy använder `S01` | Svk FCR 2025 §2.3.2 | `CURRENT_SCOPED` |
| Accepted bids använder `UTILTS S08` | Svk FCR 2025 §2.3.2.1 | `CURRENT_SCOPED` |
| UTILTS acknowledgement använder APERAK i processen | Svk FCR 2025 §2.4.4 + Appendix C | `CURRENT_SCOPED` |
| UTILTS APERAK-profil i exemplet är `D:04A:UN:E5SE9B` | Appendix C | `CURRENT_SCOPED` |
| Positiv/negativ UTILTS-APERAK anges som `312/313` | Appendix C | `CURRENT_SCOPED` |
| `DOC` och `RFF+ACW` länkar acknowledgement till UTILTS message/transaction | Appendix C | `CURRENT_SCOPED` |
| DELFOR/QUOTES använder annan APERAK-profil/koder i exemplet | Appendix C | `CURRENT_SCOPED` |
| Partial acceptance används inte i FCR acknowledgement | Svk FCR 2025 §2.4.4 | `CURRENT_SCOPED` |

## Vad som fortfarande är UNVERIFIED

För ett säkert första validator-kontrakt behöver vi fortfarande verifiera mot dokumenten under Edielportalens aktiva `6. UTILTS-APERAK`:

1. exakt dokumenttitel, edition/revision och giltighetsdatum för aktuell UTILTS- och APERAK-anvisning;
2. om `UTILTS:D:02B:UN:E5SE9B` är normerande för den valda processen och inte bara formatet i FCR-exemplet;
3. obligatoriska och villkorade segment för vald profil;
4. kompletta qualifiers och kodlistor;
5. negativ APERAK-semantik och samtliga felkoder;
6. exakt vilka acknowledgement-regler som varierar mellan UTILTS-transaktionstyper;
7. om guideexemplen innehåller historiska exempelvärden som inte ska tolkas som dagens affärsregler.

## Taxonomikonsekvens

Tydels modell behöver kunna uttrycka både format, transport, scope och evidens:

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

Varje nod/regelkandidat behöver minst:

- `status`: `CURRENT | CURRENT_SCOPED | TRANSITIONAL | LEGACY | UNVERIFIED`
- `scope`
- `source`
- `source_date_or_edition`
- `valid_from` / `valid_to` när källan stödjer det
- `evidence_level`: `NORMATIVE | PROCESS_GUIDE | EXAMPLE | SECONDARY`
- `evidence_note`

## Nästa researchsteg

1. hämta metadata och innehåll för dokumenten under Edielportalens aktiva `6. UTILTS-APERAK`;
2. editionsbestäm den fullständiga aktuella UTILTS-/APERAK-profilen;
3. jämför dess segment- och kodkrav mot FCR-guiden;
4. uppgradera endast uttryckligen stödda kandidater från `example evidence` till `normative rule evidence`;
5. därefter föreslå ett första validator-kontrakt och positiva/negativa fixtures utan antaganden.
