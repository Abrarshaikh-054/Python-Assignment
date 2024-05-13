'''Python program to combine two dictionary and add values for
common keys'''

from collections import Counter

dict1 = {'A':100,'B':200,'C':150}
dict2 = {'A':200,'B':200,'D':150}

dict3 = Counter(dict1) + Counter(dict2)

print(dict3)

