<?php
// PHP arrays are hash tables: readable, but larger than packed byte arrays.
function sieve(int $n): array {
    if ($n < 2) return [];
    $composite = array_fill(0, $n + 1, false);
    for ($p = 2; $p <= intdiv($n, $p); $p++)
        if (!$composite[$p])
            for ($m = $p * $p; $m <= $n; $m += $p) $composite[$m] = true;
    $primes = [];
    for ($i = 2; $i <= $n; $i++) if (!$composite[$i]) $primes[] = $i;
    return $primes;
}
if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__)
    echo implode(' ', sieve(isset($argv[1]) ? (int)$argv[1] : 100)), PHP_EOL;
