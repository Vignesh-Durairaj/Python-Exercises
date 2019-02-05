# Pentagon numbers
#
# Pentagonal numbers are generated by the formula, P(n) = n(3n-1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P(4) + P(7) = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, P(j) and P(k), for which their sum and difference are pentagonal and
# D = |P(k) - P(j)| is minimised; what is the value of D?

"""
Solution Approach:
==================
* The formula to detect whether a number 'n' is pentagonal or not is (square root(24n + 1) + 1) / 6 = Natural Number
* Now we can iterate infinitely for natural number starting from 1 and get the pentagonal number of it, followed by the
pentagonal numbers of other numbers less than the first value
* Check whether the sum of these two pentagonal numbers and their difference are pentagonal too
* If so, return the difference of these two, which will be the least in case and break the loop
* This is quite a brute force too !
"""


def get_pentagonal_num(num):
    return num * ((3 * num) - 1) // 2


def is_pentagonal(num):
    return (((((24 * num) + 1) ** 0.5)  + 1) / 6).is_integer()


def get_pentagonal_difference():
    is_done, a = False, 1
    while not is_done:
        a += 1
        j = get_pentagonal_num(a)
        for b in reversed(range(1, a)):
            k = get_pentagonal_num(b)
            if is_pentagonal(j - k) and is_pentagonal(j + k):
                return j - k


print(get_pentagonal_difference())