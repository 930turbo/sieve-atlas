def sieve(n : Int32) : Array(Int32)
  return [] of Int32 if n < 2
  composite = Array(Bool).new(n + 1, false)
  p = 2
  while p <= n // p
    unless composite[p]
      m = p * p
      while m <= n
        composite[m] = true
        m += p
      end
    end
    p += 1
  end
  (2..n).reject { |i| composite[i] }.to_a
end
puts sieve(ARGV.empty? ? 100 : ARGV[0].to_i).join(" ")
