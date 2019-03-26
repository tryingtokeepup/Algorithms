#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n == 2:
        return 2
    if n == 1:
        return 1
    if n == 0:
        return 1
    elif cache and cache[n] > 0:  # i still don't know why we need cache[n] > 0
        return cache[n]
    else:
        # if no cache, we will make the cache
        if not cache:
            # sean, explain dictionary comprehensions. this shit is wild son
            cache = {i: 0 for i in range(n+1)}
            print(cache)
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

# def fib(n, cache=None):
#   if n < 2:
#     return n
#   elif cache and cache[n] > 0:
#     return cache[n]
#   else:
#     if not cache:
#       cache = {i: 0 for i in range(n+1)}
#     cache[n] = fib(n-1, cache) + fib(n-2, cache)
#     return cache[n]

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
