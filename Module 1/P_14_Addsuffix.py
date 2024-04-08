str = input("Enter any string:")

len = len(str)

if len <= 2:

    print("plz enter more than 2 characters..!!")

elif str[-2:]=='ly':

    print(str)

elif str[-3:]=='ing':
    str1 = str[:3] + 'ly'
    print(str1)

else:
    str += 'ing'
    print(str)
        

