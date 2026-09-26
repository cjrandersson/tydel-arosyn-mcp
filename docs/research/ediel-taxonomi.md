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
| `CURRENT` | Verifierat som gällande i aktuell process/version |
| `TRANSITIONAL` | Används under en dokumenterad övergång eller parallell migrering |
| `LEGACY` | Historiskt eller utfasat; får inte antas gälla idag |
| `UNVERIFIED` | Kandidat som ännu saknar tillräckligt auktoritativt källstöd |

Status gäller alltid en **bestämd process, marknad, version och tidsperiod**. Ett message name är inte i sig `CURRENT` eller `LEGACY` globalt.

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
Exakt standard/version/profile som används i transaktionen. Minimifält bör omfatta `message`, `syntax_or_format`, `directory_or_version`, `profile`, `status`, `valid_from`, `valid_to`, `source_ref`.

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
notes:
```

## Researchmatris

Den här matrisen fylls endast med verifierade fynd. Frågetecken är avsiktliga.

| Process | Transaction | Från | Till | Message | Version/profile | Ack/svar | Status | Källa |
|---|---|---|---|---|---|---|---|---|
| Mätvärdeshantering | ? | ? | ? | Kandidater undersöks | ? | ? | `UNVERIFIED` | Se reading guide |
| Leverantörsrelaterade processer | ? | ? | ? | ? | ? | ? | `UNVERIFIED` | Research pending |
| Strukturdata | ? | ? | ? | ? | ? | ? | `UNVERIFIED` | Research pending |
| Avräkning | ? | ? | ? | ? | ? | ? | `UNVERIFIED` | Research pending |
| Balans/reserver | ? | ? | ? | ? | ? | ? | `UNVERIFIED` | Research pending |

## Researchprotokoll

För varje process:

1. Hitta aktuell auktoritativ processbeskrivning.
2. Fastställ ansvariga aktörsroller.
3. Dela processen i transactions.
4. Identifiera message + exakt version/profile för varje transaction.
5. Identifiera acknowledgement/reject-flöde separat från business message.
6. Dokumentera tidskrav endast när de kan citeras exakt.
7. Märk varje relation `CURRENT`, `TRANSITIONAL`, `LEGACY` eller `UNVERIFIED`.
8. Jämför mot äldre dokumentation för att undvika att historiska regler råkar presenteras som aktuella.
9. Först därefter får verifierbara constraints flyttas till ett framtida rule set.

## Definition of done för en process

En process är inte kartlagd förrän vi kan svara källbelagt på: vilka roller deltar, vad triggar varje transaction, vilket message/profile används, vilken riktning gäller, vilken acknowledgement/reject-relation finns, vilka tids-/versionsgränser gäller och vilken källa styr varje påstående.

Detta dokument är researchlagret. Validatorn ska senare konsumera kuraterade, versionsstyrda dataobjekt och regler, inte Markdown-tabellen direkt.
