def replace_str(str):

    inot = str.find('not')

    ipoor = str.find('poor')

    igood = str.find('good')

    if ipoor>inot and inot>0 and ipoor>0:

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