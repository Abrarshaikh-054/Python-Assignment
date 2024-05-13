'''Python program to count the number of characters (character
frequency) in a string '''

str = input("Enter any string:")

#create empty dictionary
dict = {}

#run a loop to through each character in given string
for i in str:
    
    #check if letter is already in dictionary
    if i in dict:
        #if true incrase the value by 1
        dict[i] += 1
    
    else:
        #if not then assign 1 as value
        dict[i] = 1
    
print(dict)