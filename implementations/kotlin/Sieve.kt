fun sieve(n: Int): List<Int> {
    if (n < 2) return emptyList()
    val composite = BooleanArray(n + 1)
    var p = 2
    while (p <= n / p) {
        if (!composite[p]) {
            var m = p * p
            while (m <= n) { composite[m] = true; m += p }
        }
        p++
    }
    return (2..n).filter { !composite[it] }
}
fun main(args: Array<String>) {
    println(sieve(if (args.isEmpty()) 100 else args[0].toInt()).joinToString(" "))
}
