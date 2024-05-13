'''python program that swap two number with temp variable and
without temp variable.'''

print("Swapping using temp variable...")
#first initialize two variable with zero
x = 0
y = 0

#take two numbers from user
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

#print before swapping
print("Before swapping:x=",x,"y=",y)

#swap the numbers using temp variable
temp = x
x = y
y = temp 

#print after swapping
print("After Swapping:x=",x,"y=",y)
print("-----------------------------------")

print("Swapping without temp variable...")

x,y = y,x

print("x=",x)
print("y=",y)
