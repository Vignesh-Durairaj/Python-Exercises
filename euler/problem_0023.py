# Non - Abundant Sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def get_factors_sum(num):
    factors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors_sum += i
            divisor = num // i
            if divisor != i: factors_sum += divisor
    return factors_sum


def get_abundant_nums():
    return sorted({num for num in range(12, 28124) if get_factors_sum(num) > num})


def get_abundant_sums():
    abundant_nums, abundant_sums = get_abundant_nums(), {24}
    for i in abundant_nums:
        for j in abundant_nums:
            sum_val = i + j
            if sum_val < 28124:
                abundant_sums.add(sum_val)
            else: break
    return abundant_sums


def get_non_abundant_sum_total():
    abundant_sums = get_abundant_sums()
    return sum([i for i in range(1, 28124) if i not in abundant_sums])


print(get_non_abundant_sum_total())
