# Algorithms and invariants

## Classic Eratosthenes

Keep one flag per integer from 0 through the inclusive bound `n`. Starting at `p = 2`, an unmarked `p` is prime. Mark `p*p, p*p+p, ...` as composite. Stop marking once `p > n / p`; this integer comparison avoids an overflowing `p*p` loop condition. Collect the unmarked integers from 2 through `n`.

**Why start at p²?** Every smaller multiple `k*p`, with `k < p`, has a prime factor smaller than `p` and has already been marked. Every composite `m <= n` has a prime factor at most `sqrt(m) <= sqrt(n)`, so the marking passes find every composite.

For a dense array and unit-cost integer operations, marking costs **O(n log log n)** time and **O(n)** flags. Output storage is additional: **O(pi(n))** integers. Bytes, Boolean objects, boxed references, and packed bits have very different constants. The immutable set examples illustrate the same marking invariant but their set operations add overhead; do not assign them the array implementation's constant factors or memory footprint.

The baseline files deliberately keep the same idea recognizable. Differences such as one-based indexing in R/Julia, ST mutation in Haskell, and explicit allocation in C show the host language's approach.

## Variant map

| Variant | What changes | Marking storage, excluding output | Tradeoff |
| --- | --- | --- | --- |
| [Odd-only](../variants/odd_only.py) | Store only odd candidates; handle 2 separately | About n/2 bytes | More index arithmetic; fewer candidates |
| [Bit-packed](../variants/bit_packed.mjs) | Eight flags per byte | About n/8 bytes | Shifts and masks for each access |
| [Segmented Python](../variants/segmented.py) / [C++](../variants/segmented.cpp) | Reuse a fixed-size marking window | O(sqrt(n) + B), with window width B | More setup per window; good locality |
| [Incremental](../variants/incremental.py) | Map each upcoming composite to prime steps | A sparse schedule, not a dense n-sized flag array | Dictionary/list overhead; collisions must preserve all steps |
| [Linear / Euler](../variants/linear.py) | Mark each composite once using its least prime factor | O(n) integer entries | Related sieve, not the same Eratosthenes loop |

### Odd-only indexing

Index `i` represents `2*i + 1`; index 0 is the number 1 and must be excluded. An odd prime's first mark is at `p*p//2`. Moving one index step corresponds to two integers, so advancing by `p` indexes marks odd multiples spaced `2*p` integers apart. Even upper bounds and the special case `n = 2` are easy places to make mistakes.

### Segmented windows

For `[low, high)`, the first multiple to mark for prime `p` is:

```text
max(p*p, ceil(low/p)*p)
```

The `p*p` term keeps a prime inside the window from marking itself. Base primes are generated up to `sqrt(n)`. Python yields primes lazily; C++ collects a vector, so their **total** memory use differs even though both use bounded marking windows. Very small windows also incur repeated base-prime scanning; the reference favors a clear implementation over aggressive tuning.

### Incremental scheduling

A new prime schedules its first composite at its square. When the scan reaches a scheduled composite, all prime steps at that key move forward. A single composite can have several prime factors, so overwriting a schedule collision loses information. The bounded implementation only schedules squares and future composites within `n`.

### Linear sieve

The least-prime-factor array ensures each composite `i*p` is visited only for `p <= least[i]`. That gives O(n) marking work in the usual unit-cost model. It can still lose to a compact Eratosthenes sieve because of integer storage and loop constants. Linear complexity alone is not a speed ranking.

## The Haskell origin

[SoEinH's original program](../historical/original-soe.hs) takes a prime from a list, then repeatedly applies `mod` to remove divisible candidates from the tail. It is an elegant demonstration of recursion, but it does not generate composite multiples by stepping through a marking structure.

The new [Haskell baseline](../implementations/haskell/sieve.hs) uses a mutable unboxed Boolean array inside `ST`, then exposes a pure `Int -> [Int]` interface. The algorithm changes without making the public function impure.

Melissa E. O'Neill explains this distinction and functional composite scheduling in [The Genuine Sieve of Eratosthenes](https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf). The paper also derives the classic marking complexity. These implementations are written for this atlas; the paper is a conceptual reference, not a source copied into the repository.

## Scope and numeric limits

The shared tested domain is integer limits from -7 through 10,000, plus additional seeded cases. Python variants also check known counts through 100,000. The runner caps requested runs at 1,000,000 to keep experiments modest; this is not a promise that every runtime uses little memory at that size.

Standalone examples assume an integer representable in their native type, with enough memory for flags and output. They do not share malformed-input handling and do not attempt arbitrary-precision indexing, cryptographic prime generation, or integer-overflow hardening near native integer maxima. Reuse the core function with validation appropriate to your application.
