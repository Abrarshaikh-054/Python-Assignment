'''Python program to find the highest 3 values in a dictionary'''

#import nlargest method from heapq module
from heapq import nlargest

dict = {'A':54,'B':45,'C':32,'D':27,'E':62,'F':49}

print(dict)

#getting largest values using get and nlargest()
larg = nlargest(3,dict,key = dict.get)

#print all largest values using loop
print("Three largest values:")

for v in larg:

    print(v,":",dict.get(v))