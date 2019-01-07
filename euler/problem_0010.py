# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def is_prime(n):
    if n == 1:
        return True;
    if n != 2 and n % 2 == 0:
        return False;
    for i in range(2, int(n ** 0.5) + 1): # Iterating only upto the square root
        if n % i == 0:
            return False;
    return True;

def prime_sum(n):
    nums = []
    for num in range(2, n):
        if is_prime(num): nums.append(num)
    return sum(nums)
