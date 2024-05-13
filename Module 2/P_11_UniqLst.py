'''Python program to get unique values from a list'''

def find_uniq(lst):

    uniq = []

    for i in lst:

        if i not in uniq:

            uniq.append(i)
        
    return uniq


lst = [11,24,32,11,45,32,30,24]

print("Original list:",lst)

print("Unique list:",find_uniq(lst))

    