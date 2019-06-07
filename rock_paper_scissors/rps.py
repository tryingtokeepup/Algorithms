#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # return needs to be a list
    # we also need possible choices

    hand = ['rock', 'paper', 'scissors']
    results = []
    if n == 0:
        return [[]]
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]

    def recursive_append(current_n, awaiting=[]):
        # if current_n == 0, take completed awaiting and append to results
        if current_n == 0:
            results.append(awaiting)
            return

        for option in hand:
            recursive_append(current_n - 1, awaiting+[option])

    recursive_append(n, [])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
