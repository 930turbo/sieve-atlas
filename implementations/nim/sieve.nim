import std/[os, strutils]
proc sieve*(n: int): seq[int] =
  if n < 2: return @[]
  var composite = newSeq[bool](n + 1)
  var p = 2
  while p <= n div p:
    if not composite[p]:
      var m = p * p
      while m <= n:
        composite[m] = true
        m += p
    inc p
  for i in 2..n:
    if not composite[i]: result.add(i)
when isMainModule:
  let n = if paramCount() > 0: parseInt(paramStr(1)) else: 100
  var words: seq[string]
  for p in sieve(n): words.add($p)
  echo words.join(" ")
