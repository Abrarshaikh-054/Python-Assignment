'''Python program to convert degree to radian'''

def Radian(val):
    #take pi value as 22/7
    pi = 22/7
    #apply formula of radiant
    rad = val*pi/180
    #return value of radian
    return rad

#take user input in degree
val = int(input("Enter value in degree:"))
#call the function with given value
res = Radian(val)

print("Radian:",res)