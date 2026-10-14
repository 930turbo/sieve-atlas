# Immutable MapSet trades compact storage for a functional marking style.
defmodule PrimeSieve do
  def sieve(n) when n < 2, do: []
  def sieve(n) do
    composite = mark(2, n, MapSet.new())
    Enum.reject(2..n, &MapSet.member?(composite, &1))
  end
  defp mark(p, n, composite) when p * p > n, do: composite
  defp mark(p, n, composite) do
    next = if MapSet.member?(composite, p), do: composite,
      else: cross(p * p, p, n, composite)
    mark(p + 1, n, next)
  end
  defp cross(m, _p, n, composite) when m > n, do: composite
  defp cross(m, p, n, composite), do: cross(m + p, p, n, MapSet.put(composite, m))
end
n = case System.argv() do [] -> 100; [first | _] -> String.to_integer(first) end
IO.puts(Enum.join(PrimeSieve.sieve(n), " "))
