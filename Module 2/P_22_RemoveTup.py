'''Python program to remove an empty tuple from a list of tuples'''

def remove(tup):
    for i in tup:
        if len(i) == 0:
            tup.remove(i)
    return tup

tup = [(10,20,30),(40,50,60),(),('a','b','c')]

print("Tuple before:",tup)
print("Tuple after:",remove(tup))