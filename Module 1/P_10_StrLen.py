def str_len(str):
    cnt = 0

    for ch in str:
        cnt+=1
    
    return cnt

str = input("Enter any string:")

print("Using for loop...")

print("The length of the string is",str_len(str))

print("Using length function...")

print("The length of the string is",len(str))



