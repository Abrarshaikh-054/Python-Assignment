'''Python programe to concatenate three dictionaries to create a
new one.'''

dic1 = {'AA':11,'BB':22}
dic2 = {'CC':33,'DD':44}
dic3 = {'EE':55,'FF':66}

dic4 = {}

for i in dic1,dic2,dic3:

    dic4.update(i)

print("\n",dic1,"\n",dic2,"\n",dic3)

print("\n",dic4)