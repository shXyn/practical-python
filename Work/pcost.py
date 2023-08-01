# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):

    total = 0

    f = open(filename)
    headers = next(f)
    rows = csv.reader(f)
    for row,line in enumerate(rows):
        try:
            total += (int(line[1]) * float(line[2]))
        except ValueError:
            print(f'Row {row}: Bad row: {line}')
    f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

