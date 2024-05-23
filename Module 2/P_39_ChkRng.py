'''Python function to check whether a number is in a given range'''

#define function that accepts range and number to check
def chk_num(n,start,end):
    #check if number is part of given range
    if n in range(start,end):
        #if true then print msg
        print(n,"is in the range of",start,"to",end)

    else:

        print(n,"is not in range")

#take starting ending and number values from user
start = int(input("Enter starting of range:"))
end = int(input("Enter ending of range:"))
num = int(input("Enter number to check:"))

#call the functions with taken arguments
chk_num(num,start,end)