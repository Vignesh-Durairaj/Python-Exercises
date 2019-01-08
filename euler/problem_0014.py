# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

"""
Solution Approach
=================

* Optimization using 'Memoization'
* Starting with the number of collatz sequence for the largest number
* A dictionary was used to store the number of elements in its Collatz sequence
* Moving to the next least value by decrementing, evaluate the collatz sequence
* If the new sequence of number is available in the dictionary, add the current counter with the value and input new
entry to the dictionary
* Populate a map/dict of numbers with total number of Collatz sequence
* Sort the map by the value
* Return the first element's Key to get the number having longest collatz sequence
* Return the first element's Key to get the number of collatz sequence, which is the maximum

"""
def longest_collatz(n):
    my_dict = {1: 1}
    while n > 1:
        counter, num = 0, n
        while num > 1:
            if num in my_dict:
                my_dict[n] = counter + my_dict[num]
                break
            else:
                if num % 2 == 0: num = num / 2
                else: num = (3 * num) + 1
                counter += 1
            my_dict[n] = counter + 1
        n -= 1

    sorted_tuple = sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_tuple[0][0]