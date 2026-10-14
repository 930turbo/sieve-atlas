def sieve(n)
  return [] if n < 2
  composite = Array.new(n + 1, false)
  p = 2
  while p <= n / p
    (p * p).step(n, p) { |m| composite[m] = true } unless composite[p]
    p += 1
  end
  (2..n).reject { |i| composite[i] }
end
puts sieve(ARGV.empty? ? 100 : Integer(ARGV[0])).join(' ') if $PROGRAM_NAME == __FILE__
