def join_str(str):

    if len(str) <= 2:
        return ''
    
    else:

        str1 = str[:2] + str[-2:]
        return str1
    
str = input("Enter any string:")

print(join_str(str))