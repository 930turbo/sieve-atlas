param([int]$Limit = 100)
function Get-SievePrimes {
    param([int]$N)
    if ($N -lt 2) { return }
    $composite = [bool[]]::new($N + 1)
    for ($p = 2; $p -le [math]::Floor($N / $p); $p++) {
        if (-not $composite[$p]) {
            for ($m = $p * $p; $m -le $N; $m += $p) { $composite[$m] = $true }
        }
    }
    for ($i = 2; $i -le $N; $i++) { if (-not $composite[$i]) { $i } }
}
if ($MyInvocation.InvocationName -ne '.') {
    Write-Output ((Get-SievePrimes -N $Limit) -join ' ')
}
