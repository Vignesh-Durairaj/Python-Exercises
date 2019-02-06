# Goldbach's other conjecture
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2x1^2
# 15 = 7 + 2x2^2
# 21 = 3 + 2x3^2
# 25 = 7 + 2x3^2
# 27 = 19 + 2x2^2
# 33 = 31 + 2x1^2
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""
Solution Approach:
=================
* The approach is reverse-engineering
* Defined a method to check whether a number is two times of a perfect square
* The start infinite iteration starting from 33, incrementing it by 2 for every iteration, so as to get ODD numbers
* If the iterated number is not a prime, check the difference of this odd number with all the primes less than it, and
verify whether the difference value is 'Two times of a perfect square'
* If not return the odd_num, else move to next iteration
"""

from euler.problem_0027 import get_prime_list


def is_perfect_squared_half(num):
    return ((num // 2) ** 0.5).is_integer()


def get_failing_conjucture():
    prime_list, odd_num = get_prime_list(10000), 33
    while True:
        odd_num += 2
        is_conjucture = False
        if odd_num in prime_list:
            continue
        for prime in [prime_num for prime_num in prime_list if prime_num < odd_num]:
            if is_perfect_squared_doubled(odd_num - prime):
                is_conjucture = True
                break
        if not is_conjucture:
            return odd_num


print(get_failing_conjucture())
