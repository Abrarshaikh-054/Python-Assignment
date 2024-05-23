'''Python program to find the maximum and minimum numbers
from the specified decimal numbers'''

def maxmin(dec):

    #take two variable and assign first value of list as max and min
    max = dec[0]
    min = dec[0]
    
    #traverse through each number of list
    for num in dec:
        #check if number is greater than max
        if num > max:
            #if true than assign it as max
            max = num
        #else check if number is less than min
        elif num < min:
            #if true than assign it as min
            min = num

    #print the max and min number
    print("Maximum of Decimal:",max)
    print("Minimum of Decimal:",min)

dec = [20.5,1.54,17.8,9.9,15.4,2.5,22.4]

maxmin(dec)