'''Python function that checks whether a passed string is palindrome or not'''

#palidrom is word or phrase that is readable as the same from backward and forward
#ex: mom,dad,madam

def palindrom(str):

    lp = 0
    rp = len(str) - 1

    while rp >= lp:

        if str[lp] != str[rp]:

            return False
        
        lp +=1
        rp -=1

    return True

str = input("Enter string to check palindrom:")

print(palindrom(str))