'''Python program to convert a list to a tuple'''
 
#get number of item user want to enter
num = int(input("Enter number of list item:"))

#create empty list
lst = []

#run a loop from 1 to defind number by user
for i in range(1,num+1):
    #take list items from user
    print("Enter item",i,":",end="")
    ele = input()
    #append every item into list
    lst.append(ele)
    #convert list into tuple using 'tuple()' function
    tup = tuple(lst)

#print list and converted tuple
print("Original List:",lst) 
print("Converted to tuple:",tup) 
