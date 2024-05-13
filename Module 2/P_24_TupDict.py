'''Python program to convert a list of tuples into a dictionary'''

tup = [('python',1),('php',2),('asp',3)]

dic = {}

for k,v in tup:

    dic.setdefault(k,[]).append(v)

print("Tuple:",tup)
print("Dictionary:",dic)
