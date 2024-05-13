'''Python program to combine values in python list of dictionaries'''

from collections import Counter

d_lst = [{'item':'shirt','price':400},{'item':'pant','price':600},{'item':'shirt','price':500}]

cv = Counter()

for dl in d_lst:

    cv[dl['item']] += dl['price']

print(cv)