'''Python program to calculate the length of a string.'''

#define a function that take string as argument and return length
def str_len(str):
    cnt = 0

    #run a for loop through a string
    for ch in str:
        #increase the count variable by 1 for every character in string
        cnt+=1
    
    return cnt

str = input("Enter any string:")

print("Using for loop...")

print("The length of the string is",str_len(str))

print("Using length function...")

print("The length of the string is",len(str))



