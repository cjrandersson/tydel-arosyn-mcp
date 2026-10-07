import type {
  ValidatorResultFinding,
  ValidatorResultOriginalResponse,
  ValidatorResultProvenance,
  ValidatorResultV0,
} from "./validator-result-v0.js";
import { validateValidatorResult } from "./validator-result-v0-schema.js";

function normalizeProvenance(provenance: ValidatorResultProvenance): Record<string, unknown> {
  const normalized: Record<string, unknown> = {
    sourceId: provenance.sourceId,
    publisher: provenance.publisher,
    title: provenance.title,
    edition: provenance.edition,
    section: provenance.section,
    evidenceLevel: provenance.evidenceLevel,
    effectiveFrom: provenance.effectiveFrom,
    effectiveTo: provenance.effectiveTo,
  };
  if (provenance.sourceChecksum !== undefined) {
    normalized.sourceChecksum = provenance.sourceChecksum;
  }
  return normalized;
}

function normalizeOriginalResponse(
  response: ValidatorResultOriginalResponse,
): Record<string, unknown> {
  const normalized: Record<string, unknown> = {
    type: response.type,
    code: response.code,
  };
  if (response.messageReference !== undefined) {
    normalized.messageReference = response.messageReference;
  }
  if (response.transactionReference !== undefined) {
    normalized.transactionReference = response.transactionReference;
  }
  return normalized;
}

function normalizeFinding(finding: ValidatorResultFinding): Record<string, unknown> {
  const normalized: Record<string, unknown> = {
    ruleId: finding.ruleId,
    severity: finding.severity,
    ruleLayer: finding.ruleLayer,
    segmentPath: finding.segmentPath,
    canonicalPath: finding.canonicalPath,
    observed: finding.observed,
    expected: finding.expected,
    provenance: finding.provenance.map(normalizeProvenance),
  };
  if (finding.originalResponse !== undefined) {
    normalized.originalResponse =
      finding.originalResponse === null
        ? null
        : normalizeOriginalResponse(finding.originalResponse);
  }
  normalized.nextStep = finding.nextStep;
  return normalized;
}

function normalizeResult(result: ValidatorResultV0): Record<string, unknown> {
  const rulePack: Record<string, unknown> = {
    id: result.rulePack.id,
    version: result.rulePack.version,
  };
  if (result.rulePack.contentHash !== undefined) {
    rulePack.contentHash = result.rulePack.contentHash;
  }

  return {
    schemaVersion: result.schemaVersion,
    resultId: result.resultId,
    status: result.status,
    context: {
      jurisdiction: result.context.jurisdiction,
      process: result.context.process,
      message: result.context.message,
      profile: result.context.profile,
      messageVersion: result.context.messageVersion,
      syntax: result.context.syntax,
      asOf: result.context.asOf,
    },
    rulePack,
    error: result.error.map(normalizeFinding),
    execution: {
      engineVersion: result.execution.engineVersion,
      mode: result.execution.mode,
      offline: result.execution.offline,
      durationMs: result.execution.durationMs,
    },
  };
}

export function serializeValidatorResult(value: unknown): string {
  const result = validateValidatorResult(value);
  return `${JSON.stringify(normalizeResult(result), null, 2)}\n`;
}
