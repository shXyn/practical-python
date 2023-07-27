# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):

    total = 0

    f = open(filename , 'rt')
    headers = next(f)

    for line in f:
        dataList = line.split(',')
        total += (int(dataList[1]) * float(dataList[2]))
    f.close()
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)

