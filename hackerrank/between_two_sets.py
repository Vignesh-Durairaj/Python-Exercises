# Between two sets

# You will be given two arrays of integers and asked to determine all integers that satisfy the following two
# conditions:
#
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
#
# For example, given the arrays a = [2, 6] and b = [24, 36], there are two numbers between them: 6 and 12.
# 6 % 2 == 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the first value. Similarly, 12 % 2 = 0, 12 % 6 = 0 and 24 % 12 =
# 0, 36 % 12 = 0.
#
# Function Description
#
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
#
# getTotalX has the following parameter(s):
#
# a: an array of integers
# b: an array of integers
#
# Input Format
#
# The first line contains two space-separated integers,  and , the number of elements in array  and the number of
# elements in array .
# The second line contains  distinct space-separated integers describing  where .
# The third line contains  distinct space-separated integers describing  where .
#
# Constraints
# 1 <= n, m <= 10
# 1 <= a[i] <= 100
# 1 <= b[j] <= 100
#
# Output Format
#
# Print the number of integers that are considered to be between  and .
#
# Sample Input
#
# 2 3
# 2 4
# 16 32 96
# Sample Output
#
# 3
# Explanation
#
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
#
# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of
# b.


def get_total_x(a, b):
    max_val, min_val, counter = max(a), min(b), 0
    for i in range(1, int(min_val / max_val) + 1):
        if(sum((i * max_val) %n for n in a) + sum(n % (i * max_val) for n in b))==0:
            counter += 1
    return counter
