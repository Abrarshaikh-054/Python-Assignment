'''Python program to combine two dictionary and add values for
common keys'''

#import counter method from collection module
from collections import Counter

#create two dictionaries with same keys and some diffrent values
dict1 = {'A':100,'B':200,'C':150}
dict2 = {'A':200,'B':200,'D':150}

#perform addtion of values with same keys using counter() method
dict3 = Counter(dict1) + Counter(dict2)

print(dict3)

