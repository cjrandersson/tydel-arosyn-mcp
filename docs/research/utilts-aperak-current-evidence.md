# UTILTS och APERAK — aktuell verifierad evidens

> Status: researchunderlag. Dokumentet beskriver endast sådant som kan beläggas i auktoritativa källor. Det är ännu inte ett komplett validator-kontrakt.

## Syfte

Det här dokumentet flyttar Tydels research från bred processnivå mot konkreta `Message`, `MessageVersion`, `Rule` och `Acknowledgement` för en avgränsad svensk Ediel-process.

## Primära källor och giltighet

Svenska kraftnäts **BSP – Implementation guide FCR**, ärende `Svk 2021/3931`, är daterad **5 mars 2025** och anger **Valid from 28 April 2025**. Guiden beskriver integration mellan BSP och Fifty MMS och är därför stark evidens för just FCR-processen.

Edielportalens aktuella sida **Edielanvisningar** visar en aktiv huvudkategori **`6. UTILTS-APERAK`** och beskriver att UTILTS och dess APERAK används för utbyte av **mätvärden och avräkningsinformation** mellan branschens aktörer. Portalen har en separat kategori **`11. Äldre anvisningar`** för anvisningar som har utgått.

Den aktuella svenska UTILTS/APERAK-anvisningen är editionsbestämd i Tydels referensbibliotek som:

- source `se-ediel-3333`;
- `251001_Ediel_UTILTS-APERAK_Anvisning_version_25-A-3.pdf`;
- UTILTS **D.02B**;
- profil **E5SE5A**;
- revision **3**;
- giltig från **2025-06-01** enligt dokumentets cover evidence.

Den engelska motsvarigheten är source `se-ediel-3334`. Edielportalen listar dessutom revision **4** (`se-ediel-3364` / `se-ediel-3365`) med giltighet från **2026-10-01**. Per **2026-09-28** är revision 4 därför future-effective och revision 3 den aktuella edition som ska användas som utgångspunkt för M0-research. Publication/filename-datum får inte förväxlas med `effective_from`.

Det finns en dokumenterad publisher-label-avvikelse för den svenska revision-4-filen: filnamnet slutar i `25-A-4` medan page footer enligt tidigare cover review visar `25-A-5`; cover anger revision 4. Tydel bevarar avvikelsen som evidens och gissar inte vilket label som avsågs.

Editionsbestämningen löser **inte** automatiskt vilka segment-, qualifier- och affärsregler som är normativa för Tydels första validator-slice. Dessa måste fortfarande extraheras och scope-bindas från den aktuella anvisningen innan de får bli validatorregler.

Källor:
- https://www.svk.se/siteassets/aktorsportalen/dokument-for-aktorer/dokument-for-reserver/implementationsguide_fcr_en_2025.pdf
- https://www.ediel.se/Info/edielanvisningar
- https://www.ediel.se/Portal/Document/3333
- https://www.ediel.se/Portal/Document/3334
- https://www.ediel.se/Portal/Document/3364
- https://www.ediel.se/Portal/Document/3365
- `reference/catalogs/ediel-se.json`
- `reference/download-lock.json`

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
| Aktiv Edielkategori `6. UTILTS-APERAK` används för mätvärden och avräkningsinformation | Edielportalen, aktuell Edielanvisningssida | `CURRENT` på kategorinivå |
| Aktuell UTILTS/APERAK-guide är revision 3, UTILTS D.02B / E5SE5A, giltig från 2025-06-01 | `se-ediel-3333` / `se-ediel-3334`, cover evidence | `CURRENT` edition identity; full rule extraction pending |
| Revision 4 är giltig från 2026-10-01 | `se-ediel-3364` / `se-ediel-3365`, cover evidence | `TRANSITIONAL` / future-effective per 2026-09-28 |
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

Editionsidentiteten är nu verifierad, men följande måste fortfarande lösas innan ett säkert första validator-kontrakt kan låsas:

1. obligatoriska och villkorade segment i den **aktuella revision-3-profilen** för vald transaction/message-slice;
2. kompletta qualifiers och kodlistor för den valda slicen;
3. relationen mellan den generella E5SE5A-guiden och processpecifika profiler/exempel såsom FCR:s E5SE9B;
4. negativ APERAK-semantik och samtliga relevanta felkoder för vald profil;
5. exakt vilka acknowledgement-regler som varierar mellan UTILTS-transaktionstyper;
6. vilka guideexempel som endast är illustrativa och vilka krav som uttryckligen är normativa;
7. om revision 4, giltig från 2026-10-01, ändrar någon regel som påverkar den första pilot-/M1-slicen.

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

1. läs den aktuella revision-3-anvisningen (`se-ediel-3333` / `se-ediel-3334`) på regel-/segmentnivå för en smal kandidat-slice;
2. markera varje härledd regel som `NORMATIVE`, `PROCESS_GUIDE`, `EXAMPLE` eller `SECONDARY`;
3. jämför de normativa revision-3-kraven mot FCR-guidens E5SE9B-exempel utan att generalisera mellan profiler;
4. kontrollera revision-4-deltat för regler som blir giltiga 2026-10-01;
5. uppgradera endast uttryckligen stödda kandidater till validatorregler;
6. därefter föreslå första validator-kontraktet och positiva/negativa fixtures utan antaganden.
