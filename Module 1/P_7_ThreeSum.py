'''Python program to find sum of three given integers. However, if
two values are equal sum will be zero.'''

#take three values as input from user 
n1 = int(input("Enter First values:"))
n2 = int(input("Enter Second values:"))
n3 = int(input("Enter Third values:"))

#check if any two of value is equal to eachother
if n1==n2 or n2==n3 or n1==n3: 
    sum = 0  #sum will be zero if two values are equal
    print("Sum is",sum)

#else perform addition of three numbers and store in variable
else:
    sum = n1+n2+n3
    print("Sum of three is",sum)

