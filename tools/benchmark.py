"""A small, honest process-level benchmark; not a language speed leaderboard."""
import argparse
import json
import platform
import statistics
import time
from pathlib import Path
from atlas import entry_for, missing, output, prepare, reference


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('ids', nargs='+')
    p.add_argument('--limit', type=int, default=100000)
    p.add_argument('--repeat', type=int, default=3)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    if not 0 <= a.limit <= 1_000_000 or not 1 <= a.repeat <= 20:
        p.error('Use limit 0..1000000 and repeat 1..20')
    results=[]
    for name in a.ids:
        entry=entry_for(name)
        if entry is None: p.error(f'Unknown ID: {name}')
        if missing(entry): p.error(f'{name}: missing runtime/compiler')
        prepare(entry)  # Build time is excluded.
        expected=reference(a.limit)
        if output(entry,a.limit) != expected: raise RuntimeError(f'{name}: incorrect result')
        samples=[]
        for _ in range(a.repeat):
            start=time.perf_counter()
            actual=output(entry,a.limit)
            elapsed=time.perf_counter()-start
            if actual != expected: raise RuntimeError(f'{name}: incorrect result')
            samples.append(elapsed)
        results.append(dict(id=name,limit=a.limit,primes=len(expected),median_seconds=statistics.median(samples),samples=samples))
    report=dict(platform=platform.platform(),measurement='process startup + algorithm + stdout + parsing; one untimed warmup; compilation excluded',results=results)
    text=json.dumps(report,indent=2)
    print(text)
    if a.output: a.output.write_text(text+'\n',encoding='utf-8')

if __name__ == '__main__': main()
