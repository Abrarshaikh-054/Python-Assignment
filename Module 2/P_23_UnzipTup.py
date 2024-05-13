'''Python program to unzip a list of tuples into individual lists'''

lt = [(10,20,1),(30,40,2),(50,60,3)]

res = list(zip(*lt))

print(res)    
