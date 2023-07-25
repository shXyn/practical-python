# pcost.py
#
# Exercise 1.27

total = 0

f = open('Data/portfolio.csv' , 'rt')
headers = next(f)

for line in f:
    dataList = line.split(',')
    total += (int(dataList[1]) * float(dataList[2]))

print('Total cost', (total))

f.close()