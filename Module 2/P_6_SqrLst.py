def generateLst():

    lst = []

    for i in range(1,30):

        lst.append(i**2)
    
    print("First 5 elements:",lst[:5])
    print("Last 5 elements:",lst[-5:])

generateLst()