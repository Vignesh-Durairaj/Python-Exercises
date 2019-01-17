# Reciprocal cycles

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to
# 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
# cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
Solution Approach :
===================

* The maximum possible cycle for reciprocal of a number N is N-1
* Identify the number of digits that cycle through, while making a reciprocal and add 1 to get the solution
* How to find the number if digits that cycle through
    * divide the number by 1 and get its remainder, add them in a list
    * Multiply the remainder by 10 and divide again to get its remainder.
    * Check whether the new remainder exists in the list. If not so, add this too
    * else break the loop
    * Continue till a perfect division occurs
    * The length of the remainder list is equal to the number of digits cycled if not divided by perfect zero at any
    point
"""


def get_cycle_count(num):
    val, rem_arr = 1, []
    rem = val % num
    while rem not in rem_arr and rem != 0:
        rem_arr.append(rem)
        val = rem * 10
        rem = val % num
    return len(rem_arr)


def get_max_cycled_divisor(num):
    max_cycle_count = 0
    for i in range(1,num):
        remainder_cycle = get_cycle_count(i)
        max_cycle_count = max(max_cycle_count, remainder_cycle)
    return max_cycle_count + 1


print(get_max_cycled_divisor(1000))
