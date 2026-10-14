/* Caller owns the returned buffer. Build: cc -std=c11 sieve.c -o sieve */
#include <stdio.h>
#include <stdlib.h>

int *sieve(int n, size_t *count) {
    *count = 0;
    if (n < 2) return NULL;
    unsigned char *composite = calloc((size_t)n + 1, 1);
    int *primes = malloc(((size_t)n + 1) * sizeof *primes);
    if (!composite || !primes) { free(composite); free(primes); exit(1); }
    for (int p = 2; p <= n / p; ++p)
        if (!composite[p])
            for (int m = p * p; m <= n; m += p) composite[m] = 1;
    for (int i = 2; i <= n; ++i) if (!composite[i]) primes[(*count)++] = i;
    free(composite);
    return primes;
}
#ifndef SIEVE_ATLAS_NO_MAIN
int main(int argc, char **argv) {
    int n = argc > 1 ? atoi(argv[1]) : 100;
    size_t count;
    int *primes = sieve(n, &count);
    for (size_t i = 0; i < count; ++i) printf("%s%d", i ? " " : "", primes[i]);
    puts(""); free(primes); return 0;
}
#endif
