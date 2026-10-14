pub fn sieve(n: i32) -> Vec<usize> {
    if n < 2 { return Vec::new(); }
    let n = n as usize;
    let mut composite = vec![false; n + 1];
    let mut p = 2;
    while p <= n / p {
        if !composite[p] {
            for m in (p*p..=n).step_by(p) { composite[m] = true; }
        }
        p += 1;
    }
    (2..=n).filter(|&i| !composite[i]).collect()
}
fn main() {
    let n = std::env::args().nth(1).map(|s| s.parse().expect("integer limit")).unwrap_or(100);
    let line = sieve(n).iter().map(|p| p.to_string()).collect::<Vec<_>>().join(" ");
    println!("{}", line);
}
