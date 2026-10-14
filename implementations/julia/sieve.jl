# Candidate i lives at index i + 1; BitVector packs flags into bits.
function sieve(n::Int)
    n < 2 && return Int[]
    composite = falses(n + 1)
    p = 2
    while p <= n ÷ p
        if !composite[p + 1]
            for m in p*p:p:n
                composite[m + 1] = true
            end
        end
        p += 1
    end
    return [i for i in 2:n if !composite[i + 1]]
end
if abspath(PROGRAM_FILE) == @__FILE__
    println(join(sieve(isempty(ARGS) ? 100 : parse(Int, ARGS[1])), " "))
end
