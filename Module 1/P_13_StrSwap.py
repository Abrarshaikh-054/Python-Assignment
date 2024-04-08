a = input("Enter first string:")
b = input("Enter second string:")

print("String before swapping :",a,",",b)

a1 =  b[:2] + a[2:]
b1 =  a[:2] + b[2:]

print("String after swapping :",a1,",",b1)

