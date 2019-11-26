def SumWithTerms(a0,r,n):
    if (n <= 0):
        return 0
    else: 
        return a0 + SumWithTerms(a0 + r , r , n-1)

print(SumWithTerms(3,4,5))