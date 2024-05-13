'''Python program to convert a list to a tuple'''

num = int(input("Enter number of list item:"))

lst = []

for i in range(1,num+1):

    print("Enter item",i,":",end="")
    ele = input()
    lst.append(ele)
    tup = tuple(lst)

print("Original List:",lst)
print("Converted to tuple:",tup)