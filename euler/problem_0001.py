# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys


def main():
    args = sys.argv
    if len(args) == 2 and args[1].isdigit():
        param = int(args[1])
    else:
        param = 10

    print(sum([i for i in range(1, param) if i % 3 == 0 or i % 5 == 0]))


if __name__ == '__main__':
    main()