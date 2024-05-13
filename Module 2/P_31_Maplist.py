'''Python program to map two lists into a dictionary'''

keys = ['apple','banana','graphs']
vals = ['red','yellow','green']

fruit = dict(zip(keys,vals))

print(fruit)