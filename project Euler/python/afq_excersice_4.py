import math

def prime_prime(n): # checks if the number found is  a prime
    print(n)
    for i in range(3, n-2,2):   
        if (n % i == 0): 
            return False
    return True

def highest_prime(n):
    test_value = math.floor(n**(0.5)) # get sqrt of n rounded down
    if test_value % 2 == 0: # if value is even lower by 1
        test_value -= 1
    for i in range(test_value,3, -2):  # counts down from the rounded down root in steps of 2
        if (n % i == 0 and prime_prime(i)):               # Finds any number who devided by the n is 0.  and tests if the number found really is a prime
            return i

print(highest_prime(600851475143))




# def afq_code(n):
#     for i in range(1000000-1,2, -2):
#         if n % i == 0:
#             if prime_prime(i) != 0:
#                 return i