// Compile with tsc --target ES2020 --module commonjs sieve.ts.
declare const process: { argv: string[] };
declare const require: { main: unknown };
declare const module: unknown;
export function sieve(n: number): number[] {
  if (n < 2) return [];
  const composite = new Uint8Array(n + 1);
  for (let p = 2; p <= Math.floor(n / p); p++) {
    if (composite[p]) continue;
    for (let m = p * p; m <= n; m += p) composite[m] = 1;
  }
  return Array.from({ length: n - 1 }, (_, i) => i + 2)
    .filter(i => composite[i] === 0);
}
if (require.main === module)
  console.log(sieve(Number(process.argv[2] ?? 100)).join(' '));
