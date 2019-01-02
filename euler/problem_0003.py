# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

"""
Solution is to define a function to determine whether a number is prime or not.
Then find the factors of the input number, check whether it is prime or not.
Iterate till the last num and return the value
"""

def is_prime(n):
    if n == 1:
        return True;

    for i in range(2, int(n ** 0.5) + 1): # Iterating only upto the square root
        if n % i == 0:
            return False;

    return True;

def large_prime_factor(n):
    i = int(n ** 0.5) + 1 # Again iterating from its square-th root value since everything beyond is not prime
    while i >= 1:
        if n % i == 0 and is_prime(i):
            return i
        else:
            i -= 1