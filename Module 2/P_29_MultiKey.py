'''Python program to check multiple keys exists in a dictionary'''

laptop = {
    'name':'Dell 5310',
    'ram' : '8 GB',
    'chip': 'intel i5',
    'card': 'nivida'
}

print(laptop.keys() >= {'name','ram'})
print(laptop.keys() >= {'chip','rom'})

