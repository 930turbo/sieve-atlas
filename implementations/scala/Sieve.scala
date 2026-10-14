object Sieve {
  def sieve(n: Int): List[Int] = {
    if (n < 2) return Nil
    val composite = Array.fill(n + 1)(false)
    var p = 2
    while (p <= n / p) {
      if (!composite(p)) {
        var m = p * p
        while (m <= n) { composite(m) = true; m += p }
      }
      p += 1
    }
    (2 to n).filter(i => !composite(i)).toList
  }
  def main(args: Array[String]): Unit =
    println(sieve(if (args.isEmpty) 100 else args(0).toInt).mkString(" "))
}
