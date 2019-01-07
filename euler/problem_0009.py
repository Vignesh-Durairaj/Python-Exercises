# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

"""
Solution Approach
=================

* Using Euclid's Formula, for a right angled triangle whose sides are a, b and c, the side are constructed using two
random number m & n, where n < m, as below
* a = m^2 - n^2
* b = 2mn
* c = m^2 - n^2

* Iterate over a series of numbers upto the square root of desired number (since beyond the root i^2 will be over i
during summation

"""

def pythagoras_triplet_prod(summation):
    root = int(summation ** 0.5)
    for n in range(1, root + 1):
        for m in range(n + 1, root + 1): # So that 'm' will always be greater than 'n'
            a, b, c = (m ** 2) - (n ** 2), 2 * m * n, (m ** 2) + (n ** 2)
            if a + b + c == summation: return a * b * c