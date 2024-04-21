def maxele(lst):

    max = lst[0]

    for i in lst:

        if i > max:
            max = i

    return max

def minele(lst):

    min = lst[0]

    for i in lst:

        if i < min:
            min = i 
    
    return min

def sumele(lst):

    sum = 0

    for i in lst:

        sum = sum + i

    return sum

lst = []

num = int(input("Enter number of list elements:"))

for i in range(1,num+1):
    print("Enter element",i,":",end="")
    ele = int(input())
    lst.append(ele)

print("The list:",lst)
print("The largest element:",maxele(lst))
print("The smallest element:",minele(lst))
print("Sum of all element:",sumele(lst))