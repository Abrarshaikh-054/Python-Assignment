'''Python program to find the repeated items of a tuple'''

#create tuple with duplicate items
tup = (1,2,3,3,4,4,7,9,1,1,3)

#create empty dictionary
item = {}

#traverse through each item of tuple
for i in tup:
    #check if count of item is greater then 1
    if tup.count(i) > 1:
        #if true then count the occurence of item and store it in dictionary as value
        item[i] = tup.count(i)

#print the item dictionary
print(item)
        
