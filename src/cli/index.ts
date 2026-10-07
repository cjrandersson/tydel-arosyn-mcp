#!/usr/bin/env node
import { runValidatorResultCli } from "./validator-result.js";

process.exitCode = await runValidatorResultCli(process.argv.slice(2));
