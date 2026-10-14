# Language catalog

One baseline per language, then six additional variants. Paths link directly to the source. All commands below are run from the repository root using Python 3.10+. The runner invokes the real language toolchain, not a translation.

## Baselines

| Language | Source | Runtime / compiler | Storage | Run |
| --- | --- | --- | --- | --- |
| Python | [sieve.py](../implementations/python/sieve.py) | Python 3.10+ | Byte array | `python tools/atlas.py run python 100` |
| JavaScript | [sieve.mjs](../implementations/javascript/sieve.mjs) | Node.js 18+ | Typed byte array | `python tools/atlas.py run javascript 100` |
| TypeScript | [sieve.ts](../implementations/typescript/sieve.ts) | TypeScript 5+ + Node.js 18+ | Typed byte array | `python tools/atlas.py run typescript 100` |
| Haskell | [sieve.hs](../implementations/haskell/sieve.hs) | GHC 9+ (array bundled) | ST unboxed array | `python tools/atlas.py run haskell 100` |
| C | [sieve.c](../implementations/c/sieve.c) | GCC / C11 | Byte array | `python tools/atlas.py run c 100` |
| C++ | [sieve.cpp](../implementations/cpp/sieve.cpp) | G++ / C++17 | Byte vector | `python tools/atlas.py run cpp 100` |
| C# | [Sieve.cs](../implementations/csharp/Sieve.cs) | Mono C# compiler + runtime | Boolean array | `python tools/atlas.py run csharp 100` |
| Java | [Sieve.java](../implementations/java/Sieve.java) | JDK 17+ | Boolean array | `python tools/atlas.py run java 100` |
| Go | [sieve.go](../implementations/go/sieve.go) | Go 1.20+ | Boolean slice | `python tools/atlas.py run go 100` |
| Rust | [sieve.rs](../implementations/rust/sieve.rs) | Rust 2021 edition | Boolean vector | `python tools/atlas.py run rust 100` |
| Ruby | [sieve.rb](../implementations/ruby/sieve.rb) | Ruby 3+ | Array | `python tools/atlas.py run ruby 100` |
| PHP | [sieve.php](../implementations/php/sieve.php) | PHP 8+ | Array | `python tools/atlas.py run php 100` |
| Perl | [sieve.pl](../implementations/perl/sieve.pl) | Perl 5 | Array | `python tools/atlas.py run perl 100` |
| Lua | [sieve.lua](../implementations/lua/sieve.lua) | Lua 5.3+ | Sparse table | `python tools/atlas.py run lua 100` |
| R | [sieve.R](../implementations/r/sieve.R) | R 4+ | Logical vector | `python tools/atlas.py run r 100` |
| Julia | [sieve.jl](../implementations/julia/sieve.jl) | Julia 1.10+ | Packed BitVector | `python tools/atlas.py run julia 100` |
| Swift | [sieve.swift](../implementations/swift/sieve.swift) | Swift 5+ | Boolean array | `python tools/atlas.py run swift 100` |
| Kotlin | [Sieve.kt](../implementations/kotlin/Sieve.kt) | Kotlin + JDK 17 | BooleanArray | `python tools/atlas.py run kotlin 100` |
| Scala | [Sieve.scala](../implementations/scala/Sieve.scala) | Scala 2.11+ + JDK | Boolean array | `python tools/atlas.py run scala 100` |
| Elixir | [sieve.exs](../implementations/elixir/sieve.exs) | Elixir 1.12+ / OTP | Immutable MapSet | `python tools/atlas.py run elixir 100` |
| Erlang | [sieve.erl](../implementations/erlang/sieve.erl) | Erlang/OTP 24+ | Immutable set | `python tools/atlas.py run erlang 100` |
| OCaml | [sieve.ml](../implementations/ocaml/sieve.ml) | OCaml 4.08+ | Boolean array | `python tools/atlas.py run ocaml 100` |
| F# | [sieve.fsx](../implementations/fsharp/sieve.fsx) | .NET SDK 8+ | Boolean array | `python tools/atlas.py run fsharp 100` |
| Dart | [sieve.dart](../implementations/dart/sieve.dart) | Dart 3+ | Typed byte array | `python tools/atlas.py run dart 100` |
| Nim | [sieve.nim](../implementations/nim/sieve.nim) | Nim 1.6+ | Boolean sequence | `python tools/atlas.py run nim 100` |
| Crystal | [sieve.cr](../implementations/crystal/sieve.cr) | Crystal 1+ | Boolean array | `python tools/atlas.py run crystal 100` |
| Fortran | [sieve.f90](../implementations/fortran/sieve.f90) | GFortran / Fortran 2008 | Logical array | `python tools/atlas.py run fortran 100` |
| Pascal | [sieve.pas](../implementations/pascal/sieve.pas) | Free Pascal 3+ | Dynamic array | `python tools/atlas.py run pascal 100` |
| Bash | [sieve.sh](../implementations/bash/sieve.sh) | Bash 4+ | Indexed array | `python tools/atlas.py run bash 100` |
| PowerShell | [sieve.ps1](../implementations/powershell/sieve.ps1) | PowerShell 7+ | Boolean array | `python tools/atlas.py run powershell 100` |

## Variants

| ID | Language | Approach | Source |
| --- | --- | --- | --- |
| `python-odd` | Python | odd-only | [odd_only.py](../variants/odd_only.py) |
| `python-segmented` | Python | segmented | [segmented.py](../variants/segmented.py) |
| `python-incremental` | Python | incremental | [incremental.py](../variants/incremental.py) |
| `python-linear` | Python | linear (Euler) | [linear.py](../variants/linear.py) |
| `javascript-bits` | JavaScript | bit-packed | [bit_packed.mjs](../variants/bit_packed.mjs) |
| `cpp-segmented` | C++ | segmented | [segmented.cpp](../variants/segmented.cpp) |

Run a variant the same way, for example `python tools/atlas.py run python-segmented 1000`.

## Use a file directly

```sh
python implementations/python/sieve.py 100
node implementations/javascript/sieve.mjs 100
runghc implementations/haskell/sieve.hs 100
gcc -std=c11 -O2 implementations/c/sieve.c -o sieve && ./sieve 100
g++ -std=c++17 -O2 implementations/cpp/sieve.cpp -o sieve && ./sieve 100
pwsh -NoProfile -File implementations/powershell/sieve.ps1 -Limit 100
```

Build commands for every compiled entry live in [implementations.json](../implementations.json). Commands use GCC, G++, Mono, and other specific toolchain names; Windows users need the corresponding tools on PATH. The runner writes compiled output into `.build/<id>/`. OCaml may also create ignored `.cmi`/`.cmo` files beside the source.

For reuse, copy the sieve function and its imports/types into your project. Python, JavaScript, TypeScript, Ruby, PHP, Perl, Lua, R, Julia, Nim, Bash, and PowerShell guard their command-line entry points. In the other standalone programs, remove the small main/driver section or adapt it into a module. C and C++ support `SIEVE_ATLAS_NO_MAIN`. This is a source reference library, not 30 separately packaged ecosystem libraries.

Generated by `python tools/generate_docs.py`; edit the manifest to change this catalog.
