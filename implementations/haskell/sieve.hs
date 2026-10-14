-- Mutable unboxed marking inside ST; the public function stays pure.
import Control.Monad (forM_, when)
import Data.Array.ST (runSTUArray, newArray, readArray, writeArray)
import Data.Array.Unboxed (UArray, (!))
import System.Environment (getArgs)

sieve :: Int -> [Int]
sieve n
  | n < 2 = []
  | otherwise = [i | i <- [2..n], not (composite ! i)]
  where
    composite :: UArray Int Bool
    composite = runSTUArray $ do
      a <- newArray (0, n) False
      forM_ (takeWhile (\p -> p <= n `div` p) [2..n]) $ \p -> do
        marked <- readArray a p
        when (not marked) $
          forM_ [p*p, p*p+p..n] $ \m -> writeArray a m True
      return a

main :: IO ()
main = do
  args <- getArgs
  let n = if null args then 100 else read (head args)
  putStrLn $ unwords $ map show $ sieve n
