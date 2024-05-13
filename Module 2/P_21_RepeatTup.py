'''Python program to find the repeated items of a tuple'''

tup = (1,2,3,3,4,4,7,9,1,1,3)

item = {}

for i in tup:

    if tup.count(i) > 1:

        item[i] = tup.count(i)
    
print(item)
        
