'''Python program to print all unique values in a dictionary'''

#Create a list of dictionaries
mdl = [{'a':101},{'b':201},{'c':301},{'a':404},{'b':404},{'d':401}]

print(mdl) 

#get all the unique values from dictionary using line abbreviation and set() function
udl = set(val for v in mdl for val in v.values())

print(udl)

 