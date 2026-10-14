"""Byte-array Eratosthenes. Inclusive upper bound; standard library only."""
from math import isqrt
import sys


def sieve(n: int) -> list[int]:
    if n < 2:
        return []
    composite = bytearray(n + 1)
    for p in range(2, isqrt(n) + 1):
        if not composite[p]:
            for multiple in range(p * p, n + 1, p):
                composite[multiple] = 1
    return [i for i in range(2, n + 1) if not composite[i]]


if __name__ == '__main__':
    print(*sieve(int(sys.argv[1]) if len(sys.argv) > 1 else 100))
