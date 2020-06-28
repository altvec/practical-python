# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            portfolio.append({
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price']),
            })
    return portfolio


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        current_price = prices[s['name']]
        change        = current_price - s['price']
        report.append(
            (s['name'], s['shares'], current_price, change)
        )
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


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
