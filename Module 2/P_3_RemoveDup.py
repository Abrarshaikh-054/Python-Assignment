'''Python program to remove duplicates from a list'''

#define a function to remove duplicate item
def remove(lst):
    #create a empty list to store uniqe items only
    final = []

    for l in lst:
        #check if item is not present in list
        if l not in final:
            #if true only then add it to list
            final.append(l)

    return final

#create a list with duplicate items
lst = [10,20,10,30,20,40,30,50]

print("List before:",lst)
print("List after:",remove(lst))

lst = []

num = int(input("Enter number of list item:"))

#to take number of list items from user
for i in range(1,num+1):

    print("Enter item",i,":")
    item = int(input())
    lst.append(item)

print("Original list:",lst)
print("Final list:",remove(lst))