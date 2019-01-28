# Coin Sums
#
# In England the currency is made up of pound - GBP, and pence - p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, GBP1 (100p) and GBP2 (200p).
# It is possible to make GBP2 in the following way:
#
# 1 x GBP1 + 1 x 50p + 2 x 20p + 1 x 5p + 1 x 2p + 3 x 1p
# How many different ways can GBP2 be made using any number of coins?

"""
Solution Approach :
===================
* Create a list of coins
* Iterate over each of the available coins
* Iterate again for the amount to be calculated from the coins face value to the desire amount
* Create another list of possibilities which starts with '1' where '1p' of 1 coin forms '1p' value in face
* Populate the possibility matrix by summing up the value of current with the total possibility to obtain the value with
 the previous coins
 * Iterate till the end and return the last element in the possibility matrix/list.
"""


def get_coin_sum(amount):
    coins, possibilities = [1, 2, 5, 10, 20, 50, 100, 200], [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            possibilities[i] += possibilities[i - coin]
    return possibilities[amount]


print(get_coin_sum(200))
