'''Python program to get unique values from a list'''

#define function that take list parameter
def find_uniq(lst):
    #create empty unique list
    uniq = []
    #traverse through list items
    for i in lst:
        #check if item is not present in uniqe list
        if i not in uniq:
            #if true then add it to unique list
            uniq.append(i)
        
    return uniq


lst = [11,24,32,11,45,32,30,24]

print("Original list:",lst)

print("Unique list:",find_uniq(lst))

    