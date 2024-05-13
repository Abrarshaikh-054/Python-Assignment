'''Python program to calculate surface volume and area of a cylinder'''

def cylinder(h,r):

    pi=22/7
    volum = pi*r*r*h
    sarea = (2*pi*r*h) + (2*pi*r*r)

    print("Volume:",volum)
    print("Surface Area:",sarea)

h = float(input("Enter height of cylinder:"))
r = float(input("Enter radian of cylinder:"))

cylinder(h,r) 