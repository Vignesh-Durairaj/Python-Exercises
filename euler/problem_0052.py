# Permuted Multiples
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
# order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""
Solution Approach:
==================
* Let us assume that the n-digit number is having unique digits
* n, 2n, 3n, 4n, 5n and 6n have those unique digits in any order
* Another assumption is that we consider that the number is a six digit number
* Lets iterate from 100000 and check whether 'n' to '6n' has same digits
* If not increment and continue, else return the value since its multiples upto 6 times has same digits
"""


def sort_num(num):
    return sorted(str(num))


def get_solution():
    num = 100000
    while not sort_num(2 * num) == sort_num(3 * num) == sort_num(4 * num) == sort_num(5 * num) == sort_num(6 * num):
        num += 1
    return num


print(get_solution())
