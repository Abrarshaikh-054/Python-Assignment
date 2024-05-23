'''Python programe to check if a given key already exists in a
dictionary'''

#define function which take dictionary and key as parameter
def findkey(dic,key):
    #check if key exist in dictionary
    if key in dic:
        #if true then print the value
        print("key found with value:",dic[key])

    else:
        #else print key not found
        print("Key not found") 

#create a dictionary with key and values
dic = {1:'one',2:'two',3:'three',4:'four',5:'five'}

#get key from user to find in dictionary
key = int(input("Enter key to found:"))

#call the function with key and dictionary
findkey(dic,key)



