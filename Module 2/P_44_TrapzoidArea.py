'''Python program to calculate the area of a trapezoid'''

# trapezoid is a quadrilateral (four sided shape) which has one pair of sides as parallel 
 
def Trapzoid(b1,b2):
    
    h = float(input("Enter height:"))

    tarea = (b1+b2)/2*h
    tarea = (b1+b2)/2*h

    return tarea

b1 = float(input("Enter base 1:"))
b2 = float(input("Enter base 2:"))

res = Trapzoid(b1,b2)

print("Area of Trapzoid:",res)