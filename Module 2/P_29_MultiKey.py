'''Python program to check multiple keys exists in a dictionary'''

#create a dictionary with key and value pair
laptop = {
    'name':'Dell 5310',
    'ram' : '8 GB',
    'chip': 'intel i5',
    'card': 'nivida'
}

#compare if dictionary has two or more keys and return the boolean value
print(laptop.keys() >= {'name','ram'})
print(laptop.keys() >= {'chip','rom'})

