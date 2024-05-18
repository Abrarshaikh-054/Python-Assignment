'''python program that allow user to enter only odd numbers else will raise an exception'''

#define custom exception by creating a new class derived from built in exception class
class NotOddNumber(Exception):
    pass

#define logic in try block
try:
    #take number from user
    num = int(input("Enter only odd number:"))
    
    #check if reminder of number is not equal to 0 
    if num % 2 != 0:
        #if yes then it is odd number so return true
        print(True)
    else: 
        #else raise 'NotOddNumber' exception with number given by user
        raise(NotOddNumber(num))

#define except block with error msg and value
except NotOddNumber as e: 

    print(e,"is not a odd number")

