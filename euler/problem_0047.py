# Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 x 7
# 15 = 3 x 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
# 
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

"""
Solution Approach:
=================
* Used Brute Force. Nothing special in the algorithm
"""

from euler.problem_0027 import get_prime_list


def get_prime_factor_count(num, primes):
    factors = {0}
    for prime in primes:
        if prime > num:
            break
        if num % prime == 0:
            factors.add(prime)
    return len(factors) - 1


def get_solution():
    primes, num, consecutive_counter = get_prime_list(100000), 1, 0
    prime_factors_needed, consecutive_values_needed = 4, 4
    while True:
        num += 1
        prime_factor_count = get_prime_factor_count(num, primes)
        if prime_factor_count >= prime_factors_needed:
            consecutive_counter += 1
        else:
            consecutive_counter = 0
        if consecutive_counter == consecutive_values_needed:
            return num - consecutive_values_needed + 1


print(get_solution())
