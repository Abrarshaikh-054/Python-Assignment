'''Python program to select an item randomly from a list'''

#import random module which select random item from list of items
import random

#create list of itmes
clr = ['Red','Green','Blue','Black','White']

#select random item from list and store it in variable
item = random.choice(clr)

#print the item stored in variable
print("Random item from list:",item)  

