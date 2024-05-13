'''Python program to check if a number is positive, negative or
zero.'''

#first take any integer number as input from user
n = int(input("Enter any number:")) 

#check if given number is greater than zero
if n>0:
    #if condition is true then print it as positive number
    print(n,"is positive number")

#check if given number is less than zero
elif n<0:
    #if condition is true then print it as negative number
    print(n,"is negative number")

else:
    #if no condition matched then print it as zero number
    print("number is zero")  