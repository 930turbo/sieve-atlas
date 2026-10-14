"""Incremental Eratosthenes: schedule the next composite of each prime."""
import sys

def sieve(n: int):
    schedule: dict[int, list[int]] = {}
    for candidate in range(2, n + 1):
        steps = schedule.pop(candidate, None)
        if steps is None:
            yield candidate
            if candidate <= n // candidate:
                schedule.setdefault(candidate * candidate, []).append(candidate)
        else:
            for step in steps:
                following = candidate + step
                if following <= n: schedule.setdefault(following, []).append(step)

if __name__ == '__main__':
    print(*sieve(int(sys.argv[1]) if len(sys.argv) > 1 else 100))
