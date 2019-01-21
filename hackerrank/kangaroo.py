# Kangaroo

# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line
# ready to jump in the positive direction (i.e, toward positive infinity).
#
# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it
# is possible, return YES, otherwise return NO.
#
# For example, kangaroo  starts at  with a jump distance  and kangaroo  starts at  with a jump distance of . After one
# jump, they are both at , (, ), so our answer is YES.
#
# Function Description
#
# Complete the function kangaroo in the editor below. It should return YES if they reach the same position at the same
# time, or NO if they don't.
#
# kangaroo has the following parameter(s):
#
# x1, v1: integers, starting position and jump distance for kangaroo 1
# x2, v2: integers, starting position and jump distance for kangaroo 2
# Input Format
#
# A single line of four space-separated integers denoting the respective values of , , , and .
#
# Constraints
# 0 <= x1 <= x2 <= 10000
# 1 <= v1 <= 10000
# 1 <= v2 <= 10000
#
# Output Format
#
# Print YES if they can land on the same location at the same time; otherwise, print NO.
#
# Note: The two kangaroos must land at the same location after making the same number of jumps.
#
# Sample Input 0
#
# 0 3 4 2
# Sample Output 0
#
# YES
#
# Sample Input 1
#
# 0 2 5 3
# Sample Output 1
#
# NO
# Explanation 1
#
# The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting
# location (i.e., ). Because the second kangaroo moves at a faster rate (meaning ) and is already ahead of the first
# kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.

"""
Solution Approach :
===================

1. The two kangaroos should reach the same position after same number of jumps (where the jump count can be any)
2. Let kangaroo 1 starts from point 'x1' and kangaroo 2 starts from point 'x2'.
3. let  'n' be the number of jumps at which they both meet at same point
4. so at 'n' times the jump of 'v1' units and 'v2' units per jump, both will be at the same point
5. Hence : x1 + n * v1 = x2 + n * v2
6. (x1 - x2) = n (v2 - v1)
7. (x1 - x2) / (v2 - v1) = n
8. 'n' will be  whole number (without decimals), since there wont be partial jumps when they meet together
9. so the both kangaroos meet when 'n' is a whole number. (i.e.,) [x1 - x2] % [v2 - v1] == 0
10. Also considering the case 2 that both kangaroos wont meet if
    * 'x2' is greater than 'x1'
    * and 'v2' is greater than or equal to 'v1'

"""

def kangaroo(x1, v1, x2, v2):
    return 'NO' if (x2 > x1 and v2 >= v1) or (x1 - x2) % (v2 - v1) != 0 else 'YES'