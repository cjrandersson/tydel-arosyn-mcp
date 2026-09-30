# UTILTS candidate fixtures

Det här katalogträdet innehåller användarlevererade, verklighetstrogna kandidat-fixtures för Tydels UTILTS-validator.

## Viktigt

- Filerna är **inte ännu verifierade mot den normativa svenska Ediel-profilen** och får därför inte användas som auktoritativa standardexempel.
- Filnamnen beskriver avsedd testintention (`pos` / `neg`), inte ett redan bevisat validatorutfall.
- Råfilerna bevaras oförändrade så att vi kan skilja källmaterial från senare korrigerade eller härledda fixtures.
- Innan en kandidat flyttas till ett verifierat regressionstest ska relevant source edition, profile, expected result och rule IDs vara dokumenterade.
- Inga uppenbara credentials, personnamn eller hemligheter hittades vid intake-kontrollen 2026-09-30. Identifierarna ser syntetiska ut men ska fortsatt behandlas som testdata, inte som verkliga marknadsaktörer.

## Intake-observationer

En lättviktig strukturell kontroll visar att kandidatpaketet inte ännu motsvarar alla beskrivningar ordagrant:

- `utilts_pos_rev3_15min_clean.edi` innehåller 2 `QTY`/`DTM+67`-intervall, inte 96.
- `utilts_pos_rev3_hourly_clean.edi` och `utilts_pos_rev4_15min_clean.edi` har deklarerade `UNT`-segmentantal som inte matchar det observerade antalet segment mellan `UNH` och `UNT`.
- Flera negativa kandidater har också ett `UNT`-count mismatch utöver det fel som filnamnet avser att testa.
- `utilts_neg_missing_intervals.edi` innehåller 1 observerat mätintervall, inte 94.
- ZIP-paketet innehöll även `utilts_neg_missing_bgm_code.edi` och `utilts_neg_missing_dtm_137.edi`, utöver de fall som först listades.

Detta är inte ett skäl att kasta materialet. Tvärtom är det användbart som rå kandidatdata, men vi ska inte kalla ett fall `VALID` förrän validatorn och den normativa källan stödjer det.

Se `manifest.yml` för intake-status och SHA-256 för varje råfil.
