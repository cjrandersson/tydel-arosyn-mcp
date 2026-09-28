# Svensk Ediel-taxonomi

> **Status:** arbetsmodell under M0. Inga meddelanden eller regler räknas som verifierade enbart för att de finns i denna fil.

Det här dokumentet definierar hur Tydel ska kartlägga den svenska energimarknadens elektroniska informationsutbyte utan att blanda ihop affärsprocess, transport, meddelandeformat och valideringsregel.

## Målkedja

```text
Actor
  ↓
Process
  ↓
Transaction
  ↓
Message
  ↓
MessageVersion
  ↓
SyntaxFormat
  ↓
TransportProfile
  ↓
Rule
  ↓
Acknowledgement
  ↓
Error
  ↓
Resolution
```

Varje länk ska vara spårbar till en källa. Ett påstående utan tillräckligt källstöd markeras `UNVERIFIED` och får inte användas som validatorregel.

## Status för ett fynd

| Status | Betydelse |
|---|---|
| `CURRENT` | Verifierat som gällande inom den uttryckligen angivna processen/versionen |
| `CURRENT_SCOPED` | Verifierat som aktuellt inom ett snävare dokumenterat scope, exempelvis en viss FCR-integration; får inte generaliseras till hela svenska Ediel |
| `TRANSITIONAL` | Används under en dokumenterad övergång eller parallell migrering |
| `LEGACY` | Historiskt eller utfasat; får inte antas gälla idag |
| `UNVERIFIED` | Kandidat som ännu saknar tillräckligt auktoritativt källstöd |

Status gäller alltid en **bestämd process, marknad, version, scope och tidsperiod**. Ett message name är inte i sig `CURRENT` eller `LEGACY` globalt.

## Kärnobjekt

### Actor
En identifierbar marknadsroll eller systemroll som skickar, tar emot eller ansvarar för information. Vi skiljer roll från specifikt företag.

Minimifält: `actor_id`, `role_name`, `market`, `valid_from`, `valid_to`, `source_ref`.

### Process
Affärsprocessen som kommunikationen stödjer, exempelvis mätvärdeshantering eller en verifierad marknadsprocess. Processnamn hämtas från auktoritativ källa där det finns.

Minimifält: `process_id`, `name`, `purpose`, `actors[]`, `status`, `valid_from`, `valid_to`, `source_ref`.

### Transaction
Ett avgränsat steg mellan aktörer inom en process. Här dokumenteras riktning, trigger, förväntat svar och tidskrav när dessa är källbelagda.

### Message
Den logiska meddelandetypen, exempelvis ett EDIFACT message name eller motsvarande XML/CIM message. Message är separat från version och svensk profil.

### MessageVersion
Exakt standard/version/profile som används i transaktionen. Minimifält bör omfatta `message`, `directory_or_version`, `profile`, `status`, `valid_from`, `valid_to`, `source_ref`.

### SyntaxFormat
Den tekniska syntaxen/representationen, exempelvis EDIFACT, XML eller CIM-baserad representation. Den modelleras separat från affärsprocess och transport.

### TransportProfile
Hur meddelandet transporteras i ett verifierat scope, exempelvis SMTP, ECP/EDX, API eller annan specificerad kanal. Transport är inte samma sak som message format.

### Rule
En deterministiskt testbar constraint. Varje regel får ett stabilt Tydel-ID och ett lager: `BASE_STANDARD`, `SWEDISH_PROFILE`, `BUSINESS_PROCESS` eller `TYDEL_SAFETY`.

En regel får inte skapas från en LLM-sammanfattning utan att den bakomliggande källan kan pekas ut.

### Acknowledgement
Teknisk eller affärsmässig kvittens/svarsrelation. Vi dokumenterar separat om en acknowledgement endast visar teknisk mottagning eller även uttrycker affärsmässigt accept/reject.

### Error
Observerbart felutfall kopplat till rule, transaction eller transport. Feltext från ett system är evidence, inte automatiskt en standardregel.

### Resolution
Säkert nästa steg som följer av verifierad information. Tydel ska skilja på `verified_resolution`, `operator_check` och `unknown`.

## Källhierarki

För svenska marknads- och processregler prioriteras auktoritativa källor från relevanta marknadsinstitutioner och myndigheter, i första hand Svenska kraftnät, Energimarknadsinspektionen och eSett där respektive organisation faktiskt ansvarar för informationen.

Normativ profil-/Edielanvisning väger tyngre för validatorregler än ett guideexempel. En aktuell processguide kan ge stark scope-evidens, medan ett enskilt exempel inte ensamt gör ett segment obligatoriskt.

UN/EDIFACT/OpenEDI kan användas för generell struktur men ersätter inte svenska process- eller profilregler.

Varje källpost ska minst innehålla:

```yaml
source_id:
publisher:
title:
url:
document_version:
published_at:
valid_from:
valid_to:
retrieved_at:
checksum:
authority_scope:
evidence_level:
notes:
```

## Researchmatris

Matrisen visar **vad som faktiskt är verifierat på respektive lager**. `CURRENT` på processnivå betyder inte att message/profile automatiskt är verifierad.

