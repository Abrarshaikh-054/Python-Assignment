'''Python function that takes a list and returns a new list with unique
elements of the first list '''

#define a function which take list and find unique element
def uniq_ele(lst):

    #create a empty list to store unique elements
    u = []

    #run a for loop through each elements
    for i in lst:
        #check if element is not present in unique list        
        if i not in u:
            #if true then append it to unique list
            u.append(i)

    return u

#create a list of duplicate elements
lst = [10,11,11,22,22,33,44,44,55]

#print original and unique elements of list
print("Original List:",lst)
print("New Unique List:",uniq_ele(lst))