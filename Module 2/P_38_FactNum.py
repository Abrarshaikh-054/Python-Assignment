'''Python function to calculate the factorial of a number '''

#define a function which take number to calculate factorial
def fact(n):
    #check if number is 0
    if n == 0:
        #if true then return 1
        return 1
    
    else:
        #else find factorial using recursion of function
        return n*fact(n-1)
    
n = int(input("Enter number to find factorial:"))

res = fact(n)

print("Factorial of",n,"is",res)

 