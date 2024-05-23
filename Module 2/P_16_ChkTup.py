'''Python program to check whether an element exists within a tuple'''

#create a tuple with list of elements
tup = ('A','b','r','a','r','0','5','4')
#get element from user which is to be found
ele = input("Enter element to find:")
#check if element exist in tuple
if ele in tup:
    
    print("Element exist in tuple")

else:

    print("Element does not exist")