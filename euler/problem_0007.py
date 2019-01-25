# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

"""
Solution Approach
=================
* Iterate infinitely from 2 and check each number is prime
* if the number is prime, then increment a counter (initiated to 1, earlier)
* else move on to next number
* Break the loop if the desired counter is reached
"""


def is_prime(n):
    if n == 1:
        return True
    if n != 2 and n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1): # Iterating only upto the square root
        if n % i == 0:
            return False
    return True


def get_prime(n):
    i, counter = 2, 1
    while True:
        if is_prime(i):
            counter += 1
        if counter > n: break
        else: i += 1
    return i
