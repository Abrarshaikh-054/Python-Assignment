'''Python program to count occurrences of a substring in a string'''
 
str = input("Enter any sentence:")

counts = {}

#split the senetence into words using split function
words = str.split()

#run a loop through each word
for i in words:
    
    #check if word is already in dictionary
    if i in counts:
        #if ture increase the count variable
        counts[i] += 1
    
    else:
        #if not assing initial value as
        counts[i] = 1

print(counts)