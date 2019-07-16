#!/usr/bin/python

#initial commit
#again

import argparse

def find_max_profit(prices):
  # best_profit = 0

  # for i in range(0, len(prices)):
  #   for j in range(i+1, len(prices)):
  #     best_profit = max(best_profit, prices[j] - prices[i])

  # return best_profit

  if len(prices) == 0:
    return 0

  profit = 0
  cheapest = prices[0]

  for i in range(1, len(prices)):
    cheapest = min(cheapest, prices[i])

    profit = max(profit, prices[i]-cheapest)

    max_profit = profit

  if max_profit == 0:
    return -(prices[len(prices)-1])
  else:
    return max_profit



  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))