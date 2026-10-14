# Contributing

Add one clear idea at a time: a new language, a materially different representation, an explanation, or a correctness fix. Short, readable source is the point; avoid adding framework dependencies to a sieve example.

1. Put a baseline in `implementations/<language>/`; put an alternate algorithm or representation in `variants/`.
2. Expose a named reusable function. Keep the small CLI driver separate or guarded when the language permits.
3. Accept an inclusive integer upper bound as the first CLI argument, default to 100, and print ascending primes separated by whitespace. Below 2, print an empty line. No prompts or debug output on stdout.
4. Mark actual composite multiples beginning at `p*p`. Label related algorithms such as Euler's linear sieve explicitly; do not call a recursive divisibility filter an optimized Eratosthenes sieve.
5. Register source, toolchain, build/run argument arrays, storage, and variant in `implementations.json`. Add its CI runtime setup and a required verification command. Do not silently skip a new language in CI.
6. Run the oracle checks, regenerate the catalog/artwork, and update the README index/counts and the manifest count expectations in tests.

```sh
python tools/atlas.py test YOUR_ID --require
python -m unittest discover -s tests -v
python tools/generate_docs.py
python tools/render_assets.py
```

Explain the invariant and the storage tradeoff for a new variant. Include edge cases around prime squares and storage/window boundaries. For a speed claim, give the runtime version, hardware, bound, flags, repeat count, and exactly what was timed. Avoid universal language rankings.
