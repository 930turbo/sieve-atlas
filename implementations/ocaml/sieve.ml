let sieve n =
  if n < 2 then [] else begin
    let composite = Array.make (n + 1) false in
    let p = ref 2 in
    while !p <= n / !p do
      if not composite.(!p) then begin
        let m = ref (!p * !p) in
        while !m <= n do composite.(!m) <- true; m := !m + !p done
      end;
      incr p
    done;
    List.init (n - 1) (fun i -> i + 2) |> List.filter (fun i -> not composite.(i))
  end
let () =
  let n = if Array.length Sys.argv > 1 then int_of_string Sys.argv.(1) else 100 in
  print_endline (String.concat " " (List.map string_of_int (sieve n)))
