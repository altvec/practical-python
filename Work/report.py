#!/usr/bin/env python3

# report.py
#
# Exercise 2.4

from stock import Stock
from fileparse import parse_csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = parse_csv(
            lines,
            select=['name', 'shares', 'price'],
            types=[str, int, float],
        )
    return [Stock(d['name'], d['shares'], d['price']) for d in portdicts]


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        current_price = prices[s.name]
        change        = current_price - s.price
        report.append((s.name, s.shares, current_price, change))
    return report


def print_report(report):
    '''
    Print formatted report.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(portfolio_file, prices_file):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_file)
    prices    = read_prices(prices_file)
    report    = make_report(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfolio_file prices_file')
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
