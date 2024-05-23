'''Python function that checks whether a passed string is palindrome or not'''

#palidrom is word or phrase that is readable as the same from backward and forward
#ex: mom,dad,madam

#define a function which take string as parameter
def palindrom(str):
    #take two pointer variable and point at right and left of string
    lp = 0
    rp = len(str) - 1

    #run a while loop till right pointer is greater or equal to left pointer
    while rp >= lp:
        #check if left pointer is not equal to right pointer
        if str[lp] != str[rp]:
            #if true then return false
            return False
        #else increment left pointer and decrement right pointer by 1
        lp +=1
        rp -=1

    return True

str = input("Enter string to check palindrom:")

print(palindrom(str))