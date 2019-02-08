# Prime permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#   (i) each of the three terms are prime, and,
#   (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

"""
Solution Approach:
==================
* This is kinda brute force but with little catch
* Firstly populate the list of all primes that are greater than 1487 (since the above case already covers this)
* Define a function to get a list of all prime combos for an input number
* Define another function to check whether a number is a combo of another
* The start with the iteration of the prime list by comparing one against the another
* For each iteration get a number that is the sum of second number and the difference between the first and second prime
* If the sum is a prime and the first prime, second prime and the sum all are in a permutation then return the
concatenated value of these three
"""

from euler.problem_0027 import get_prime_list

prime_list = [prime for prime in get_prime_list(9999) if prime > 1487]


def get_prime_combinations(num):
    combos = list(map(int, list(map(lambda t: ''.join(t), list(permutations(str(num)))))))
    return [combo for combo in combos if combo in prime_list]


def is_combo(num1, num2):
    return num2 in get_prime_combinations(num1)


def get_solution():
    for i in range(len(prime_list)):
        for j in range(i + 1, len(prime_list)):
            k = prime_list[j] + prime_list[j] - prime_list[i]
            if k in prime_list and is_combo(prime_list[i], prime_list[j]) and is_combo(prime_list[j], k):
                return str(prime_list[i]) + str(prime_list[j]) + str(k)


print(get_solution())
