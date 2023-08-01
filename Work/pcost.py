# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):

    total = 0

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row,line in enumerate(rows,start=1):
        record = dict(zip(headers,line))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price
        except ValueError:
            print(f'Row {row}: Bad row: {line}')
    f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

