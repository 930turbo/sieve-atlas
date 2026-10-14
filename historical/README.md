# The original SoEinH

[original-soe.hs](original-soe.hs) preserves the original program unchanged. It reads a limit from an interactive prompt and prints a Haskell list of primes. Run with `runghc historical/original-soe.hs` and enter a number.

Its recursive filter chain is a historical/educational example, not a current baseline or a benchmark target. The current Haskell baseline uses genuine composite marking in an ST array. See [the algorithm notes](../docs/ALGORITHMS.md#the-haskell-origin) for the distinction.

This folder is intentionally excluded from the uniform command-line protocol and language test matrix. The original commits remain in repository history.
