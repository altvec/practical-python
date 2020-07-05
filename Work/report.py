#!/usr/bin/env python3

# report.py
#
# Exercise 2.4

import tableformat
from stock import Stock
from portfolio import Portfolio
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
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return Portfolio(portfolio)


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


def print_report(reportdata, formatter):
    '''Print formatted report.'''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    '''Make a stock report given portfolio and price data files.'''
    portfolio = read_portfolio(portfolio_file)
    prices    = read_prices(prices_file)
    report    = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfolio_file prices_file format')
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
