'''Python function to reverses a string if its length is a multiple of 4'''

def reverse_str(str):

    if len(str) % 4 == 0:

        return ''.join(reversed(str))
    
    else:

        print("string is not reversable..!!")
        return str
        
    
str = input("Enter string divisible by 4:")

print(reverse_str(str))