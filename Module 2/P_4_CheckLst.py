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

if check(lst1):

    print("The list is not empty:",lst1)

else:

    print("The list is empty",lst1)

lst1 = []

num = int(input("Enter the number of list items:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = int(input())
    lst1.append(item)

res = check(lst1)

if res == 0:

    print("This is empty list:",lst1)

else:

    print("This is not empty list",lst1)
    