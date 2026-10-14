# R vectors are one-indexed: candidate i is stored at i + 1.
sieve <- function(n) {
  if (n < 2) return(integer(0))
  composite <- rep(FALSE, n + 1L)
  p <- 2L
  while (p <= n %/% p) {
    if (!composite[p + 1L]) {
      composite[seq.int(p * p, n, by = p) + 1L] <- TRUE
    }
    p <- p + 1L
  }
  candidates <- seq.int(2L, n)
  candidates[!composite[candidates + 1L]]
}
if (sys.nframe() == 0L) {
  args <- commandArgs(trailingOnly = TRUE)
  cat(paste(sieve(if (length(args)) as.integer(args[1]) else 100L), collapse = " "), "\n", sep = "")
}
