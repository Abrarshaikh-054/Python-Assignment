n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

def test_num(x,y):

    if x==y:

        print(x,"is equal to",y)
        return True
    
    elif x+y==5:

        print("the sum of",x,"and",y,"is 5")
        return True
    
    elif x-y==5:

        print("The differnce between",x,"and",y,"is 5")
        return True
    
    else:

        print("none of the condition satisfied..!!")
        return False
    
print(test_num(n1,n2))