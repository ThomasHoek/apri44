minim = 101

def af1(minim):
    for i in range(10, 99, 1):
        for t in range(10, 99, 1):
            if i*t < 1000:
                k = i*t
                c = k % 10
                k = (k - c) / 10

                b = k % 10
                k = (k-b) / 10

                a = k % 10
                k = (k-a) / 10
                # print(100 * c + 10 * b + a)

                if (100 * c + 10 * b + a == i * t) and minim < i*t:
                    minim = i*t
                    print(minim)
    print(minim)

def afq2(minim):
    minim = 101

    for i in range(100, 999, 1):
        for t in range(100, 999, 1): 
            k = i*t
            d = k % 10
            k = (k - d) / 10

            c = k % 10
            k = (k-c) / 10

            b = k % 10
            k = (k-b) / 10

            a = k % 10
            k = (k-a) / 10
            print("--->",  1000 * d + 100 * c + 10 * b + a)
            if d == a and minim < i*t:
                minim = i*t
    print(minim)




def palindromes(x):
    if (len(x) <= 3):
        return (x[0] == x[-1])
    elif (x[0] == x[-1] ):
        return palindromes(x[1:-1])
    else:
        return False

# minim = str(input("What palindrome do you want to check"))
# print(palindromes(minim))




