'''Python program to calculate the area of a trapezoid'''

#trapezoid is a quadrilateral (four sided shape) which has one pair of sides as parallel 
 
#define a function which accepts two base value
def Trapzoid(b1,b2):
    #take height from the user
    h = float(input("Enter height:"))
    #apply the formula to find area of trapzoid
    tarea = (b1+b2)/2*h

    return tarea

#get two base values from users
b1 = float(input("Enter base 1:"))
b2 = float(input("Enter base 2:"))

#call the function with given base values
res = Trapzoid(b1,b2)

print("Area of Trapzoid:",res)