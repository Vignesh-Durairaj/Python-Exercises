# Consecutive prime sum
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
Solution Approach:
=================
Just another brute force
"""

from euler.problem_0027 import get_prime_list


def get_max_consec_prime_sum(max_cap):
    primes, max_sum, max_exec = get_prime_list(max_cap), 0, -1
    for i in range(len(primes)):
        sum_val = 0
        for j in range(i, len(primes)):
            sum_val += primes[j]
            if sum_val > max_cap:
                break
            if sum_val in primes and sum_val > max_sum and (j - i) > max_exec:
                max_exec = j - i
                max_sum = sum_val
    return max_sum


print(get_max_consec_prime_sum(1000000))
