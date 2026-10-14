-- Sparse table: absent entries are not marked composite.
local function sieve(n)
    local composite, primes = {}, {}
    if n < 2 then return primes end
    local p = 2
    while p <= math.floor(n / p) do
        if not composite[p] then
            for m = p * p, n, p do composite[m] = true end
        end
        p = p + 1
    end
    for i = 2, n do
        if not composite[i] then primes[#primes + 1] = i end
    end
    return primes
end
if ... ~= 'sieve' then
    print(table.concat(sieve(tonumber(arg[1]) or 100), ' '))
end
return sieve
