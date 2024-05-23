'''Python program to reverse a tuple'''

#create tuple of characters
tup=('a','b','c','d','e')

#reverse it using 'reversed()' function
rtup = reversed(tup)

#print original and reversed function
print("Original:",tup)
print("Reversed:",tuple(rtup))