export const VALIDATOR_RESULT_SCHEMA_VERSION = "tydel.validator-result/v0" as const;

export type ValidatorResultStatus = "PASS" | "FAIL";
export type ValidatorResultSeverity = "ERROR" | "WARNING";
export type RuleLayer =
  | "BASE_STANDARD"
  | "MARKET_PROFILE"
  | "BUSINESS_PROCESS"
  | "TYDEL_SAFETY";
export type EvidenceLevel = "NORMATIVE" | "PROCESS_GUIDE" | "EXAMPLE" | "SECONDARY";

export interface ValidatorResultContext {
  jurisdiction: string;
  process: string;
  message: string;
  profile: string;
  messageVersion: string;
  syntax: string;
  asOf: string;
}

export interface ValidatorResultRulePack {
  id: string;
  version: string;
  contentHash?: string | null;
}

export interface ValidatorResultProvenance {
  sourceId: string;
  publisher: string;
  title: string;
  edition: string;
  section: string;
  evidenceLevel: EvidenceLevel;
  effectiveFrom: string | null;
  effectiveTo: string | null;
  sourceChecksum?: string | null;
}

export interface ValidatorResultOriginalResponse {
  type: string;
  code: string;
  messageReference?: string | null;
  transactionReference?: string | null;
}

export interface ValidatorResultFinding {
  ruleId: string;
  severity: ValidatorResultSeverity;
  ruleLayer: RuleLayer;
  segmentPath: string;
  canonicalPath: string;
  observed: string;
  expected: string;
  provenance: readonly ValidatorResultProvenance[];
  originalResponse?: ValidatorResultOriginalResponse | null;
  nextStep: string;
}

export interface ValidatorResultExecution {
  engineVersion: string;
  mode: "LOCAL";
  offline: true;
  durationMs: number;
}

export interface ValidatorResultV0 {
  schemaVersion: typeof VALIDATOR_RESULT_SCHEMA_VERSION;
  resultId: string;
  status: ValidatorResultStatus;
  context: ValidatorResultContext;
  rulePack: ValidatorResultRulePack;
  error: readonly ValidatorResultFinding[];
  execution: ValidatorResultExecution;
}
