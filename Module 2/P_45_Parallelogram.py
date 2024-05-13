'''Python program to calculate the area of a parallelogram'''

#parallelogram is a quadrilateral with two pairs of parallel sides

def parallelogram(base,height):

    area = base*height

    print("Area of parallelogram:",area)

base = int(input("Enter base:"))
height = int(input("Enter height:"))

parallelogram(base,height)
