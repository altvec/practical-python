#!/usr/bin/env python3

# pcost.py
#
# Exercise 1.27
from report import read_portfolio


def portfolio_cost(filename):
    '''Return portfolio cost.'''
    portfolio = read_portfolio(filename)
    return sum([s.cost for s in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfolio_file')
    cost = portfolio_cost(args[1])
    print(f'Total cost: {cost}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
