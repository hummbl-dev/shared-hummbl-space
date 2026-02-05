import { execSync } from 'child_process';

export function runCommand(cmd: string) {
  console.log(`Executing: ${cmd}`);
  execSync(cmd, { stdio: 'inherit' });
}
