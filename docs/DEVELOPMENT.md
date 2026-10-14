# Development

## Run the atlas

Python 3.10+ drives the optional tools. Each implementation needs its own compiler/interpreter on PATH; the runner never installs software or downloads packages.

```sh
python tools/atlas.py list
python tools/atlas.py run python 100
python tools/atlas.py run cpp-segmented 10000
python tools/atlas.py test
python tools/atlas.py test python javascript --require
python -m unittest discover -s tests -v
```

`list` reports missing executables. `run` builds a compiled entry into `.build/<id>/` before running it; no cached executable can hide a source change. With no IDs, `test` attempts the entire manifest and reports unavailable toolchains as **SKIP**. `--require` turns missing tools into failures, as used in CI. A test run with no passing entries exits nonzero. IDs are listed in [the catalog](LANGUAGES.md).

Build/run commands are argument arrays in [implementations.json](../implementations.json). The harness uses `subprocess` without `shell=True`, enforces build/run timeouts, and rejects any stdout that is not a whitespace-separated list of nonnegative integers. Negative inputs must produce no primes. PowerShell receives negative bounds through the named `-Limit` argument to avoid script parameter ambiguity.

The common protocol applies to integer inputs; malformed arguments and native exceptions are intentionally outside the cross-language contract. Direct runs default to 100. The runner rejects limits above 1,000,000; individual source files leave resource/overflow validation to callers.

## Verification

The harness compares full ordered prime lists with independent trial division for 17 explicit/seeded limits and checks the no-argument default separately. Cases include -7, 0, 1, 2, 3, 4, 9, 25, 49, 97, 100, 1,000, 10,000 and four reproducible random limits. It catches missing endpoints, composite squares, duplicates, wrong ordering, and accidental prompts.

Python unit tests exercise all five Python implementations against an oracle over 52 limits, known prime counts up to 100,000, and segmented block sizes including 1. Manifest tests ensure source registration stays complete. Documentation and artwork generators have `--check` modes for CI.

GitHub Actions covers all 30 languages and all 36 entries in eight jobs: core, four compiler/interpreter groups, Julia, Dart, and Swift. Most jobs use Ubuntu 24.04; Swift uses macOS. CI installs external toolchains, but implementations themselves use standard libraries only. This is correctness CI, not exhaustive verification across every platform/version of every language. Check the workflow badge for the current result.

## Benchmarks

```sh
python tools/benchmark.py python python-odd python-segmented --limit 100000 --repeat 3
python tools/benchmark.py javascript javascript-bits --limit 100000 --output benchmark-results.json
```

The benchmark builds first, verifies the result, takes one untimed warmup, then reports all samples and their median. It measures **process startup + algorithm + stdout serialization + capture/parsing**, excluding compilation. It records the host platform and prime count. It is useful for local experiments, not a language speed leaderboard: runtime startup, JIT behavior, output volume, toolchain versions, hardware, and flags all affect results. Compare variants in the same runtime, and record runtime versions when sharing numbers.

## Generated files

```sh
python tools/generate_docs.py
python tools/render_assets.py
python tools/generate_docs.py --check
python tools/render_assets.py --check
```

The catalog is generated from the manifest. The original SVG artwork is generated from actual prime classifications with the Python standard library; no external image assets or font downloads are needed. Update the manifest before regenerating the catalog. README links and counts should be updated when the collection grows.

## Repository layout

```text
implementations/        One readable baseline per language
variants/               Six alternate implementations, clearly classified
historical/             Original SoEinH source and context
tools/                  Runner, benchmark, docs and artwork generators
tests/                  Oracle, invariant and manifest tests
docs/                   Language catalog, algorithms, development, SVG artwork
implementations.json    Executable registry: source, run/build commands, metadata
```

The original root `soe.hs` has moved to `historical/original-soe.hs`; the current Haskell program is under `implementations/haskell/sieve.hs`. Git history is retained. This repository is a source reference library, not an installable package with a common cross-language ABI.
