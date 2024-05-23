'''program to check a list is empty or not.'''

#define a function to check empty list
def check(lst):
    #check if length of the list is equal to zero
    if len(lst) == 0:
        #if true then return zero as it is empty list
        return 0
    else:
        #else return one as it is not a empty list
        return 1

lst1 = [10,20,30,40]

#call the 'check()' fucntion with 'lst1' 
if check(lst1):
    #if true then then print as not empty list
    print("The list is not empty:",lst1)

else:
    #else print as empty list
    print("The list is empty",lst1)

'''checking empty list with user defined itmes'''

lst1 = [] #create empty list 

#get number of item user want to enter in list
num = int(input("Enter the number of list items:"))

#run a for loop till given number by user and append each item in list
for i in range(1,num+1):

    print("Enter item",i,":")
    item = int(input())
    lst1.append(item)

#call the 'check() function with lst1 and store result'
res = check(lst1)

#check if result is equal to 0
if res == 0:
    #if true then it is empty list
    print("This is empty list:",lst1)

else:
    #else print as not empty list
    print("This is not empty list",lst1)
    