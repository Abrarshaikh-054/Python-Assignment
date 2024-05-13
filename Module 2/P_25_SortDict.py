'''Python script to sort (ascending and descending) a dictionary by
value'''

import operator

dict = {'c':5,'php':2,'c++':4,'python':1,'asp':3}

print("Original dictionary:",dict)

sorted_dic = sorted(dict.items(),key=operator.itemgetter(1))

rsorted_dic = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)


print(sorted_dic)
print(rsorted_dic)