# Circular Primes
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
# prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

"""
Solution Approach:
==================
* Just another brute force, as in the previous solution. I.m really lazy today to think
* One trick I used is to filter out the primes containing a digit which is even, since while rotation, it may become an
even number
"""

from euler.problem_0027 import get_prime_list as get_prime_list


primes_list = get_prime_list(1000000)

def rotate_number(num):
    return str(num)[1:] + str(num)[0]


def is_all_rotations_prime(num_str):
    for i_unused in range(0, len(num_str)):
        num_str = rotate_number(num_str)
        if int(num_str) not in primes_list:
            return False
    return True


def get_circular_primes():
    circular_primes = []
    for prime in primes_list:
        prime_str = str(prime)
        for digit in prime_str:
            if digit in ['0', '2', '4', '6', '8']: continue
        if is_all_rotations_prime(prime_str):
            circular_primes.append(prime)
    return circular_primes


print(len(get_circular_primes))
