#!/usr/bin/python

import sys

# Time Complexity(2^n) Awful but possibly un avoidable
# Space Complexity(2^n) Builds an output of size 3^n


def rock_paper_scissors(n):
    if n < 1:
        return [[]]
    if n > 1:
        games = [['rock']+i for i in rock_paper_scissors(n-1)]
        games += [['paper']+i for i in rock_paper_scissors(n-1)]
        games += [['scissors']+i for i in rock_paper_scissors(n-1)]
        return games

    else:
        return [['rock'], ['paper'], ['scissors']]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
