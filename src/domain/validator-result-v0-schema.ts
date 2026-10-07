import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import {
  Ajv2020,
  type AnySchema,
  type ErrorObject,
  type ValidateFunction,
} from "ajv/dist/2020.js";
import formatsPlugin, { type FormatsPlugin } from "ajv-formats";

import type { ValidatorResultV0 } from "./validator-result-v0.js";

const schemaPath = fileURLToPath(
  new URL("../../schemas/validator-result-v0.schema.json", import.meta.url),
);
const schema = JSON.parse(readFileSync(schemaPath, "utf8")) as AnySchema;

const ajv = new Ajv2020({
  allErrors: true,
  strict: true,
  // The locked schema applies array keywords in conditional property subschemas;
  // their array type is declared on the root property.
  strictTypes: false,
});
const addFormats = formatsPlugin as unknown as FormatsPlugin;
addFormats(ajv);
const validateSchema: ValidateFunction = ajv.compile(schema);

function describeError(error: ErrorObject): string {
  const path = error.instancePath || "/";
  if (error.keyword === "required") {
    const missingProperty = (error.params as { missingProperty?: string }).missingProperty;
    return `${path}: must have required property '${missingProperty ?? "unknown"}'`;
  }
  return `${path}: ${error.message ?? error.keyword}`;
}

export class ValidatorResultContractError extends Error {
  readonly issues: readonly string[];

  constructor(issues: readonly string[]) {
    super(`Validator Result v0 contract violation: ${issues.join("; ")}`);
    this.name = "ValidatorResultContractError";
    this.issues = issues;
  }
}

export function validateValidatorResult(value: unknown): ValidatorResultV0 {
  if (!validateSchema(value)) {
    const issues = (validateSchema.errors ?? []).map(describeError);
    throw new ValidatorResultContractError(issues);
  }
  return value as ValidatorResultV0;
}

export function isValidatorResult(value: unknown): value is ValidatorResultV0 {
  return validateSchema(value);
}
