# Champernowne's constant
#
# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)

"""
Solution Approach :
===================
* Pretty brute force this time
* Iterated infinitely to get a number starting from 0 and appending with next integer, incremented by 1
* Break the iteration till it reaches the 1000000th digit
* Get the 10, 100, 1000, 10000, 100000, 1000000th digit of that number and sum that to get the solution
"""

from euler.problem_0008 import prod as prod


def get_number_string():
    num_str, int_val = '', 0
    while True:
        num_str += str(int_val)
        if len(num_str) > 1000000: break
        else: int_val += 1
    return num_str


def get_solution():
    number_str = get_number_string()
    return prod([int(number_str[10**i]) for i in range(7)])


print(get_solution())
