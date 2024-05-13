'''Python programe to merge two Python dictionaries'''

def merge(dict1,dict2):
    
    dict1.update(dict2)

    return dict1

dict1 = {'AA':10,'BB':20}
dict2 = {'CC':30,'DD':40}

print(dict1)
print(dict2)

print(merge(dict1,dict2))