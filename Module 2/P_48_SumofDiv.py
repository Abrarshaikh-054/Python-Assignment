'''Python program to returns sum of all divisors of a number'''

def SumofDiviser(num):

    div = [1]
    sum = 1

    for i in range(2,num):

        if num % i == 0 :

            div.append(i)
            sum += i
         
    print("Divisors of",num,":",div)
    print("Sum of Divisor:",sum)

num = int(input("Enter number to find sum of divisors:"))

SumofDiviser(num)  
    
    