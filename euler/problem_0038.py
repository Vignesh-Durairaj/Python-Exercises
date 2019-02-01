# Pandigital multiples
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
# of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
# (1,2, ... , n) where n > 1?

"""
Solution Approach:
==================
* We have to iterate from largest 1 digit number multiplying by a sequence
* so if the fixed digit is '9' multiplying with (1, 2, 3, 4, 5) gives '918273645'
* If the fixed number is two digit, it gives wont get a 9 digit number
* Same applies for a three digit number
* now, moving to a four digit number there is a possibility, where it can be multiplied by (1, 2)
* For a five digit number 90000 * (1, 2) = 11 digit number
* So, iterating in reverse from 9999 as a fixed digit number by (1, 2) we check for the possibility
* Break the loop once a pandigital number shows up. That's the answer
"""

from euler.problem_0032 import is_pandigital as is_pandigital


def get_largest_pandigital_multiple():
    for num in range(9999, 0, -1):
        multiple_concatenated = str(num) + str(num * 2)
        if is_pandigital(multiple_concatenated):
            return multiple_concatenated


print(get_largest_pandigital_multiple())
