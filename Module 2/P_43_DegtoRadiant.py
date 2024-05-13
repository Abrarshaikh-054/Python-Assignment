'''Python program to convert degree to radian'''

def degree(val):

    pi = 22/7
    rad = val*pi/180

    return rad

val = int(input("Enter value in degree:"))

res = degree(val)

print("Radian:",res)