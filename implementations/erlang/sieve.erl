%% escript entry point; sets records composite multiples in a balanced tree.
-module(sieve).
-export([main/1, sieve/1]).
sieve(N) when N < 2 -> [];
sieve(N) ->
    Composite = mark(2, N, sets:new()),
    [I || I <- lists:seq(2, N), not sets:is_element(I, Composite)].
mark(P, N, Composite) when P * P > N -> Composite;
mark(P, N, Composite) ->
    Next = case sets:is_element(P, Composite) of
        true -> Composite;
        false -> cross(P * P, P, N, Composite)
    end,
    mark(P + 1, N, Next).
cross(M, _P, N, Composite) when M > N -> Composite;
cross(M, P, N, Composite) -> cross(M + P, P, N, sets:add_element(M, Composite)).
main(Args) ->
    N = case Args of [] -> 100; [First | _] -> list_to_integer(First) end,
    io:format("~s~n", [string:join([integer_to_list(P) || P <- sieve(N)], " ")]).
