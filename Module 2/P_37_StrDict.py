'''Python program to create a dictionary from a string'''

#take string input from user
str = input("Enter any string to create dictionary:")

#take empty dictionary
dict = {}

#iterate through string 
for ch in str:
    #take each letter as key and number of occurences as value
    dict[ch] = dict.get(ch,0) + 1

print(dict)