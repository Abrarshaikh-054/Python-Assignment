'''Python function to check whether a number is in a given range'''

def chk_num(n,start,end):

    if n in range(start,end):

        print(n,"is in the range of",start,"to",end)

    else:

        print(n,"is not in range")

start = int(input("Enter starting of range:"))
end = int(input("Enter ending of range:"))
num = int(input("Enter number to check:"))

chk_num(num,start,end)