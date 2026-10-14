// Compile with C++17. Define SIEVE_ATLAS_NO_MAIN when embedding.
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
std::vector<int> sieve(int n) {
    if (n < 2) return {};
    std::vector<std::uint8_t> composite(n + 1);
    for (int p = 2; p <= n / p; ++p)
        if (!composite[p])
            for (int m = p * p; m <= n; m += p) composite[m] = 1;
    std::vector<int> primes;
    for (int i = 2; i <= n; ++i) if (!composite[i]) primes.push_back(i);
    return primes;
}
#ifndef SIEVE_ATLAS_NO_MAIN
int main(int argc, char **argv) {
    const auto primes = sieve(argc > 1 ? std::stoi(argv[1]) : 100);
    for (auto p : primes) std::cout << p << ' ';
    std::cout << '\n';
}
#endif
