'''Python program to convert a tuple to a string'''

def Convert(tup):
		
	str = ''
	for i in tup:
		str = str + i
	return str


tup = ('A','B','R','A','R')
print("Tuple:",tup)
str = Convert(tup)
print("String:",str)
