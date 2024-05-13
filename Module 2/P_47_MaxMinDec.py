'''Python program to find the maximum and minimum numbers
from the specified decimal numbers'''
 
def maxmin(dec):

    max = dec[0]
    min = dec[0]

    for num in dec:

        if num > max:

            max = num

        elif num < min:

            min = num

    print("Maximum of Decimal:",max)
    print("Minimum of Decimal:",min)

dec = [20.5,17.8,9.9,15.4,2.5,22.3]

maxmin(dec)