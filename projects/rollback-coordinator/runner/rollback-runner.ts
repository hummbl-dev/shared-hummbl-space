import { runCommand } from '../scripts/utils';

export async function executeRollback(planFile: string) {
  console.log(`Executing rollback plan ${planFile} (stub).`);
  // TODO: parse plan, call governance, run scripts sequentially
}
