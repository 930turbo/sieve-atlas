"""Render original, deterministic SVG artwork from actual prime classifications."""
import argparse
import html
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def prime(n):
    return n >= 2 and all(n % d for d in range(2,math.isqrt(n)+1))

def svg(width,height,body,label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(label)}">
<title>{html.escape(label)}</title>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101828"/><stop offset="1" stop-color="#090e19"/></linearGradient></defs>
<rect width="{width}" height="{height}" rx="24" fill="url(#bg)"/>
<g font-family="Segoe UI,Inter,Arial,sans-serif">{body}</g></svg>\n'''

def text(x,y,value,size=16,fill='#dce5f5',weight='400',extra=''):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" {extra}>{html.escape(str(value))}</text>'

def hero():
    entries=json.loads((ROOT/'implementations.json').read_text(encoding='utf-8'))
    count=len({e['language'] for e in entries})
    parts=[text(54,70,'THE PRIME NUMBER FIELD GUIDE',13,'#a9b8d0','600','letter-spacing="3"'),
           text(50,168,'SIEVE',88,'#f2f6ff','800','letter-spacing="-4"'),
           text(50,260,'ATLAS',88,'#80eed1','800','letter-spacing="-4"'),
           text(54,324,'One ancient algorithm.',25,'#eef3fd','500'),
           text(54,361,'A world of ways to write it.',25,'#a9b8d0'),
           '<path d="M54 405 H554" stroke="#26354b"/>',
           text(54,449,str(count),32,'#bbacff','700'),text(54,477,'LANGUAGES',11,'#a9b8d0','600','letter-spacing="2"'),
           text(232,449,str(len(entries)),32,'#bbacff','700'),text(232,477,'IMPLEMENTATIONS',11,'#a9b8d0','600','letter-spacing="2"'),
           text(442,449,'p²',32,'#bbacff','700'),text(442,477,'START HERE',11,'#a9b8d0','600','letter-spacing="2"'),
           text(54,548,'Mark the multiples. Keep the primes.',16,'#7f94b1')]
    for n in range(1,145):
        row,col=divmod(n-1,12)
        x,y=644+col*46,52+row*39
        is_prime=prime(n)
        fill='#153d3a' if is_prime else '#111c2d'
        border='#3e9c88' if is_prime else '#1b2a40'
        parts.append(f'<rect x="{x}" y="{y}" width="40" height="32" rx="7" fill="{fill}" stroke="{border}"/>')
        parts.append(text(x+20,y+21,n,12,'#9ff6dc' if is_prime else '#60748f','600' if is_prime else '400','text-anchor="middle"'))
    parts.extend(['<circle cx="650" cy="551" r="5" fill="#80eed1"/>',text(664,556,'Prime',13,'#a9b8d0'),'<circle cx="756" cy="551" r="5" fill="#3e506b"/>',text(770,556,'Composite / 1',13,'#a9b8d0'),text(1190,556,'1 — 144',13,'#7f94b1',extra='text-anchor="end"')])
    return svg(1250,600,''.join(parts),'Sieve Atlas: 30 languages, 36 implementations, with primes highlighted from 1 to 144')

def walkthrough():
    parts=[text(36,50,'THE SIEVE, IN FOUR PASSES',25,'#eef3fd','700'),text(36,82,'Cross off multiples from p². Stop once p² exceeds the limit.',16,'#a9b8d0')]
    colors={2:'#7fb6fa',3:'#bdabff',5:'#ffc588',7:'#f2a3bf'}
    for stage,p in enumerate([2,3,5,7]):
        x0=32+stage*272
        parts.extend([f'<rect x="{x0}" y="112" width="252" height="360" rx="16" fill="#111d2e" stroke="#26354b"/>',text(x0+20,150,f'p = {p}',25,colors[p],'700'),text(x0+20,178,f'Start at {p} × {p} = {p*p}',13,'#a9b8d0')])
        for n in range(1,50):
            row,col=divmod(n-1,7)
            x,y=x0+20+col*30,200+row*30
            factor=next((d for d in [2,3,5,7] if d<=p and n>=d*d and n%d==0),None)
            fill=colors[factor] if factor else '#80eed1' if prime(n) else '#dce5f5'
            if n==1: fill='#4b607b'
            parts.append(text(x+10,y+18,n,12,fill,'600','text-anchor="middle"'))
            if factor or n==1: parts.append(f'<path d="M{x+2} {y+9} l17 12" stroke="{fill}" stroke-opacity=".65"/>')
        parts.append(text(x0+20,447,'Multiples marked' if p<7 else '15 primes remain',13,'#a9b8d0'))
    parts.extend([text(36,515,'Why p²?',17,'#eef3fd','600'),text(155,515,'Smaller multiples already have a smaller prime factor.',16,'#a9b8d0'),text(36,549,'After 7: 2  3  5  7  11  13  17  19  23  29  31  37  41  43  47',16,'#80eed1')])
    return svg(1120,580,''.join(parts),'Four marking passes for primes up to 49: multiples of 2, 3, 5 and 7; 15 primes remain')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true')
    a=p.parse_args()
    for name,content in [('hero.svg',hero()),('sieve-walkthrough.svg',walkthrough())]:
        path=ROOT/'docs'/'images'/name
        if a.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content: raise SystemExit(f'Stale asset: {path}')
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8')
    print('Visual assets are current' if a.check else 'Rendered original SVG assets')

if __name__=='__main__': main()
