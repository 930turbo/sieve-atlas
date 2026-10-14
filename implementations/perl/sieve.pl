use strict;
use warnings;
sub sieve {
    my ($n) = @_;
    return () if $n < 2;
    my @composite = (0) x ($n + 1);
    for (my $p = 2; $p <= int($n / $p); $p++) {
        next if $composite[$p];
        for (my $m = $p * $p; $m <= $n; $m += $p) { $composite[$m] = 1; }
    }
    return grep { !$composite[$_] } 2..$n;
}
print join(' ', sieve(@ARGV ? int($ARGV[0]) : 100)), "\n" unless caller;
