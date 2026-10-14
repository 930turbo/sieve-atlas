"""Linear (Euler) sieve. Related algorithm: each composite marked once."""
import sys

def sieve(n: int) -> list[int]:
    if n < 2: return []
    least = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if least[i] == 0:
            least[i] = i
            primes.append(i)
        for p in primes:
            if p > least[i] or p > n // i: break
            least[p * i] = p
    return primes

if __name__ == '__main__':
    print(*sieve(int(sys.argv[1]) if len(sys.argv) > 1 else 100))
