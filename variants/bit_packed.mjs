// Packed flags: one bit per candidate instead of one byte.
import { pathToFileURL } from 'node:url';
export function sieve(n) {
  if (n < 2) return [];
  const bits = new Uint8Array(Math.ceil((n + 1) / 8));
  const marked = i => (bits[i >> 3] & (1 << (i & 7))) !== 0;
  const mark = i => { bits[i >> 3] |= 1 << (i & 7); };
  for (let p = 2; p <= Math.floor(n / p); p++)
    if (!marked(p)) for (let m = p * p; m <= n; m += p) mark(m);
  const primes = [];
  for (let i = 2; i <= n; i++) if (!marked(i)) primes.push(i);
  return primes;
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href)
  console.log(sieve(Number(process.argv[2] ?? 100)).join(' '));
