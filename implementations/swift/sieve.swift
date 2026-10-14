func sieve(_ n: Int) -> [Int] {
    if n < 2 { return [] }
    var composite = [Bool](repeating: false, count: n + 1)
    var p = 2
    while p <= n / p {
        if !composite[p] {
            for m in stride(from: p * p, through: n, by: p) { composite[m] = true }
        }
        p += 1
    }
    return (2...n).filter { !composite[$0] }
}
let n = CommandLine.arguments.count > 1 ? Int(CommandLine.arguments[1])! : 100
print(sieve(n).map(String.init).joined(separator: " "))
