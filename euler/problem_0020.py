# Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def get_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * get_factorial(num - 1)


def get_factorial_digit_sum(num):
    fact, num_arr = str(get_factorial(num)), []
    for i in range(len(fact)):
        num_arr.append(int(fact[i]))
    return sum(num_arr)


print(get_factorial_digit_sum(100))
