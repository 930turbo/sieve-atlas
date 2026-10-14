"""Segmented Eratosthenes: stream primes with a fixed-size marking window."""
from math import isqrt
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from implementations.python.sieve import sieve as base_sieve

def sieve(n: int, block_size: int = 32768):
    if block_size < 1: raise ValueError('block_size must be positive')
    if n < 2: return
    base = base_sieve(isqrt(n))
    for low in range(2, n + 1, block_size):
        high = min(n + 1, low + block_size)
        composite = bytearray(high - low)
        for p in base:
            start = max(p * p, ((low + p - 1) // p) * p)
            for m in range(start, high, p): composite[m - low] = 1
        for offset, marked in enumerate(composite):
            if not marked: yield low + offset

if __name__ == '__main__':
    print(*sieve(int(sys.argv[1]) if len(sys.argv) > 1 else 100))
