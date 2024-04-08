print("Swapping using temp variable...")
x = 0
y = 0

x = int(input("Enter first value:"))
y = int(input("Enter second value:"))

print("Before swapping:x=",x,"y=",y)

temp = x
x = y
y = temp 

print("After Swapping:x=",x,"y=",y)
print("-----------------------------------")

print("Swapping without temp variable...")

x,y = y,x

print("x=",x)
print("y=",y)
