def palindrome(n):
    n = str(n)
    a = [int(digit) for digit in n]
    b = a.copy()
    b.reverse()

    if a == b:
        return True
    else:
        return False

currentmax = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if (palindrome(i*j) == True and i*j > currentmax):
            currentmax = i*j
            multiple = (str(i), "x", str(j))

print(multiple, " = ", currentmax)