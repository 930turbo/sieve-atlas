"""Build/run/verify entries from implementations.json without shell execution."""
import argparse
import json
import math
import os
from pathlib import Path
import random
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'implementations.json').read_text(encoding='utf-8'))
CASES = [-7, 0, 1, 2, 3, 4, 9, 25, 49, 97, 100, 1000, 10000]
ENV = dict(os.environ, DOTNET_NOLOGO='1', DOTNET_CLI_TELEMETRY_OPTOUT='1',
           DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1')


def reference(n):
    """Independent trial-division oracle for correctness, not the implementation."""
    return [i for i in range(2, n + 1) if all(i % d for d in range(2, math.isqrt(i) + 1))]


def entry_for(name):
    return next((e for e in MANIFEST if e['id'] == name), None)


def command(entry, field):
    build = ROOT / '.build' / entry['id']
    values = dict(source=str(ROOT / entry['path']), build=str(build))
    result = [part.format(**values) for part in entry[field]]
    if result[0] == 'python': result[0] = sys.executable
    if os.name == 'nt' and str(build) in result[0] and not result[0].endswith('.exe'):
        result[0] += '.exe'
    return result


def missing(entry):
    executables = []
    if entry['build']: executables.append(command(entry, 'build')[0])
    run = command(entry, 'run')[0]
    if not str(ROOT / '.build') in run: executables.append(run)
    return [exe for exe in executables if not shutil.which(exe)]


def invoke(args, timeout=120):
    result = subprocess.run(args, cwd=ROOT, env=ENV, encoding='utf-8', errors='replace',
                            capture_output=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {args!r}\n{result.stdout}\n{result.stderr}")
    return result.stdout


def prepare(entry):
    (ROOT / '.build' / entry['id']).mkdir(parents=True, exist_ok=True)
    if entry['build']: invoke(command(entry, 'build'), timeout=300)


def output(entry, n=None):
    args = command(entry, 'run') + ([] if n is None else ([entry['limit_flag']] if entry.get('limit_flag') else []) + [str(n)])
    raw = invoke(args, timeout=60).strip()
    if raw and not re.fullmatch(r'\d+(?:\s+\d+)*', raw):
        raise ValueError(f"Non-protocol output: {raw[:300]!r}")
    return [int(word) for word in raw.split()]


def verify(entries, required=False):
    failed, passed, skipped = 0, 0, 0
    expected = {n: reference(n) for n in CASES}
    rng = random.Random(2026)
    extras = [rng.randrange(2, 3000) for _ in range(4)]
    expected.update({n: reference(n) for n in extras})
    for entry in entries:
        absent = missing(entry)
        if absent:
            print(f"{'FAIL' if required else 'SKIP'} {entry['id']}: missing {', '.join(absent)}")
            failed += int(required)
            skipped += int(not required)
            continue
        try:
            prepare(entry)
            for n, primes in expected.items():
                actual = output(entry, n)
                if actual != primes:
                    raise ValueError(f'n={n}: expected {primes[:20]} ({len(primes)} total), got {actual[:20]} ({len(actual)} total)')
            if output(entry) != expected[100]: raise ValueError('Default limit must be 100')
            print(f"PASS {entry['id']}: {len(expected) + 1} cases")
            passed += 1
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
            print(f"FAIL {entry['id']}: {error}")
            failed += 1
    print(f'\n{passed} passed / {failed} failed / {skipped} skipped')
    return 1 if failed or not passed else 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='action', required=True)
    sub.add_parser('list', help='Show implementations and runtime availability')
    run = sub.add_parser('run')
    run.add_argument('id')
    run.add_argument('limit', type=int, nargs='?', default=100)
    test = sub.add_parser('test')
    test.add_argument('ids', nargs='*', help='Default: every entry; unavailable runtimes are skipped')
    test.add_argument('--require', action='store_true', help='Fail instead of skipping a missing runtime')
    args = p.parse_args(argv)
    if args.action == 'list':
        for e in MANIFEST:
            print(f"{e['id']:22} {e['language']:12} {e['variant']:15} {'missing: ' + ', '.join(missing(e)) if missing(e) else 'available'}")
        return 0
    ids = args.ids if args.action == 'test' else [args.id]
    entries = [entry_for(name) for name in ids] if ids else MANIFEST
    if any(e is None for e in entries): p.error('Unknown ID; run `list` to see available IDs')
    if args.action == 'test': return verify(entries, args.require)
    if args.limit > 1_000_000: p.error('Runner safety limit is 1,000,000; call the source directly for larger experiments')
    entry = entries[0]
    if missing(entry): p.error('Missing runtime/compiler: ' + ', '.join(missing(entry)))
    try:
        prepare(entry)
        print(*output(entry, args.limit))
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        p.exit(1, f'error: {error}\n')
    return 0


if __name__ == '__main__': raise SystemExit(main())
