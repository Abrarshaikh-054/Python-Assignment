'''Python program to get the Fibonacci series of given range.'''

'''fibonacci series is sequence of numbers in which each number is 
sum of two previous numbres
ex: 0,1,2,3,5,8....
'''

num = int(input("Enter any number:"))

#initalize 0 and 1 to two different variable  
n1=0
n2=1
#create additional count variable with value of zero
cnt=0

if num <=0:
    print("plz enter positive number...")

elif num==1:
    print("fibonacci series is",n1)

#run a while loop if number is not zero and one
else:
    print("fibonacci series:",end="")
    #run a while loop until cnt is samller than num
    while cnt<num:
        print(n1,end="")
        #create new variable with sum of two previous values
        n3=n1+n2

        #exchange the two previous values with next two values
        n1=n2
        n2=n3
        #increase the couting by 1
        cnt+=1