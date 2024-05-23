'''Python program to find the second smallest number in a list'''

#define function which take list as parameter
def find_num(lst):
    #find length of list
    l = len(lst)
    #create empty list to store unique numbers
    uniq = []
    #traverse throgh a list of numbers
    for i in lst:
        #check if number is not present in unique list
        if i not in uniq:
            #if true then add it to list
            uniq.append(i)

    #sort the unique list
    uniq.sort()

    #print specific numbers using indexing
    print("Unique Sorted List:",uniq)
    print("\nLargest number:",uniq[-1])
    print("Second largest:",uniq[-2])
    print("Smallest number:",uniq[0])
    print("Second Samllest:",uniq[1])

lst = [1,3,4,1,-2,-1,0,5]

find_num(lst) #call the function using pre-defined list

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = input()
    lst.append(item)

find_num(lst) #call the function using user-defined list
