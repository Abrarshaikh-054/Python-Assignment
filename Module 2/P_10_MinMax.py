'''Python program to find the second smallest number in a list'''

def find_num(lst):

    l = len(lst)

    uniq = []

    for i in lst:

        if i not in uniq:

            uniq.append(i)
    
    uniq.sort()

    print("Unique Sorted List:",uniq)
    print("\nLargest number:",uniq[-1])
    print("Second largest:",uniq[-2])
    print("Smallest number:",uniq[0])
    print("Second Samllest:",uniq[1])

lst = [1,3,4,1,-2,-1,0,5]

find_num(lst)

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = input()
    lst.append(item)

find_num(lst)
