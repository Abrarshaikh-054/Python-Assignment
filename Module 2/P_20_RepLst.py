'''Python program to replace last value of tuples in a list'''

lst = [10,20,30,40,50]

l = len(lst)

print("Original:",lst)

for i in range(1,l):

    if i == l-1:
        
        lst[i] = 60
        print("Replaced:",lst)


