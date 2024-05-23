'''Python programe to merge two Python dictionaries'''

#define a function which take two dictionary as parameter
def merge(dict1,dict2):
    #merge two dictionary using update function
    dict1.update(dict2)
    #return updated dictionary
    return dict1

#create two diffrent dictionary
dict1 = {'AA':10,'BB':20}
dict2 = {'CC':30,'DD':40}

print(dict1)
print(dict2)

#call the function with two dictionaries
print(merge(dict1,dict2))