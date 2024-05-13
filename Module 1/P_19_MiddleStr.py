'''Write a Python function to insert a string in the middle of a string'''

#define a function which take two arguments
def middle_str(str,word):
    #find middle of string and store it in variable
    mid = int(len(str)/2)
    
    #insert a string at middle using slicing method
    str1 = str[:mid] + word + str[mid:]

    return str1

#print(middle_str('shaikh ahemad','abrar'))

str = input("enter any string:")
word = input("enter middle word:")
print(middle_str(str,word))


