# Smallest Multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_prime(n):
    if n == 1:
        return True;
    if n != 2 and n % 2 == 0:
        return False;
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False;
    return True;

def smallest_multiple(n):
    prod = 1
    for i in range(2, n + 1):
        if is_prime(i):
            j = i
            while True:
                if i * j <= n: i = i * j
                else: break
            prod *= i
    return prod
