# report.py
#
# Exercise 2.4

# pcost.py
import sys
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    stock_prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except:
                print('Invalid:', row)
    return stock_prices

def make_report(stocks,prices):
    report = []
    for s in stocks:
        current_price = prices.get(s['name'],0.0)
        change =  current_price - s['price']
        report.append((s['name'],s['shares'],current_price,change))
    return report

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/prices.csv'

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices(filename)
rept = make_report(portfolio,prices)

print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
print(f'{"----------":>10s} {"----------":>10s} {"----------":>10s} {"----------":>10s}')
for name, shares, price, change in rept:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
