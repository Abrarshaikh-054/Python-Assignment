'''Python program to read a random line from a file'''

import random

#open text file with read mode
file = open("Assig work\\Module 2\\text1.txt","r")

#read lines in variable using 'read()' function
lines = file.read().splitlines()

#choose random line using random() method
print(random.choice(lines))

