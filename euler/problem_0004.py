# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

"""
Solution approach
=================

* Define a function to determine whether a number is a palindrome or not
* Iterate all the desired digits of numbers and multiply them from the largest to smallest
* Check whether the product is a palindrome or not
* Return the value.
"""

def is_palindrome(n):
    n_str = str(n)
    return True if n_str == n_str[::-1] else False

"""
Parameter n = number of digits
"""
def large_palindrome_product(n):
    num = 10 ** n

    for i in range(num - 1, (num // 10) + 1, -1):
        for j in range(num - 1, (num // 10) + 1, -1):
            prod = i * j;
            if prod % 10 == 0: break
            if is_palindrome(prod):
                return prod