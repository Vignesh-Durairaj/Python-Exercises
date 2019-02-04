# Pandigital prime
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
# 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

"""
Solution Approach :
===================
* Just another brute force, but with quick time and memory (I use a 8GB RAM computer) cycles
* Getting all the combinations of a 9 digit pandigital number and iterate over it to find a prime
* The list was sorted in reverse before iterating
* If a pandigital was found as prime, break the loop and return the value
* Else remove the largest value in the input string and repeat from step 2, till the starting input string reduced
to empty string
"""

from euler.problem_0007 import is_prime as is_prime
from itertools import permutations as permutations


def is_pandigital(num_str):
    for i in range(1, len(num_str)):
        if str(i) not in num_str: return False
    return True


def get_permutations(num_str):
    return list(map(lambda t: ''.join(t), list(permutations(num_str))))


def get_largest_pandigital_prime():
    num_str = '123456789'
    while True:
        all_nums = sorted(get_permutations(num_str), reverse=True)
        for num in all_nums:
            if is_prime(int(num)):
                return num
        num_str = num_str[:-1]
        if num_str == '': break


print(get_largest_pandigital_prime())
