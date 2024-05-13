'''Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. '''

def generateLst():

    lst = []

    for i in range(1,30):

        lst.append(i**2)
    
    print("First 5 elements:",lst[:5])
    print("Last 5 elements:",lst[-5:])

generateLst()