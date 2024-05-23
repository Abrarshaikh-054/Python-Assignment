'''Python program to unzip a list of tuples into individual lists'''

#creat a list of tuples
lt = [(10,20,1),(30,40,2),(50,60,3)]

#Unzip tuple with 'zip()' function
res = list(zip(*lt))

#print the unzip list
print(res)    
