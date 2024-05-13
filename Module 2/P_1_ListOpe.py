'''Python function to get the largest number, smallest num and sum
of all from a list'''

#define function to get largest number
def maxele(lst):

    max = lst[0]

    for i in lst:

        if i > max:
            max = i

    return max

#define function to get smallest number
def minele(lst):

    min = lst[0]

    for i in lst:

        if i < min:
            min = i 
    
    return min

#define function to get sum of all numbers
def sumele(lst):

    sum = 0

    for i in lst:

        sum = sum + i

    return sum

lst = []

num = int(input("Enter number of list elements:"))

#run a for loop to get number of list item from user
for i in range(1,num+1):
    print("Enter element",i,":",end="")
    ele = int(input())
    lst.append(ele)

print("The list:",lst)
print("The largest element:",maxele(lst))
print("The smallest element:",minele(lst))
print("Sum of all element:",sumele(lst))
