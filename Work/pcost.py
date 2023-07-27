# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):

    total = 0

    f = open(filename)
    #headers = next(f)
    rows = csv.reader(f)
    for row in rows:
        try:
            total += (int(row[1]) * float(row[2]))
        except:
            print('Invalid Line: ', row)
    f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

