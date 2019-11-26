sumWithTerms :: Integer -> Integer -> Integer ->  Integer
sumWithTerms a b c
        | (c <= 0) = 0
        | otherwise = a + sumWithTerms (a+b) b (c-1)

-- solving using terms. 