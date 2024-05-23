'''Python script to sort (ascending and descending) a dictionary by
value'''

#import operator module
import operator

dict = {'c':5,'php':2,'c++':4,'python':1,'asp':3}

print("Original dictionary:",dict)

#sort the dictionary using sorted() and get the items using itemgetter()
sorted_dic = sorted(dict.items(),key=operator.itemgetter(1))
#for reversed sorted dictionary add reverse equal to true
rsorted_dic = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_dic)
print(rsorted_dic)