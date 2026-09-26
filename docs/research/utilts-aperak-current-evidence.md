# UTILTS och APERAK — aktuell verifierad evidens

> Status: researchunderlag. Dokumentet beskriver endast sådant som kan beläggas i auktoritativa källor. Det är inte ännu ett komplett validator-kontrakt.

## Syfte

Det här dokumentet flyttar Tydels research från den breda processnivån närmare konkreta `Message`, `MessageVersion`, `Acknowledgement` och `Rule` för en avgränsad svensk Ediel-process.

## Verifierad aktuell användning

Svenska kraftnäts implementationsguide för FCR (2025) anger att både **committed plan FCR** och **activated energy FCR** skickas en gång per dag efter leveransdygnets slut i **UTILTS-format, UTILTS S01**. Guiden hänvisar uttryckligen vidare till Edielportalens avsnitt `6. UTILTS-APERAK` för ytterligare information om tidsserieprodukterna.

Detta räcker för att klassificera UTILTS som `CURRENT_SCOPED` för denna process. Det bevisar inte att UTILTS är den generella aktuella profilen för all svensk mätvärdes- eller handelsvärdesrapportering.

Källa: Svenska kraftnät, *BSP – Implementationsguide FCR*, 2025, avsnitt 2.3.2.2–2.3.2.3 och Appendix C.

- https://www.svk.se/siteassets/aktorsportalen/dokument-for-aktorer/dokument-for-reserver/implementationsguide_fcr_sv_2025.pdf
- Edielportalens hänvisade anvisningssida: https://www.ediel.se/Info/edielanvisningar

## Verifierad acknowledgement-relation

Samma aktuella implementationsguide innehåller Appendix C med exempel på **positiv APERAK för UTILTS**. Exemplet visar bland annat:

- `UNH+1+APERAK:D:04A:UN:E5SE9B'`
- `BGM+312+...` för positiv APERAK
- guiden anger `313` för negativ APERAK
- `DOC+E31::260+...` refererar till UTILTS-meddelandet och dess meddelandenummer
- `RFF+ACW:...` refererar till UTILTS-transaktionen
- `ERC+100::260` används i det positiva exemplet för godkänd transaktion

Detta ger konkret evidens för följande avgränsade taxonomikedja:

```text
Process: FCR reporting
  → Transaction: committed plan / activated energy
  → Message: UTILTS
  → scoped subtype/profile evidence: S01
  → Acknowledgement: APERAK
  → acknowledgement version evidence: D:04A:UN:E5SE9B
  → positive BGM code: 312
  → negative BGM code: 313
```

### Viktig avgränsning

Exempelfilen visar en konkret APERAK-version och semantik i en aktuell Svenska kraftnät-guide. Tydel ska **inte** därifrån anta att `D:04A:UN:E5SE9B`, BGM-koderna eller samtliga segmentregler gäller universellt för alla svenska UTILTS-processer. De klassificeras tills vidare som `CURRENT_SCOPED` till den process/evidens där de är belagda.

## Kandidater till framtida deterministiska regler

Följande är nu tillräckligt konkreta för att registreras som **rule candidates**, men de ska inte bli produktionsregler innan det aktuella validator-scope:et har låsts och motsvarande officiella profilkrav har verifierats:

| Kandidat | Evidens | Status |
| --- | --- | --- |
| APERAK kan kvittera UTILTS | Svk FCR 2025 Appendix C | `CURRENT_SCOPED` |
| Positiv APERAK använder BGM 312 i exemplet | Svk FCR 2025 Appendix C | `CURRENT_SCOPED` |
| Negativ APERAK anges som BGM 313 | Svk FCR 2025 Appendix C | `CURRENT_SCOPED` |
| APERAK refererar till UTILTS message/transaction | `DOC` och `RFF+ACW` i Svk-exemplet | `CURRENT_SCOPED` |
| APERAK-profil `D:04A:UN:E5SE9B` | Svk FCR 2025 Appendix C | `CURRENT_SCOPED` |

## Vad som fortfarande är UNVERIFIED

För ett säkert första validator-kontrakt behöver vi fortfarande verifiera mot den aktuella fullständiga UTILTS–APERAK-anvisningen:

1. exakt aktuell UTILTS `UNH`-profil/version för vald svensk process;
2. obligatoriska och villkorade segment för just den profilen;
3. samtliga tillåtna qualifiers och kodlistor;
4. negativ APERAK-semantik och felkoder utöver att BGM 313 anges;
5. om acknowledgement-regler varierar mellan olika UTILTS-transaktionstyper;
6. editions-/giltighetsdatum så att Tydel kan välja rätt regelverk historiskt.

## Taxonomikonsekvens

Tydels maskinläsbara modell bör kunna uttrycka både evidensstatus och scope:

```text
Actor
→ Process
→ Transaction
→ Message
→ MessageVersion
→ SyntaxFormat / TransportProfile
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
- `valid_from` / `valid_to` när källa stödjer det
- `evidence_note`

Det förhindrar att en korrekt regel från FCR-processen oavsiktligt blir en global svensk Ediel-regel.

## Nästa researchsteg

Nästa steg är att få fram och editionsbestämma den fullständiga aktuella **UTILTS–APERAK-anvisningen** från Edielportalen och jämföra den med FCR-guidens exempel. Först därefter bör vi föreslå ett exakt första validator-kontrakt.
