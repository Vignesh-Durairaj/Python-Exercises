# Digit cancelling fractions
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
# digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
Solution Approach:
=================

* We need 4 two-digit number where the numerator is less than denominator and either of them is a multiple of 10
* This reduces the iteration of possible iteration
* Define a function to find whether it is a non-trivial fraction or not
* Create a list of tuples containing non-trivial fraction as (numerator, denominator)
* Get the minimal fraction (which is the value after un-orthodox cancelling of fraction digits) for each
* Get the product of all in (numerator, denominator) format
* Divide the denominator with the GCD to get the solution
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_cancelling_fraction(num, den):
    i, j, k, l = (num // 10, num % 10, den // 10, den % 10)
    div_val = num / den
    return True if (i == k and div_val == j / l) \
                   or (i == l and div_val == j / k) \
                   or (j == k and div_val == i / l) \
                   or (j == l and div_val == i / k) else False


def get_cancelling_fractions():
    fraction_list = []
    for i in range(1, 10):
        for j in range(1, 10):
            num = den = (10 * i) + j
            while den < 99:
                den += 1
                if den % 10 == 0: continue
                if is_cancelling_fraction(num, den):
                    fraction_list.append((num, den))
    return fraction_list


def get_lowest_fraction(fraction):
    num, den = fraction
    i, j, k, l = (num // 10, num % 10, den // 10, den % 10)
    if i == k:
        return j, l
    elif i == l:
        return j, k
    elif j == k:
        return i, l
    elif j == l:
        return i, k


def get_solution():
    num_prod = den_prod = 1
    for fraction in get_cancelling_fractions():
        num_prod *= get_lowest_fraction(fraction)[0]
        den_prod *= get_lowest_fraction(fraction)[1]
    return den_prod // gcd(num_prod, den_prod)


print(get_solution())
