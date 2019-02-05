# Problem 6

# he sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
Solution Approach
=================

* Sum of natural numbers upto N = N(N+1)/2
* Sum of square of natural numbers upto N = N(N+1)(2N+1)/6
* Applying above formulae to identify the number reduces the complexity
"""


def square_sum_diff(n):
    sum_val = n * (n + 1) / 2
    square_sum = n * (n + 1) * ((2 * n) + 1) / 6
    return (sum_val ** 2) - square_sum
