def middle_str(str,word):

    mid = int(len(str)/2)
    
    #print(len(str))
    #print(mid)

    str1 = str[:mid] + word + str[mid:]

    return str1

#print(middle_str('shaikh ahemad','abrar'))

str = input("enter any string:")
word = input("enter middle word:")
print(middle_str(str,word))


