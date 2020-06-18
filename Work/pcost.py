# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    '''Return portfolio cost.'''
    cost = 0.0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        next(rows)  # skip headers
        for row in rows:
            _, shares, price = row
            try:
                cost += int(shares) * float(price)
            except ValueError as err:
                print(err)
                continue
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
