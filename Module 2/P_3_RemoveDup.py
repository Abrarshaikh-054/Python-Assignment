def remove(lst):

    final = []

    for l in lst:

        if l not in final:

            final.append(l)

    return final

lst = [10,20,10,30,20,40,30,50]

print("List before:",lst)
print("List after:",remove(lst))

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = int(input())
    lst.append(item)

print("Original list:",lst)
print("Final list:",remove(lst))