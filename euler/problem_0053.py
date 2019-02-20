# Combinatoric selections
#
# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#
# nCr =	 n! / r!(n−r)!
# where r ≤ n, n! = nx(n−1)x...x3x2x1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

"""
Solution Approach:
==================
* Brute force.....
* Going to iterate from 100 to 1 and calculate the count of combinations that are exceeding a million
"""

from euler.problem_0034 import get_factorial_dict


def get_solution():
    factorial_dict, counter = get_factorial_dict(100), 0
    for n in range(1, 101):
        for r in range(n + 1):
            if factorial_dict[n] / (factorial_dict[r] * factorial_dict[n - r]) > 1000000:
                counter += 1
    return counter


print("Solution is :", get_solution())
