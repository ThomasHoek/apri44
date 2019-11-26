type DoubleValue = (Int, Int)

afqnumber :: Int -> Int -> Int -> Either DoubleValue String
afqnumber a b c
            | a  <= 0 || b <= 0 = Right "No values found"
            | (a * b) == c = Left (a,b)
            | otherwise = afqnumber(a-1) (b-1) c

afqmain :: Int -> Either DoubleValue String
afqmain a = afqnumber (a-1) a a