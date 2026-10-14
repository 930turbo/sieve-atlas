using System;
using System.Collections.Generic;
public static class PrimeSieve {
    public static List<int> Sieve(int n) {
        var primes = new List<int>();
        if (n < 2) return primes;
        var composite = new bool[n + 1];
        for (int p = 2; p <= n / p; p++)
            if (!composite[p])
                for (int m = p * p; m <= n; m += p) composite[m] = true;
        for (int i = 2; i <= n; i++) if (!composite[i]) primes.Add(i);
        return primes;
    }
    public static void Main(string[] args) {
        Console.WriteLine(string.Join(" ", Sieve(args.Length > 0 ? int.Parse(args[0]) : 100)));
    }
}
