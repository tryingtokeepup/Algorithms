#!/usr/bin/python

import sys
import math


# def strip_out_useless_coins(amount, coin_types):
#     for coin in coin_types:
#         if amount > coin:
#             coin_types.remove(coin)  # this is amazing, so i can legit

#     return coin_types


# def recursive_coins(quotient):
#     if quotient == 5:
#         return 2
#     if quotient == 10:
#         return 4

# def making_change(amount, denominations):
#     # this will be constant cool story bro
#     coin_types = strip_out_useless_coins(amount, denominations)
#     if amount < 0:
#         return print("Please enter a positive amount. WE don't have test cases for negatives, lol.")
#     elif amount < 5:
#         return 1

#     else:
#         # so, we need to divide the amount by the largest coin_type possible
#         while amount > coin_type[-1]:
#         # so let's take 14. you can take a dime, which is f(10). f(1) 4 times
#             remainder = amount % coin_types[-1]
#             quotient = math.floor(amount / coin_types[-1])


def making_change(amount, denominations):
    # this allows us to iterate over 0 all the way through 10, which is technically 11 elements
    ways_to_change = [0 for amount in range(amount+1)]
    ways_to_change[0] = 1
    for denom in denominations:  # this will be pennies, nickels, dimes, half-dollars, quarters
        # we don't try to divide 0 by pennies and stuff lol
        for amount in range(1, amount+1):
            if denom <= amount:  # for example, if amount is dime, we can put denoms up to dimes into the dime
                ways_to_change[amount] += ways_to_change[amount - denom]
    return print(ways_to_change[amount])


# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(
#             ways=making_change(amount, denominations), amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")
making_change(300, [1, 5, 10, 25, 50])
