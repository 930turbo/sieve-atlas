"""Odd candidates only: index i represents 2*i+1. O(n log log n)."""
from math import isqrt
import sys

def sieve(n: int) -> list[int]:
    if n < 2: return []
    composite = bytearray((n + 1) // 2)
    composite[0] = 1  # 1 is not prime.
    for p in range(3, isqrt(n) + 1, 2):
        if not composite[p // 2]:
            for m in range(p * p // 2, len(composite), p):
                composite[m] = 1
    return [2] + [2*i + 1 for i in range(1, len(composite)) if not composite[i]]

if __name__ == '__main__':
    print(*sieve(int(sys.argv[1]) if len(sys.argv) > 1 else 100))
