import { readFile } from "node:fs/promises";

import type { ValidatorResultV0 } from "../domain/validator-result-v0.js";
import {
  ValidatorResultContractError,
  validateValidatorResult,
} from "../domain/validator-result-v0-schema.js";
import { serializeValidatorResult } from "../domain/validator-result-v0-serializer.js";

export const VALIDATOR_RESULT_EXIT = {
  PASS: 0,
  FAIL: 1,
  FAILURE: 2,
} as const;

export type ValidatorResultExitCode = 0 | 1 | 2;

export interface ValidatorResultCliIo {
  readFile(path: string): Promise<string>;
  readStdin(): Promise<string>;
  writeStdout(value: string): void;
  writeStderr(value: string): void;
}

export function exitCodeForValidatorResult(value: unknown): 0 | 1 {
  const result = validateValidatorResult(value);
  return result.status === "PASS" ? VALIDATOR_RESULT_EXIT.PASS : VALIDATOR_RESULT_EXIT.FAIL;
}

async function readStdin(): Promise<string> {
  const chunks: Buffer[] = [];
  for await (const chunk of process.stdin) {
    chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
  }
  return Buffer.concat(chunks).toString("utf8");
}

const processIo: ValidatorResultCliIo = {
  readFile: (path) => readFile(path, "utf8"),
  readStdin,
  writeStdout: (value) => process.stdout.write(value),
  writeStderr: (value) => process.stderr.write(value),
};

function failureMessage(error: unknown): string {
  if (error instanceof ValidatorResultContractError) {
    return `Validator Result v0 contract failure: ${error.issues.join("; ")}`;
  }
  if (error instanceof SyntaxError) {
    return `Validator Result v0 contract failure: invalid JSON (${error.message})`;
  }
  const detail = error instanceof Error ? error.message : String(error);
  return `Validator Result v0 runtime failure: ${detail}`;
}

export async function runValidatorResultCli(
  args: readonly string[],
  io: ValidatorResultCliIo = processIo,
): Promise<ValidatorResultExitCode> {
  try {
    if (args.length !== 1) {
      throw new Error("usage: tydel-validator-result <result.json|->");
    }

    const input = args[0] === "-" ? await io.readStdin() : await io.readFile(args[0]);
    const parsed: unknown = JSON.parse(input);
    const result: ValidatorResultV0 = validateValidatorResult(parsed);
    io.writeStdout(serializeValidatorResult(result));
    return exitCodeForValidatorResult(result);
  } catch (error) {
    io.writeStderr(`${failureMessage(error)}\n`);
    return VALIDATOR_RESULT_EXIT.FAILURE;
  }
}
