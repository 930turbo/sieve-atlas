import java.util.ArrayList;
import java.util.List;
public class Sieve {
    public static List<Integer> sieve(int n) {
        List<Integer> primes = new ArrayList<>();
        if (n < 2) return primes;
        boolean[] composite = new boolean[n + 1];
        for (int p = 2; p <= n / p; p++)
            if (!composite[p])
                for (int m = p * p; m <= n; m += p) composite[m] = true;
        for (int i = 2; i <= n; i++) if (!composite[i]) primes.add(i);
        return primes;
    }
    public static void main(String[] args) {
        var primes = sieve(args.length > 0 ? Integer.parseInt(args[0]) : 100);
        System.out.println(String.join(" ", primes.stream().map(String::valueOf).toArray(String[]::new)));
    }
}
