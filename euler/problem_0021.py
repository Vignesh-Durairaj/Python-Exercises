# Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

"""
Solution Approach :
===================

Nothing special. I used brute force. Yeah, you'd seen it correct... BRUTE FORCE. Will check for a better solution.
"""

num_dict = {}


def  get_proper_factors_sum(num):
    return sum([i for i in range(1, num) if num % i == 0])


def is_amicable(num1, num2):
    return num1 in num_dict and num2 in num_dict and num1 != num2 and num_dict[num1] == num2 and num_dict[num2] == num1


def get_amicable_sum(max_num):
    for i in range(max_num):
        num_dict[i] = get_proper_factors_sum(i)
    return sum([item for item in num_dict if is_amicable(item, num_dict[item])])


print(get_amicable_sum(10000))
