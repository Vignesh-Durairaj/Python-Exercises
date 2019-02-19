# Prime digit replacements
#
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43,
# 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
# seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
# 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

"""
Solution Approah:
=================
* Get the complete list of primes less than a million
* For an eight prime family we need a six digit prime number with 3 repeatable digits at-least
* If in case it has more than 3 of repeatable digits in any order it will be divisible by 3
* The last digit should not be a part of the repeatable digits, since this will create a composite
* Check only for digits repeating with values of 0, 1 or 2 since other higher values still give out a composite
"""

from euler.problem_0027 import get_prime_list
primes = get_prime_list(1000000)


def is_eight_primes_available(prime, num):
    counter = 0
    for digit in '0123456789':
        new_num = int(str.replace(prime, num, digit))
        if new_num > 100000 and new_num in primes:
            counter += 1
    return counter == 8


def get_solution():
    for prime in primes:
        if prime > 100000:
            prime_str = str(prime)
            last_char = prime_str[-1]
            if (prime_str.count('0') == 3 and is_eight_primes_available(prime_str, '0')
                    or prime_str.count('1') == 3 and last_char != '1' and is_eight_primes_available(prime_str, '1')
                    or prime_str.count('2') == 3 and is_eight_primes_available(prime_str, '2')):
                return prime_str


print(get_solution())
