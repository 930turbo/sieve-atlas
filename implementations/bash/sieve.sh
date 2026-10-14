#!/usr/bin/env bash
# Bash 4+. Uses an indexed array; intended for small educational examples.
sieve() {
    local n=$1 p m i
    local -a composite=()
    for ((p=2; p<=n/p; p++)); do
        if [[ ${composite[p]:-0} == 0 ]]; then
            for ((m=p*p; m<=n; m+=p)); do composite[m]=1; done
        fi
    done
    for ((i=2; i<=n; i++)); do
        if [[ ${composite[i]:-0} == 0 ]]; then printf '%d ' "$i"; fi
    done
    printf '\n'
}
if [[ ${BASH_SOURCE[0]} == "$0" ]]; then sieve "${1:-100}"; fi
