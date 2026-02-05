#!/usr/bin/env ts-node
import { executeRollback } from '../runner/rollback-runner';

const [,, cmd, arg] = process.argv;

async function main() {
  if (!cmd) {
    console.error('Usage: rollback-coordinator <plan-file>');
    process.exit(1);
  }
  await executeRollback(cmd);
}

main();
