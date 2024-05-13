'''Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''

str = input("Enter any string:")

#find length of string using len function
len = len(str)

#check if length is less or equal to 2
if len <= 2:
    #print error msg
    print("plz enter more than 2 characters..!!")

#else check if last two letters of string is 'ly'
elif str[-2:]=='ly':
    #print the string by default
    print(str)

#else check if last three letters are 'ing'
elif str[-3:]=='ing':
    #if true then add 'ly' at the end and print it
    str1 = str[:3] + 'ly'
    print(str1)

else:
    str += 'ing'
    print(str)
        

