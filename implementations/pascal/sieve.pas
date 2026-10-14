program PrimeSieve;
{$mode objfpc}
uses SysUtils;
type TIntArray = array of LongInt;
function Sieve(n: LongInt): TIntArray;
var composite: array of Boolean; p, m, i, count: LongInt;
begin
  SetLength(Result, 0);
  if n < 2 then Exit;
  SetLength(composite, n + 1);
  p := 2;
  while p <= n div p do begin
    if not composite[p] then begin
      m := p * p;
      while m <= n do begin composite[m] := True; m := m + p end;
    end;
    p := p + 1;
  end;
  SetLength(Result, n + 1);
  count := 0;
  for i := 2 to n do
    if not composite[i] then begin Result[count] := i; count := count + 1 end;
  SetLength(Result, count);
end;
var n, i: LongInt; primes: TIntArray;
begin
  n := 100;
  if ParamCount > 0 then n := StrToInt(ParamStr(1));
  primes := Sieve(n);
  for i := 0 to Length(primes) - 1 do Write(primes[i], ' ');
  WriteLn;
end.
