'''Python program that will return true if the two given integer
values are equal or their sum or difference is 5'''

#define a function that takes two arguments
def test_num(x,y):

    #check if both numbers are same and return true
    if x==y:

        print(x,"is equal to",y)
        return True
    
    #else check if sum of two numbers is 5 and return true
    elif x+y==5:

        print("the sum of",x,"and",y,"is 5")
        return True
    
    #else check if diffrence of two numbers is 5 and return true
    elif x-y==5:

        print("The differnce between",x,"and",y,"is 5")
        return True
    
    #if no condition is matched print error msg and return false
    else:

        print("none of the condition satisfied..!!")
        return False
    
#take two values from user as input
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

#call the fuction with two given values
print(test_num(n1,n2))

