import importlib.util
import json
import math
from pathlib import Path
import random
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from implementations.python.sieve import sieve
from variants.odd_only import sieve as odd
from variants.segmented import sieve as segmented
from variants.incremental import sieve as incremental
from variants.linear import sieve as linear


def oracle(n):
    return [i for i in range(2,n+1) if all(i%d for d in range(2,math.isqrt(i)+1))]


class SieveTests(unittest.TestCase):
    def test_boundaries_and_random(self):
        rng=random.Random(42)
        for n in [-10,0,1,2,3,4,9,25,49,97,100,1000]+[rng.randrange(3000) for _ in range(40)]:
            expected=oracle(n)
            for function in [sieve,odd,segmented,incremental,linear]:
                with self.subTest(n=n,variant=function.__module__):
                    self.assertEqual(list(function(n)),expected)

    def test_known_prime_counts(self):
        for n,count in [(10,4),(100,25),(1000,168),(10000,1229),(100000,9592)]:
            for function in [sieve,odd,segmented,incremental,linear]:
                self.assertEqual(len(list(function(n))),count)

    def test_segment_boundaries(self):
        for size in [1,2,3,7,32,49,1000]:
            self.assertEqual(list(segmented(300,size)),oracle(300))
        with self.assertRaises(ValueError): list(segmented(10,0))

    def test_manifest(self):
        entries=json.loads((ROOT/'implementations.json').read_text(encoding='utf-8'))
        self.assertEqual(len(entries),36)
        self.assertEqual(len({e['language'] for e in entries}),30)
        self.assertEqual(len({e['id'] for e in entries}),len(entries))
        for entry in entries:
            self.assertTrue((ROOT/entry['path']).is_file(),entry['path'])
            self.assertTrue(entry['run'])
        registered={e['path'] for e in entries}
        for folder in ['implementations','variants']:
            for path in (ROOT/folder).rglob('*'):
                if path.suffix in {'.py','.mjs','.ts','.hs','.c','.cpp','.cs','.java','.go','.rs','.rb','.php','.pl','.lua','.R','.jl','.swift','.kt','.scala','.exs','.erl','.ml','.fsx','.dart','.nim','.cr','.f90','.pas','.sh','.ps1'}:
                    self.assertIn(path.relative_to(ROOT).as_posix(),registered)

    def test_visual_assets(self):
        for file in (ROOT/'docs'/'images').glob('*.svg'):
            ET.parse(file)


if __name__ == '__main__': unittest.main()
