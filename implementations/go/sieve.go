package main
import (
    "fmt"
    "os"
    "strconv"
)
func Sieve(n int) []int {
    primes := []int{}
    if n < 2 { return primes }
    composite := make([]bool, n+1)
    for p := 2; p <= n/p; p++ {
        if !composite[p] {
            for m := p*p; m <= n; m += p { composite[m] = true }
        }
    }
    for i := 2; i <= n; i++ { if !composite[i] { primes = append(primes, i) } }
    return primes
}
func main() {
    n := 100
    if len(os.Args) > 1 {
        value, err := strconv.Atoi(os.Args[1]); if err != nil { panic(err) }; n = value
    }
    for _, p := range Sieve(n) { fmt.Printf("%d ", p) }; fmt.Println()
}
