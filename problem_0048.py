# Self powers
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""
Nothing special here, it is brute force.
"""


def get_solution():
    sum_val = 0
    for i in range (1, 1001):
        sum_val += i ** i
    return str(sum_val)[-10:]


print(get_solution())
