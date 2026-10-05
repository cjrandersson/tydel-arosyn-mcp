# Tydel

**Tydel** (från fornsvenskans *þyþa* – *”att göra något begripligt för folket”*) är ett utvecklarcentrerat **Conformance & CI/CD Layer** för energimarknadens migrering till det centrala Datahanteringsverktyget (DHV) och IEC CIM (Common Information Model).

Tydel flyttar valideringen av komplexa marknadsprocesser och nätkoder hela vägen till vänster ("Shift-Left"). Istället för att integrationskonsulter och mjukvaruleverantörer testar asynkront mot externa hubb-sandlådor, validerar Tydel CIM-meddelanden (JSON/XML) lokalt på under 10 millisekunder – direkt i utvecklarens IDE eller som en automatiserad kvalitetsgrind i CI/CD-pipelinen.

[![Validator First](https://shields.io)](ARCHITECTURE.md)
[![CIM Compliant](https://shields.io)]()
[![CI/CD Ready](https://shields.io)]()

## ⚡ Varför Tydel?

Energimarknaden genomgår sin största transformation i modern tid. Övergången till DHV och CIM innebär att hundratals mjukvarusystem och integrationsflöden måste byggas om från grunden. 

En generisk JSON- eller XML-schema-validator kan verifiera att syntaxen är korrekt. Men den kan inte avgöra om meddelandet följer de sekventiella affärsreglerna för ett leverantörsbyte, en balansavräkning eller en mätvärdesrapportering enligt de nordiska tillämpningsprofilerna. 

Tydel löser detta genom **marknadsprocessmedveten diagnostik**. Verktyget talar om exakt vilken affärsregel som brutits, vilken rad eller JSON-path det gäller, samt ger ett säkert nästa felsökningssteg för utvecklaren.

---

## 🧭 DEVELOPMENT COCKPIT

Detta är källan för projektets aktuella läge. Statusen här speglar `project-status.yml`.

### Aktuellt läge
* **Nuvarande milestone:** M0 — Research foundation & första CIM/DHV-validator-scope
* **Status:** 🟡 PÅGÅR
* **Nuvarande mål:** Låsa en smal, auktoritativ och testbar svensk CIM-profil (t.ex. mätvärden/metering) och förbereda kunddiscovery mot integrationskonsulter.
* **Exakt nästa tekniska uppgift:** Extrahera normativa affärsregler för den valda CIM-profilen från Ei:s och Svenska kraftnäts DHV-specifikationer.
* **Nästa owner:** ChatGPT

### Resursallokering & Ansvar
* **@cjrandersson:** Strategisk styrning och uppsättning av GitHub Actions-arkitektur. Status: ⚪ CLEAR.
* **ChatGPT:** Ansvarig för att bryta ner normativa CIM-regler, bygga upp fixture-strukturer samt Customer Discovery-underlag. Status: 🟢 ACTIVE.
* **Codex:** Väntar på implementation av produktionskod till dess att första validator-kontraktet är låst. Status: ⏸ WAITING.
* **@gonzalolorcakeabit-bit:** Ansvarig för oberoende peer-review via Claude-briefen. Status: 🟡 READY.

---

## 🏗 Kärnkomponenter i skiktet

1. **Tydel Engine (Deterministic Validator):** En blixtsnabb kompilerad motor som utvärderar inkommande eller utgående nyttolaster (payloads) mot maskinläsbara regelset (CIM-profiler).
2. **Tydel CLI & CI/CD Gate:** Ett utvecklarverktyg som kan köras lokalt i terminalen eller sömlöst integreras i GitHub Actions, GitLab CI eller iCore/Mulesoft-pipelines för att blockera felaktiga byggen.
3. **MCP Assistant Layer:** Ett Model Context Protocol-gränssnitt som låter AI-kodassistenter (Copilot, Cursor) konsumera Tydels valideringsmotor och referensmaterial live under kodning.

## 🛡 Säkerhet & Arkitekturprinciper

* **Validator First:** Parsern och de deterministiska reglerna är systemets "Source of Truth". AI-modeller används aldrig för att avgöra om ett meddelande är giltigt eller inte.
* **Immutable Provenance:** Varje validering mot en specifik profilversion genererar ett kryptografiskt och audit-klart kvitto som kan användas som efterlevnadsbevis (Compliance Evidence).
* **Zero Trust Ingestion:** Tydel hanterar enbart meddelandestruktur och affärslogik. Ingen känslig produktionsdata eller personuppgifter (GDPR) ska lagras eller skickas externt.

## 🚀 Komma igång

*(Implementation påbörjas i Milestone 1)*

```bash
# Validera en CIM-nyttolast lokalt mot DHV-profilen för mätvärden
tydel validate --profile se-dhv-metering-v1 ./fixtures/metering_payload.json
```

## 📄 Disclaimer
Tydel är ett oberoende research- och utvecklingsprojekt. Det är inte anslutet till, godkänt av eller certifierat av Svenska kraftnäts DHV-projekt, Energimarknadsinspektionen (Ei), eSett eller någon annan officiell marknadsaktör.
