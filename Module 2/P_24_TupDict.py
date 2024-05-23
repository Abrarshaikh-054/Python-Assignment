'''Python program to convert a list of tuples into a dictionary'''

#creat list of tuples with pair of two values
tup = [('python',1),('php',2),('asp',3)]

#take empty dictionary
dic = {}

#iterate through each tuples
for k,v in tup:
    #set key and values in dictionary using 'setdefault()' function
    dic.setdefault(k,[]).append(v)

#print tuple and dictionary
print("Tuple:",tup)
print("Dictionary:",dic)
