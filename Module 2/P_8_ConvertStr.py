def convertstr(lst):

    new = ""

    for i in lst:

        new += i

    return new

lst = ['h','e','l','l','o']

str = "".join(lst)

print("Using join method:",str)

#print(convertstr(lst))

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = input()
    lst.append(item)

print("Original List:",lst)
print("Converted to String:",convertstr(lst))