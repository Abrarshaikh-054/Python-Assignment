'''Python program to get the Factorial number of given number.'''

#The factorial of a number is the multiplication of all the integers from 1 to that number

#first take any integer number as input from user
num = int(input("Enter any number:"))

#initialy assign 1 to fact variable 
fact=1

#check if given number is less then zero
if num<0:
    #if true then print error msg
    print("plz enter positive number..")

#check if given number is equal to zero
elif num==0:
    #if true then print 1 as factorial of zero
    print("factorial of 0 is 1")

#run a for loop if number is number is not zero and negative
else:
    #for loop to find factorial of given number
    for i in range(1,num+1):
    #The factorial of a number is the multiplication of all the integers from 1 to that number
    #ex: fact of 5 is 1*2*3*4*5 =  120
        fact=fact*i
    print("the factorial of ",num,"is",fact) 