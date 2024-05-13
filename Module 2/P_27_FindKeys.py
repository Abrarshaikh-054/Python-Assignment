'''Python programe to check if a given key already exists in a
dictionary'''

def findkey(dic,key):

    if key in dic:

        print("key found with value:",dic[key])

    else:

        print("Key not found") 

dic = {1:'one',2:'two',3:'three',4:'four',5:'five'}

key = int(input("Enter key to found:"))

findkey(dic,key)



