// Segmented C++17 sieve. Result storage is separate from the marking window.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
std::vector<int> sieve(int n, int block_size = 32768) {
    if (block_size < 1) throw std::invalid_argument("positive block size required");
    if (n < 2) return {};
    int root = static_cast<int>(std::sqrt(n));
    std::vector<bool> flags(root + 1, false);
    std::vector<int> base, primes;
    for (int p = 2; p <= root; ++p) {
        if (flags[p]) continue;
        base.push_back(p);
        for (std::int64_t m = 1LL*p*p; m <= root; m += p) flags[m] = true;
    }
    for (std::int64_t low = 2; low <= n; low += block_size) {
        auto high = std::min<std::int64_t>(n + 1LL, low + block_size);
        std::vector<std::uint8_t> composite(high - low, 0);
        for (auto p : base) {
            auto start = std::max<std::int64_t>(1LL*p*p, ((low+p-1)/p)*p);
            for (auto m = start; m < high; m += p) composite[m-low] = 1;
        }
        for (auto i = low; i < high; ++i) if (!composite[i-low]) primes.push_back(static_cast<int>(i));
    }
    return primes;
}
#ifndef SIEVE_ATLAS_NO_MAIN
int main(int argc, char** argv) {
    for (auto p : sieve(argc > 1 ? std::stoi(argv[1]) : 100)) std::cout << p << ' ';
    std::cout << '\n';
}
#endif
