'''Python program to calculate surface volume and area of a cylinder'''

#define function which take height and radian
def cylinder(h,r):
    #take pi value as 22/7
    pi=22/7
    #apply the formula of surface volume and area of cylinder
    volum = pi*r*r*h
    sarea = (2*pi*r*h) + (2*pi*r*r)

    #print the result of calculation respectively
    print("Volume:",volum)
    print("Surface Area:",sarea)

#get the value of height and radian from user
h = float(input("Enter height of cylinder:"))
r = float(input("Enter radian of cylinder:"))

#call the function with height and radian
cylinder(h,r) 