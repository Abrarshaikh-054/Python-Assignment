'''Python program to calculate the area of a parallelogram'''

#parallelogram is a quadrilateral with two pairs of parallel sides

#define function that accepts base and height value
def parallelogram(base,height):
    #multiply the the value of base with height and store in variable
    area = base*height
    #print the result stored in variable
    print("Area of parallelogram:",area)

#get base and height value from user
base = int(input("Enter base:"))
height = int(input("Enter height:"))

#call the function with base and height
parallelogram(base,height)
