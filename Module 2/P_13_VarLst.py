'''Python program to split a list into different variables'''

#create list of tuples
companies = [("Samsung","Apple","Vivo"),
          ("Dell","Lenovo","Hp"),
          ("Nikon","Canon","Sony")]

#take three diffrent variable and assign list inside it
var1,var2,var3 = companies

#print the all the variables sepratly
print("Mobiles:",var1)
print("Laptop:",var2)
print("Camera:",var3)