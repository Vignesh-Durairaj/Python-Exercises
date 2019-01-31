# Double-base palindromes
#
# The decimal number, 585 = 1001001001b2 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

"""
Solution Approach:
==================


"""


def is_palindrome(str_val):
    for i in range(0, (len(str_val) // 2) + 1):
        if str_val[i] != str_val[len(str_val) - 1 - i]:
            return False
    return True


def get_palindrome_numbers_list(upper_bound):
    palindrome_list = []
    for num in range(1, upper_bound + 1):
        if is_palindrome(str(num)): palindrome_list.append(num)
    return palindrome_list


def is_binary_palindrome(num):
    binary_val = bin(num)[2:]
    return True if binary_val[0] == '1' and binary_val[-1] == '1' and is_palindrome(binary_val) else False


def get_double_base_palindrome_sum():
    palindromes, double_base_palindrome = get_palindrome_numbers_list(999999), []
    for palindrome in palindromes:
        if is_binary_palindrome(palindrome):
            double_base_palindrome.append(palindrome)
    return sum(double_base_palindrome)


print(get_double_base_palindrome_sum())
