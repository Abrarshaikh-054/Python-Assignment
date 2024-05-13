'''Python program to find the highest 3 values in a dictionary'''

from heapq import nlargest

dict = {'A':54,'B':45,'C':32,'D':27,'E':62,'F':49}

print(dict)

larg = nlargest(3,dict,key = dict.get)

print("Three largest values:")

for v in larg:

    print(v,":",dict.get(v))