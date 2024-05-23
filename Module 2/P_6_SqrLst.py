'''Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. '''

#define a function to generate a list
def generateLst():
    #create a empty list
    lst = []
    #run a for loop in range of 1 to 30
    for i in range(1,31):
        #perform square operation and append number in list
        lst.append(i**2)
    
    #print first and last 5 numbers using slicing method
    print("First 5 elements:",lst[:5])
    print("Last 5 elements:",lst[-5:])

generateLst()