d = {}

while True:
    menu = """
    Press 1 for signup
    Press 2 for login
    Press 3 for exit
    """
    print(menu)

    choice = int(input("Enter your choice:"))

    if choice==1:

        print("||","*"*30,"Signup form","*"*30,"||")

        email = input("enter your email:")
        name = input("enter your name:")
        mobile = int(input("enter mobile no:"))
        passw = input("enter your password:")
        cpass = input("confirm your password:")

        if passw == cpass:

            d['email']=email
            d['name']=name
            d['mobile']=mobile
            d['passw']=passw

            print("-"*20,"signup successfull...","-"*20)
        
        else:
            print("-"*20,"Paasword and confirm password must be same..!!","-"*20)

    elif choice==2:

        email = input("enter your email:")
        passw = input("enter your password:")

        if d['email']==email and d['passw']==passw:

            print("-"*20,"You are in control...","-"*20)

        else:
            print("-"*20,"User does not exist..!!","-"*20)
    
    elif choice==3:

        print("Thank for your precious time :)")
        break

    else:

        print("Invalid choice..!!")
        break



