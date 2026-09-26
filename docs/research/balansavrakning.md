# Balansavräkning i Sverige

> Status: **VERIFIERAD PROCESSGRUND / MEDDELANDEPROFILER EJ VERIFIERADE**  
> Senast granskad: 2026-09-26

Detta dokument beskriver endast sådant som kan stödjas av aktuella auktoritativa källor. Det är underlag för Tydels taxonomi, inte en implementeringsspecifikation.

## Verifierad processgrund

**Balansavräkning** är bestämning och fördelning av skillnaden mellan inköpt/producerad och såld/levererad elenergi samt ekonomisk reglering av denna energi. Energimarknadsinspektionens EIFS 2025:1 anger att avräkningen för balansansvariga utförs av Svenska kraftnät eller den som Svenska kraftnät har utsett i sitt ställe.

I den nuvarande nordiska modellen är **eSett Oy** Imbalance Settlement Responsible (ISR) och utför balansavräkning samt fakturering av BRP:er för obalanser på uppdrag av de fyra TSO:erna Energinet, Fingrid, Statnett och Svenska kraftnät.

Svenska kraftnät beskriver 2026 balansansvarig part som en aktiv marknadsroll och anger att eSett utför balansavräkningen för Sverige, Norge, Finland och Danmark. Under 2026 pågår dessutom implementationsarbete kring uppdelningen av rollerna **BSP** (leverantör av balanstjänster) och **BRP** (balansansvarig part). Detta ska behandlas som aktuell marknadsförändring och inte blandas ihop med historiska rollmodeller.

## Taxonomisk modell

| Lager | Verifierat innehåll | Status |
| --- | --- | --- |
| Actor | Svenska kraftnät (TSO) | CURRENT |
| Actor | eSett Oy (ISR) | CURRENT |
| Actor | BRP / balansansvarig part | CURRENT |
| Actor | BSP / leverantör av balanstjänster | CURRENT, rollimplementation under utveckling 2026 |
| Process | Balansavräkning | CURRENT |
| Transaction | Underliggande rapporterings-/avräkningstransaktioner | UNVERIFIED |
| Message | Exakta Ediel-/XML-meddelanden | UNVERIFIED |
| MessageVersion | Exakt profil/version/edition | UNVERIFIED |
| Rule | Process- och rollregler enligt aktuella regelverk | PARTIAL |
| Acknowledgement | Exakt teknisk kvittensprofil | UNVERIFIED |
| Error | Kodverk/felmodell per meddelande | UNVERIFIED |
| Resolution | Operativ åtgärd per verifierad regel/felkod | UNVERIFIED |

## Viktig editionsgräns

EIFS 2025:1 trädde i kraft **1 juni 2025** och ersatte EIFS 2023:1. Ei anger uttryckligen att äldre föreskrifter fortfarande gäller för rapportering av mätvärden som avser tid före 1 juni 2025. Tydels framtida regelmotor får därför inte välja regelverk enbart efter mottagningsdatum; relevant leverans-/mätperiod kan påverka vilken edition som gäller.

Detta är ett konkret exempel på varför taxonomin behöver `MessageVersion`/edition och tidsdimension som förstaklassdata.

## Vad vi inte påstår ännu

Följande ska **inte** betraktas som verifierat av detta dokument:

- vilket tekniskt meddelande som används för varje balansavräkningstransaktion i Sverige i dag;
- om en viss EDIFACT-, XML- eller annan profil är `CURRENT`, `TRANSITIONAL` eller `LEGACY`;
- segment, qualifiers, obligatoriska fält eller kodlistor;
- exakt acknowledgement-/felmeddelande och dess versionsberoende regler.

Dessa uppgifter måste hämtas från aktuell Svenska kraftnät/eSett-specifikation eller annan auktoritativ implementationsanvisning innan de får bli validatorregler.

## Källor

1. Energimarknadsinspektionen, **EIFS 2025:1 – föreskrifter och allmänna råd om mätning och rapportering av överförd el**. Definitioner av balansansvarig och balansavräkning samt editionsgräns från 1 juni 2025. https://ei.se/om-oss/publikationer/publikationer/foreskrifter-el/2025/foreskrift-eifs-20251
2. eSett Open Data, **Main**. eSett beskriver sin roll som Imbalance Settlement Responsible och ansvar för imbalance settlement/invoicing för BRP på uppdrag av de fyra nordiska TSO:erna. https://opendata.esett.com/
3. Svenska kraftnät, **Avgifter och kostnader – balansansvarig part**. Bekräftar aktuell BRP-kontext och att eSett utför balansavräkning för Sverige, Norge, Finland och Danmark. https://www.svk.se/aktorsportalen/balansansvarig-part/avgifter-och-kostnader/
4. Svenska kraftnät, **Nytt datum för aktörsmöte om införande av aktörsrollerna BSP och BRP**, 2026-09-07. Aktuell status för implementationsarbetet kring BSP/BRP. https://www.svk.se/press-och-nyheter/nyheter/balansansvar/2026/nytt-datum-for-aktorsmote-om-inforande-av-aktorsrollerna-bsp-och-brp/
