# Truncatable primes
#
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
# 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
Solution Approach:
==================
* The smallest two digit prime is 11, which is not a truncatable prime. So the smallest truncatable prime which is not
a single digit one is 23.
* So iterate infinitely from 23, for all the even number for a prime and if prime, check whether it is a truncatable
prime. If so add them in a list
* Break the loop once the list contains 11 items added
* To check whether a number is a truncatable prime :
    * check the Remainder and quotient of the number divided by 10, which should be prime in both cases
    * increment the divisor by a multiplying factor of 10, until it reaches the same size of the number
    * If it is prime in all cases, it is a truncatable prime
"""

from euler.problem_0007 import is_prime as is_prime


def is_truncatable_prime(num):
    divisor = 1
    for i_unused in range (10, num):
        divisor *= 10
        if not is_prime(num % divisor) or not is_prime(num // divisor):
            return False
        if len(str(divisor)) == len(str(num)):
            break
    return True


def get_truncatable_primes():
    truncatable_primes, prime_num = [], 23
    while len(truncatable_primes) < 11:
        if is_prime(prime_num) and is_truncatable_prime(prime_num):
            truncatable_primes.append(prime_num)
        prime_num += 2
    return truncatable_primes


print(sum(get_truncatable_primes()))
