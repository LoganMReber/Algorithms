#!/usr/bin/python

import argparse

# Space Complexity = O(1)
# Time Complexity = O(n)


def find_max_profit(prices):
    # when true stock prices are climbing
    climbing = False
    # highest is the highest value the stock can have
    # since you must always sell it can never be 0
    highest = 1
    # best_low is the valley with the largest difference
    # between itself and 'highest'
    # must start as 0, otherwise lowest could never be 0
    best_low = 0
    # cur_low is the bottom of the current valley
    # must start as 1, otherwise a negative profit can't
    # be returned
    cur_low = 1
    for i in range(2, len(prices)):
        climbing = prices[i] > prices[i-1]  # check if delta is positive

        if not climbing:
            # if descending i is the bottom of current valley
            cur_low = i
        else:
            # has to check if there is a better delta in a peaks shadow
            # example: 90=>100 is worse than 10=>30
            if prices[i]-prices[cur_low] > prices[highest]-prices[best_low]:

                highest = i
                if prices[cur_low] < prices[best_low]:
                    # the cur_low is the best_low if cur_low is
                    # on the correct side of peak. Therefore best_low
                    # is only found as the highest peak is found
                    best_low = cur_low

    return prices[highest] - prices[best_low]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}."
          .format(profit=find_max_profit(args.integers), prices=args.integers))
