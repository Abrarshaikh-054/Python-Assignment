'''Python function to check whether a number is perfect or not'''

#perfect number is positive integer that is equal to the sum of all its positive divisors
#example : 1+2+3 = 6

def Perfect_chk(n):
    #take sum variable and assign 0 
    sum = 0
    #run a loop from 1 to given number 
    for i in range(1,n):
        #check if reminder of number divided by each iterator is 0
        if n % i == 0:
            #if true then add divisior in sum variable
            sum += i

    #check if sum and number is equal
    if sum == n:
        #if true then print as perfect number
        print(n,"is a perfect number")
    
    else:
        #else its not perfect number
        print(n,"is not a perfect number")

n = int(input("Enter number to check perfect number:"))

Perfect_chk(n)