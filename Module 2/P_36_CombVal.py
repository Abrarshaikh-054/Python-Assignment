'''Python program to combine values in python list of dictionaries'''

#import counter method from collection module
from collections import Counter

#create a list of dictionary with item and value
d_lst = [{'item':'shirt','price':400},{'item':'pant','price':600},{'item':'shirt','price':500}]

#create counter object
cv = Counter()

#traverse the dictionary and perform combine additon of values
for dl in d_lst:

    cv[dl['item']] += dl['price']

print(cv)