import { verifyMigrations } from './migration-verifier';

export async function executeRollback(planFile: string) {
  console.log(`Executing rollback plan ${planFile} (stub).`);
  await verifyMigrations('db');
  console.log('Rollback complete (stub).');
}
