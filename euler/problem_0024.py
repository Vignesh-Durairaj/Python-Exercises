# Lexicographic permutations

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
# 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
Solution Approach
=================
* No brute forced used (and hence I'm not using permutations function from 'itertools' module
* Get a dictionary of numbers from 0 t 9 mapped to their factorials
* Created a source array [0 to 9] and a destination array
* We need to find the millionth lexicographic permutation ordered by natural sorting
* which means 999999th index
* when a input array of three numbers [0, 1, 2] is given, the lexicographic order is as follows
* [0, 1, 2] [0, 2, 1] [1, 0, 2] [1, 2, 0] [2, 0, 1] [2, 1, 0]
* The total combination is Factorial(N), where N is the total number of elements
* Factorial(3) = 6
* Suppose we need the 5th element, (i.e,.) [2, 0, 1] which is at index:4
* in-array = [0, 1, 2] and out-array = []
* Divide the position by factorial(N-1) = 4 / factorial(2) = 4/2 = Quotient: 2, Remainder : 0
* Move the Quotient-th index from in-array to out-array
* Out-Array : [2] in-Array:[0, 1]
* Divide the remainder with factorial(N - 2) : 0 / factorial(1) : 0/1 = 0 and 0
* Out-Array: [2, 0], In-Array : [1]
* When the factorial becomes factorial(0), append the remaining element from the out in-Array to out-Array
* [2, 0, 1]
* Iteration happens till 0!, where it starts from (position - 1)! and decrementing it for each iteration against the
remainder
"""


def get_factorial_dict():
    factorials = {0: 1, 1: 1}
    for i in range(2, 10): factorials[i] = i * factorials[i - 1]
    return factorials


def get_lex_permutation():
    num, factorials, in_list, out_list = 999999, get_factorial_dict(), [i for i in range(10)], []
    for i in reversed(range(len(in_list))):
        div, rem = num // factorials[i], num % factorials[i]
        out_list.append(in_list[div])
        del in_list[div]
        num = rem
    return ''.join(map(str, out_list))
