# Digit Fifth Powers
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""
Solution Approach:
==================
* Am going to use brute-force
* The iteration starts with '2' since '1' is not included
* The trick is to determine the upper bound
* Let us assume the number we need is 1 digit so 9 ^ 5 = 59045
* If the upper bound is 2 digit number then for 99 -> 9 ^ 5 + 9 ^ 5 = 118098 (2 * 9 ^ 5)
* For 3 Digits (3 * 9 ^ 5) = 177147
* For 4 and 5 digits they are 236196 & 295245 respectively
* For 6 and 7 digits they are 354294 and 413343 respectively.
* For a 7 digit number 7 * (2 ^ 5) = 224. So we assume the max bound is 6 digit and the larest possible number is 354294
* Now iterate for equality of the sum of individual digits powered by 5 and calculate its sum
"""


def fifth_powers_sum():
    sum_val = 0
    for num in range(2, 354295):
        power_values = map(lambda pow_val: pow_val ** 5, map(int, str(num)))
        sum_val += num if sum(power_values) == num else 0
    return sum_val


print(fifth_powers_sum())
