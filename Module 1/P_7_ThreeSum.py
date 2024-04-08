n1 = int(input("Enter First values:"))
n2 = int(input("Enter Second values:"))
n3 = int(input("Enter Third values:"))

print("First value:",n1)
print("Second value:",n2)
print("Third value:",n3)

if n1==n2 or n2==n3 or n1==n3: 
    sum = 0  #sum will be zero if two values are equal
    print("Sum is",sum)

else:
    sum = n1+n2+n3
    print("Sum of three is",sum)