| Process / scope | Transaction | Från | Till | Message | Version/profile | Ack/svar | Status | Källa |
|---|---|---|---|---|---|---|---|---|
| Mätvärdesrapportering | Rapportera mätvärden | Nätföretag | Elleverantör / BRP / Svenska kraftnät eller utsedd part beroende på transaction | `UNVERIFIED` | `UNVERIFIED` | Kvittenskrav inom 30 min är verifierat; teknisk ack-profile `UNVERIFIED` | Process/krav `CURRENT`; teknisk profil `UNVERIFIED` | [`matvarden.md`](matvarden.md) |
| Leverantörsbyte | Anmälan om övertagande/byte | Ny elleverantör | Nätföretag | `UNVERIFIED` | `UNVERIFIED` | Generellt kvittenskrav verifierat; teknisk ack-profile `UNVERIFIED` | Affärsrelation `CURRENT`; teknisk profil `UNVERIFIED` | [`leverantorsbyte.md`](leverantorsbyte.md) |
| Strukturdata | Ej kartlagd | ? | ? | ? | ? | ? | `UNVERIFIED` | Research ej genomförd |
| Balansavräkning | Underliggande rapporterings-/avräkningstransaktioner | BRP / relevanta marknadsroller | eSett / relevanta mottagare beroende på transaction | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` | Process/roller `CURRENT`; transactions/profiler `UNVERIFIED` | [`balansavrakning.md`](balansavrakning.md) |
| FCR / Fifty MMS | FCR-bud | BSP | Fifty MMS | `QUOTES` | Exakt ack/profile varierar; se researchunderlaget | APERAK förekommer i verifierat FCR-scope | `CURRENT_SCOPED` | [`utilts-aperak-current-evidence.md`](utilts-aperak-current-evidence.md) |
| FCR / Fifty MMS | FCR-planer | BSP | Fifty MMS | `DELFOR` | Exakt ack/profile varierar; se researchunderlaget | APERAK förekommer i verifierat FCR-scope | `CURRENT_SCOPED` | [`utilts-aperak-current-evidence.md`](utilts-aperak-current-evidence.md) |
| FCR / Fifty MMS | Accepted bids | Fifty MMS | BSP | `UTILTS S08` | Scope verifierat; exakt normativ edition ska fortfarande editionsbestämmas | APERAK relation verifierad inom FCR-scope | `CURRENT_SCOPED` | [`utilts-aperak-current-evidence.md`](utilts-aperak-current-evidence.md) |
| FCR / Fifty MMS | Activated energy | Fifty MMS | BSP | `UTILTS S01` | `D:02B:UN:E5SE9B` belagd i aktuell guideexempel; ännu inte uppgraderad till generell normativ profil | `APERAK D:04A:UN:E5SE9B` med `312/313` belagd i FCR-guide | `CURRENT_SCOPED` | [`utilts-aperak-current-evidence.md`](utilts-aperak-current-evidence.md) |

### Viktig avgränsning för FCR-raderna

`CURRENT_SCOPED` betyder här att relationen är verifierad inom Svenska kraftnäts FCR/Fifty MMS-guide. Guideexempel är **example/process-guide evidence**, inte automatiskt normativa regler för alla svenska UTILTS-/APERAK-flöden. Den aktuella fullständiga UTILTS–APERAK-anvisningen måste editionsbestämmas innan obligatoriska segment, qualifiers och kompletta kodlistor får bli validatorregler.

## Researchprotokoll

För varje process:

1. Hitta aktuell auktoritativ processbeskrivning.
2. Fastställ ansvariga aktörsroller.
3. Dela processen i transactions.
4. Identifiera message + exakt version/profile för varje transaction.
5. Identifiera syntaxformat och transportprofil separat.
6. Identifiera acknowledgement/reject-flöde separat från business message.
7. Dokumentera tidskrav endast när de kan citeras exakt.
8. Märk varje relation `CURRENT`, `CURRENT_SCOPED`, `TRANSITIONAL`, `LEGACY` eller `UNVERIFIED`.
9. Registrera evidensnivå så att guideexempel inte upphöjs till normativa regler.
10. Jämför mot äldre dokumentation för att undvika att historiska regler råkar presenteras som aktuella.
11. Först därefter får verifierbara constraints flyttas till ett framtida rule set.

## Definition of done för en process

En process är inte kartlagd förrän vi kan svara källbelagt på: vilka roller deltar, vad triggar varje transaction, vilket message/profile används, vilken riktning gäller, vilket syntaxformat och transportprofil som gäller, vilken acknowledgement/reject-relation finns, vilka tids-/versionsgränser gäller och vilken källa styr varje påstående.

En **verifierad processgrund** är därför inte samma sak som en färdig processmappning. Dokumenten för mätvärden, leverantörsbyte och balansavräkning har verifierad grund men fortfarande uttryckligen öppna message/profile-frågor.

Detta dokument är researchlagret. Validatorn ska senare konsumera kuraterade, versionsstyrda dataobjekt och regler, inte Markdown-tabellen direkt.
