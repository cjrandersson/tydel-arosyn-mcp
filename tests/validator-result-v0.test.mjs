import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import test from "node:test";

import {
  ValidatorResultContractError,
  exitCodeForValidatorResult,
  isValidatorResult,
  runValidatorResultCli,
  serializeValidatorResult,
  validateValidatorResult,
} from "../build/index.js";

const root = resolve(import.meta.dirname, "..");
const passPath = resolve(root, "fixtures/m1/validator-result/pass.json");
const failPath = resolve(root, "fixtures/m1/validator-result/fail-aperak-313.json");
const passText = readFileSync(passPath, "utf8");
const failText = readFileSync(failPath, "utf8");
const passFixture = JSON.parse(passText);
const failFixture = JSON.parse(failText);

function clone(value) {
  return structuredClone(value);
}

function reverseObjectKeys(value) {
  if (Array.isArray(value)) {
    return value.map(reverseObjectKeys);
  }
  if (value !== null && typeof value === "object") {
    return Object.fromEntries(
      Object.entries(value)
        .reverse()
        .map(([key, nested]) => [key, reverseObjectKeys(nested)]),
    );
  }
  return value;
}

function cliIo({ stdin = "", readFile = (path) => readFileSync(path, "utf8") } = {}) {
  const output = { stdout: "", stderr: "" };
  return {
    output,
    io: {
      readFile: async (path) => readFile(path),
      readStdin: async () => stdin,
      writeStdout: (value) => {
        output.stdout += value;
      },
      writeStderr: (value) => {
        output.stderr += value;
      },
    },
  };
}

test("committed PASS and FAIL fixtures satisfy Validator Result v0", () => {
  assert.equal(validateValidatorResult(passFixture).status, "PASS");
  assert.equal(validateValidatorResult(failFixture).status, "FAIL");
  assert.equal(isValidatorResult(passFixture), true);
  assert.equal(isValidatorResult(failFixture), true);
});

test("PASS must not contain an ERROR but may contain a WARNING", () => {
  const invalid = clone(passFixture);
  invalid.error = clone(failFixture.error);
  assert.throws(() => validateValidatorResult(invalid), ValidatorResultContractError);

  const withWarning = clone(passFixture);
  const warning = clone(failFixture.error[0]);
  warning.severity = "WARNING";
  withWarning.error = [warning];
  assert.equal(validateValidatorResult(withWarning).status, "PASS");
});

test("FAIL requires at least one ERROR", () => {
  const empty = clone(failFixture);
  empty.error = [];
  assert.throws(() => validateValidatorResult(empty), ValidatorResultContractError);

  const warningOnly = clone(failFixture);
  warningOnly.error[0].severity = "WARNING";
  assert.throws(() => validateValidatorResult(warningOnly), ValidatorResultContractError);
});

test("JSON Schema rejects incompatible versions, invalid dates, and extra fields", () => {
  const wrongVersion = clone(passFixture);
  wrongVersion.schemaVersion = "tydel.validator-result/v1";
  assert.throws(() => validateValidatorResult(wrongVersion), ValidatorResultContractError);

  const invalidDate = clone(passFixture);
  invalidDate.context.asOf = "2026-02-30";
  assert.throws(() => validateValidatorResult(invalidDate), ValidatorResultContractError);

  const extraField = clone(passFixture);
  extraField.unlocked = true;
  assert.throws(() => validateValidatorResult(extraField), ValidatorResultContractError);
});

test("golden serialization is byte-for-byte stable for both fixtures", () => {
  assert.equal(serializeValidatorResult(passFixture), passText);
  assert.equal(serializeValidatorResult(failFixture), failText);
  assert.equal(serializeValidatorResult(reverseObjectKeys(passFixture)), passText);
  assert.equal(serializeValidatorResult(reverseObjectKeys(failFixture)), failText);
});

test("FAIL serialization preserves locations, values, provenance, response, and safe next step", () => {
  const roundTrip = JSON.parse(serializeValidatorResult(failFixture));
  const finding = roundTrip.error[0];
  assert.equal(finding.segmentPath, "UNB[1]/UNH[1]/BGM[1]");
  assert.equal(finding.canonicalPath, "acknowledgement.status");
  assert.equal(finding.observed, "313");
  assert.match(finding.expected, /^312 /);
  assert.deepEqual(finding.provenance, failFixture.error[0].provenance);
  assert.deepEqual(finding.originalResponse, failFixture.error[0].originalResponse);
  assert.equal(finding.nextStep, failFixture.error[0].nextStep);
});

test("exit mapping is PASS=0 and FAIL=1", () => {
  assert.equal(exitCodeForValidatorResult(passFixture), 0);
  assert.equal(exitCodeForValidatorResult(failFixture), 1);
});

test("CLI emits deterministic JSON and maps PASS/FAIL to 0/1", async () => {
  const passRun = cliIo();
  assert.equal(await runValidatorResultCli([passPath], passRun.io), 0);
  assert.equal(passRun.output.stderr, "");
  assert.equal(passRun.output.stdout, passText);

  const failRun = cliIo();
  assert.equal(await runValidatorResultCli([failPath], failRun.io), 1);
  assert.equal(failRun.output.stderr, "");
  assert.equal(failRun.output.stdout, failText);
});

test("CLI maps malformed JSON, contract failure, and runtime failure to 2", async () => {
  const malformed = cliIo({ stdin: "{" });
  assert.equal(await runValidatorResultCli(["-"], malformed.io), 2);
  assert.match(malformed.output.stderr, /contract failure: invalid JSON/);

  const invalidContract = cliIo({
    stdin: JSON.stringify({ ...passFixture, schemaVersion: "wrong" }),
  });
  assert.equal(await runValidatorResultCli(["-"], invalidContract.io), 2);
  assert.match(invalidContract.output.stderr, /contract failure/);

  const runtimeFailure = cliIo({
    readFile: () => {
      throw new Error("fixture read failed");
    },
  });
  assert.equal(await runValidatorResultCli(["unreadable.json"], runtimeFailure.io), 2);
  assert.match(runtimeFailure.output.stderr, /runtime failure: fixture read failed/);
});
