'''Python function to check whether a number is perfect or not'''

#perfect number is positive integer that is equal to the sum of all its positive divisors
#example : 1+2+3 = 6

def Perfect_chk(n):

    sum = 0


    for i in range(1,n):

        if n % i == 0:

            sum += i

    if sum == n:

        print(n,"is a perfect number")
    
    else:

        print(n,"is not a perfect number")

n = int(input("Enter number to check perfect number:"))

Perfect_chk(n)