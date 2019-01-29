# Pandigital products
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1
# through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""
Solution Approach
=================
* We need to find pandigital products whose multiplier, multiplicand and product contain all 1 to 9 number
* Hence the sum of length of  multiplier, multiplicand and product should not exceed 9
* Lets define a method to identify whether the input number string is a pandigital or not.
* Then define another method to iterate over multiplier and multiplicand at a range of 1 to 99999
* since anything beyond 99999 multiplies will give a value of 5 + 5 + 6 = 16 digits
* Get the string equivalent of multiplicand, multiplier and the product into a single string
* Check for its length to be equal to be 9 and if so, check whether it is a pandigital or not
* If true again, add the product in a set and return the sum value of the set

* NOTE : Any further iteration whose length exceeding 9 will result in non-pandigital 9 + n digit number
* Hence it is advisable to break the loop further.
"""


def is_pandigital(num_str):
    for i in range(1, 10):
        if str(i) not in num_str: return False
    return True


def get_pandigital_sum():
    prod_set = {0}
    for multiplicand in range (1, 100000):
        for multiplier in range(multiplicand, 100000):
            product = multiplicand * multiplier
            num_str = str(multiplicand) + str(multiplier) + str(product)
            if len(num_str) > 9: break;
            if len(num_str) == 9 and is_pandigital(num_str):
                prod_set.add(product)
    return sum(prod_set)


print(get_pandigital_sum())
