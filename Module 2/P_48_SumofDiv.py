'''Python program to returns sum of all divisors of a number'''

#define a function which accepts number as parameter
def SumofDiviser(num):
    #take one variable to store divisors
    div = [1]
    #take second variable to store sum of divisors
    sum = 1

    #run a loop from 2 to the number given by user
    for i in range(2,num):
        #check if division of number and iterator return 0
        if num % i == 0 :
            #if true then append it in divisors list
            div.append(i)
            #and add it in sum of divisors
            sum += i
    
    #print the divisors and its sum
    print("Divisors of",num,":",div)
    print("Sum of Divisor:",sum)

#get the number from user to find sum of divisors
num = int(input("Enter number to find sum of divisors:"))

#call the function with the given number
SumofDiviser(num)  
    
    