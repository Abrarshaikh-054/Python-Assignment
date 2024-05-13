'''Python program to check whether an element exists within a tuple'''

tup = ('A','b','r','a','r','0','5','4')

ele = input("Enter element to find:")

if ele in tup:

    print("Element exist in tuple")

else:

    print("Element does not exist")