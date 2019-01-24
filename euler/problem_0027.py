# Quadratic Primes
# ================
#
# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <=n <= 39. However, when
# n=40, 402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2-79n+1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a| < 1000 and |b| <= 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |-4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with n=0.

"""
Solution Approach :
===================

* Since the quadratic equation of n2 + an + b = Prime number, the value of 'b' should be a prime (for n = 0)
* Also co-efficient 'a' should be odd, if b != 2, since 'b' already being odd (except 2) and adding two odds gives an
even number and adding by another number(say 1) finally gives odd
* Knowing the range of 'a' and 'b', we can iterate over them with the equation to find the number of primes for 'n'
consecutive numbers
* Comparing the number 'n' for one iteration with the previous iterations gives the max value of 'n' and the
co-efficients 'a' and 'b'
* For a defined range get value of 'a' and 'b'  for 'n' primes in consecutive values if 'n' and return its product
"""

from euler.problem_0007 import is_prime as is_prime


def get_prime_list(max_cap):
    prime_nums = []
    for num in range(2, max_cap + 1):
        if is_prime(num):
            prime_nums.append(num)
    return prime_nums


def quadratic_primes(num):
    max_val = 0
    for b in get_prime_list(num):
        for a in range(-1 * (num - 1), num, 2):
            n = 1
            while is_prime(abs(n * n + a * n + b)):
                n += 1
            if n > max_val:
                co_efficients, max_val = (a, b), n
    return co_efficients[0] * co_efficients[1]


print(quadratic_primes(1000))
