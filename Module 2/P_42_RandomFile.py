'''Python program to read a random line from a file'''

import random

file = open("Assig work\\Module 2\\text1.txt")

lines = file.read().splitlines()

print(random.choice(lines))

