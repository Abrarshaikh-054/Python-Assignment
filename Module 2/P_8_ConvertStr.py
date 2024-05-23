'''Python program to convert a list of characters into a string'''

#define a function to convert character list into string
def convertstr(lst):
    #create empty string
    new = ""
    #iterate through each character in list 
    for i in lst:
        #assign each character in empty string
        new += i

    return new

#create list of characters
lst = ['h','e','l','l','o']

#directly create string using join method
str = "".join(lst)

print("Using join method:",str)

#getting list of character from user and converting it to string

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = input()
    lst.append(item)

print("Original List:",lst)
print("Converted to String:",convertstr(lst))