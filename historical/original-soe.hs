import Data.List (filter)

sieve :: Integral a => a -> [a]
sieve n = sieve' [2..n]
    where sieve' []     = []
          sieve' (p:xs) = p : sieve' (filter (\x -> x `mod` p /= 0) xs)

main :: IO ()
main = do
    putStrLn "Enter a number: "
    n <- readLn :: IO Int
    let primes = sieve n
    print primes
