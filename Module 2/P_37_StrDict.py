'''Python program to create a dictionary from a string'''

from collections import defaultdict,Counter

str = input("Enter any string to create dictionary:")

dict = {}

for ch in str:

    dict[ch] = dict.get(ch,0) + 1

print(dict)