'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string'''

def join_str(str):
    #check if length is less or equal to 2
    if len(str) <= 2:
        #if true then return empty string
        return ''
    
    else:
        #otherwise take first and last two character from it and make new string
        str1 = str[:2] + str[-2:]
        return str1
    
str = input("Enter any string:")

print(join_str(str))