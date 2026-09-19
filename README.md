# Tydel: MCP-Driven Grid Data Monitoring & Ingestion Framework
An intelligent, Model Context Protocol (MCP) powered operational middleware platform engineered specifically for regional Swedish Distribution System Operators (DSOs) and Balance Responsible Parties (BRPs) in the Mälardalen region (SE3 Bidding Zone).

Tydel continuously parses legacy **Ediel (EDIFACT)** messaging streams, tracks operational errors, forecasts grid load capacities, and translates technical data infrastructure bottlenecks into natural language actionable alerts.

---

## 🏗️ Platform Core Architecture

Tydel bridges the structural gap between legacy electrical utility communications and modern automated agentic workflows using a layered microservice blueprint:

```
                  ┌──────────────────────────────────────────────┐
                  │               TYDEL CORE ENGINE              │
                  │  (EDIFACT Parser, MCP Agent, Forecast Engine) │
                  └───────▲──────────────────────────────▲───────┘
                          │                              │
     PHASE 1: Passive     │                              │   PHASE 2: Active
     Log Ingestion        │                              │   Inline Routing
                          │                              │
    ┌─────────────────────┴──────┐                ┌──────┴─────────────────────┐
    │ CLIENT'S EXIST. EDI ROUTER │                │       CENTRAL EDIEL /      │
    │ (e.g., eBuilder / BizTalk) │                │    eSETT MARKET PLATFORM   │
    └──────────────▲─────────────┘                └──────────────▲─────────────┘
                   │                                             │
                   │ (Copies files via SFTP)                     │ (Direct AS2 / HTTPS)
                   │                                             │
    ┌──────────────┴─────────────┐                               │
    │    Smart Meters / Grid     │───────────────────────────────┘
    └────────────────────────────┘
```

### 🔓 The Ingestion Strategy
* **Passive Log Ingestion (Low Friction):** Integrates via automated `SFTP` text outbox dumps without disrupting operational inline environments. 
* **Inline Communications Gateway (Active Loop):** Intercepts live data pipelines as an active routing layer using `AS2 / HTTPS` transport frameworks, allowing automated runtime transaction error self-healing.

---

## ⚙️ MCP Server Logic & Step-by-Step Translation Blueprint

The Model Context Protocol (MCP) server acts as a standardized interface mapping underlying code validation anomalies into natural language suggestions over a secure JSON-RPC interface.

```
[ Raw Inbound MSCONS File ] ──► [ 1. Parsing Engine ] ──► [ 2. Context Packager ]
                                                                   │
                                                                   ▼
[ 5. Frontend Dashboard UI ] ◄── [ 4. LLM Inference ] ◄── [ 3. MCP Server Payload ]
```

1. **Raw Error Extraction (Parser):** The TypeScript pipeline encounters anomalies within an incoming file stream (e.g., a non-numeric value in a data segment):
   ```text
   LOC+172+735999102030405061'
   DTM+241:PT15M:806'
   QTY+131:NULL'  <-- CRASH: System encounters string instead of expected numeric value
   ```
2. **Context Packaging:** The extraction loop links structural error parameters to operational grid definitions:
   ```json
   {
     "errorCode": "EDI_VALUE_TYPE_MISMATCH",
     "segment": "QTY",
     "meta": {
       "meteringPointId": "735999102030405061",
       "affectedUtility": "Upplands Energi",
       "marketPartner": "eSett",
       "imbalanceRiskZone": "SE3"
     }
    }
   ```
3. **MCP Tool Formatting:** Exposes standardized resources compliant with the `@modelcontextprotocol/sdk`:
   ```typescript
   import { CallToolResult } from "@modelcontextprotocol/sdk";
   
   export async function handleGetEdiErrorContext(messageId: string): Promise<CallToolResult> {
     const errorData = await db.fetchErrorLog(messageId);
     return {
       content: [{
         type: "text",
         text: `CONTEXT ENVIRONMENT: Swedish DSO operational error.\nRaw Segment: ${errorData.rawString}\nMetering Point: ${errorData.meta.meteringPointId}`
       }]
     };
   }
   ```
4. **LLM Inference Processing:** Uses internal systemic templates to translate the error context into a structured, plain-language action sequence.
5. **UI Rendering:** Renders contextual actions directly into the frontend command center sidebar.

---

## 🇸🇪 Swedish Infrastructure Compliance & Hosting

To operate inside critical national infrastructure under Sweden's **Säkerhetsskyddslagen** and the EU **NIS2 directive**, Tydel isolates data from non-EU legal jurisdictions (negating US Cloud Act exposure).

* **Sovereign Cloud Layer:** Deployed within secure, local Swedish hosting nodes (such as **Safespring**, **Cleura**, or **Elastx**).
* **Multi-Tenant BYOC Model:** Features a *Bring Your Own Certificate* cryptography structure. Private keys and X.509 certificates required by the *Svenska kraftnät Ediel Agreement* remain isolated in individual encrypted environments.

---

## 💻 TypeScript Implementation Blueprint

### Core Domain Layout Types (`types/grid.ts`)
```typescript
export type MessageType = 'MSCONS' | 'PRODAT' | 'DELFOR' | 'APERAK';
export type PipelineStatus = 'healthy' | 'warning' | 'critical';

export interface EdiErrorPayload {
  messageId: string;
  type: MessageType;
  origin: string;
  timestamp: string;
  status: PipelineStatus;
  segmentErrorLocation?: string;
  plainEnglishSummary: string;
  rawPayloadUrl: string;
}
```

### PDF Ingestion & Automation Engine (`scripts/ingest-ediel-handbook.ts`)
```typescript
import * as fs from 'fs';
import * as path from 'path';
import pdf from 'pdf-parse';

interface ExtractedSection {
  segmentCode: string;
  markdownContext: string;
}

export async function convertEdielPdfToMarkdown(pdfPath: string): Promise<ExtractedSection[]> {
  const dataBuffer = fs.readFileSync(pdfPath);
  const parsedPdf = await pdf(dataBuffer);
  const fullText = parsedPdf.text;
  
  const segmentDelimiter = /(Segment:\s+[A-Z]{3})/g;
  const rawChunks = fullText.split(segmentDelimiter);
  const formattedSections: ExtractedSection[] = [];

  rawChunks.forEach((chunk, index) => {
    formattedSections.push({
      segmentCode: `EDIEL_SEGMENT_${index}`,
      markdownContext: `### Ediel Specification Rule\n\n\`\`\`\n${chunk.trim()}\n\`\`\``
    });
  });

  return formattedSections;
}
```

---

## 🛠️ Getting Started & Local Development

### 1. Prerequisites
Ensure you have the following frameworks configured locally within your sovereign deployment container:
* Node.js v18+ 
* TypeScript v5+

### 2. Installation
```bash
npm install @modelcontextprotocol/sdk pdf-parse
npm install --save-dev typescript @types/node
```

### 3. Build the Context Core
To run the documentation parsing pipeline and initialize the localized context databases:
```bash
npx ts-node scripts/ingest-ediel-handbook.ts
```
