'''Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''


def replace_str(str):

    #find the index of 'not' 'poor' and 'good' word and store it in variable
    inot = str.find('not')

    ipoor = str.find('poor')

    igood = str.find('good')

    #check if index of 'poor' is greater than 'not'
    if ipoor>inot and inot>0 and ipoor>0:

        #if true then replace 'not poor' with 'good' and return it  
        str = str.replace(str[inot:ipoor+4],'good')
        return str
    
    elif igood>inot and inot>0 and igood>0:

        str = str.replace(str[inot:igood+4],'poor')
        return str
    
    else:

        return str
    
str = input("Enter string with the word poor or good following not:")
res = replace_str(str)
print(res)