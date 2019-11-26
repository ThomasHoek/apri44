def fibonacchi_sum(a,b):
    while (b <= 4000000):
        if (b % 2 == 0):
            return b + fibonacchi_sum(b,a+b)
        else: 
            return fibonacchi_sum(b,a+b)
    return 0
print(fibonacchi_sum(1,2))