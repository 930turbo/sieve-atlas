// A byte per candidate; no dependencies. Import { sieve } for reuse.
import { pathToFileURL } from 'node:url';
export function sieve(n) {
  if (n < 2) return [];
  const composite = new Uint8Array(n + 1);
  for (let p = 2; p <= Math.floor(n / p); p++) {
    if (composite[p]) continue;
    for (let m = p * p; m <= n; m += p) composite[m] = 1;
  }
  const primes = [];
  for (let i = 2; i <= n; i++) if (!composite[i]) primes.push(i);
  return primes;
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href)
  console.log(sieve(Number(process.argv[2] ?? 100)).join(' '));
