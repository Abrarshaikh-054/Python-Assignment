'''python program to find sum of first n positive integers'''

#take positive number from user
n = int(input("Enter positive number:"))

#find the sum of first n numbers with given fromula and store it in variable
sum = (n*(n+1)/2)

#print the variable 
print("Sum of the first",n,"positive numbers is",sum)