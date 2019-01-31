# Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
Solution Approach:
==================
* The first challenge is to get the upper bound of the iteration we are going to do
* Arriving at the upper bound is quite similar to the solution for problem 0
* Lets find the number of digits it has
    * if the bound is 10 digit number then the 999999999 has the sum of factorial as 362280 * 10 = 3622800 (which is a 7
     digit number
    * if the bound is 7 digit number then 9999999 has the sum of digit factorial as 2535960 (again a 7 digit number)
* So, lets make this 2535960 as the upper bound of our iteration
* Now I'm using brute force to iterate (I'm pretty tired today and got into a mind-rust)
"""


def get_factorial_dict(max_bound):
    factorials = {0: 1, 1: 1}
    for i in range(2, max_bound + 1): factorials[i] = i * factorials[i - 1]
    return factorials


def get_digit_factorial():
    factorial_dict, total_sum = get_factorial_dict(9), 0
    for num in range(3, 2535961):
        factorial_sum = sum([factorial_dict[int(digit)] for digit in str(num)])
        total_sum += num if factorial_sum == num else 0
    return total_sum


print(get_digit_factorial())
