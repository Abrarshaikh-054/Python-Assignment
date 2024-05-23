'''Python program to map two lists into a dictionary'''

#create two diffrent lists
keys = ['apple','banana','graphs']
vals = ['red','yellow','green']

#merge two list into dictionary using zip() function
fruit = dict(zip(keys,vals))

print(fruit)