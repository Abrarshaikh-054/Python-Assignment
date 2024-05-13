'''Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string'''

a = input("Enter first string:")
b = input("Enter second string:")

print("String before swapping :",a,",",b)

#take first two letters from second string and combine it with last letters of first string
a1 =  b[:2] + a[2:]
#take first two letters from first string and combine it with last letters of second string
b1 =  a[:2] + b[2:]

print("String after swapping :",a1,",",b1)

