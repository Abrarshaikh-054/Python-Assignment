num = int(input("Enter any number:"))

n1=0
n2=1
cnt=0

if num <=0:
    print("plz enter positive number...")

elif num==1:
    print("fibonacci sequence upto",num,"is",n1)

else:
    print("fibonacci series:")
    while cnt<=num:
        print(n1)
        n3=n1+n2

        n1=n2
        n2=n3
        cnt+=1