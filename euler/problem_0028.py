# Number Spiral Diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# [21] 22 23 24 [25]
# 20  [7]  8  [9] 10
# 19  6  [1]  2   11
# 18  [5]  4  [3] 12
# [17] 16 15 14 [13]
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""
Solution Approach
=================
* Start a list with '1' as it content and an incrementer initialised to '2'
* Since every level of the square surrounding the center increase its size by two units the incrementer was initialized
to 2
* Iterate over four times to add the recent value of a temporary number with the incrementer
* Add each of them in the list (as in step 1)
* Increment the 'incrementer' by 2 for next level
* check whether the last value added in the list is less than the squared value of the dimension.
* like '25' for a 5 X 5 square
* If it exceeds break the iteration and return the sum of the list contents
"""


def num_spiral_diagonals(num):
    diagonal_num, incrementer, diag_nums = 1, 2, [1]
    while diagonal_num < num ** 2:
        for i_unused in range(0, 4):
            diagonal_num += incrementer
            diag_nums.append(diagonal_num)
        incrementer += 2
    return sum(diag_nums)
