'''Python program to remove an empty tuple from a list of tuples'''

#define a fucntion that take tuple as parameter
def remove(tup):
    #traverse through list of tuple
    for i in tup:
        #check if length of tuple is equal to 0
        if len(i) == 0:
            #if true then remove it
            tup.remove(i)
    return tup

#creat multiple tuples in list
tup = [(10,20,30),(40,50,60),(),('a','b','c')]

#print the tuples before and after removing
print("Tuple before:",tup)
print("Tuple after:",remove(tup))