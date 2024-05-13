'''Python program to find whether a given number is even or odd,
print out an appropriate message to the user.
even:2,4,6,8...
odd:1,3,5,7,9....
'''

num = int(input("Enter any number:"))

#check if number is less or equal to 0
if num<=0:
    #if true then print error msg
    print("Plz enter positive number..")

#otherwise check if reminder of number divisable by 2 is 0
elif num%2==0:
    #if true then print as even number
    print(num,"is even number")

else :
    #else print as odd number
    print(num,"is odd number")