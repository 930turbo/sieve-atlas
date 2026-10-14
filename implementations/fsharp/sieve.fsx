let sieve n =
    if n < 2 then [] else
    let composite = Array.create (n + 1) false
    let mutable p = 2
    while p <= n / p do
        if not composite.[p] then
            for m in p * p .. p .. n do composite.[m] <- true
        p <- p + 1
    [ for i in 2 .. n do if not composite.[i] then yield i ]
let args = fsi.CommandLineArgs |> Array.skip 1
let n = if args.Length = 0 then 100 else int args.[0]
sieve n |> List.map string |> String.concat " " |> printfn "%s"
