'''Python program to convert a tuple to a string'''

#define a function which take tuple as parameter
def Convert(tup):
	#create a empty string
	str = ''
	#iterate through tuple
	for i in tup:
		#add each item of tuple in string
		str = str + i
	return str


tup = ('A','B','R','A','R')
print("Tuple:",tup)
str = Convert(tup)
print("String:",str)
