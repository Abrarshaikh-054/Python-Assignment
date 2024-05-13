'''Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings'''

def count_str(words):

    cnt = 0

    for word in words:     
        #check if length of word is greater or equal to two and first and last char is same
        if len(word) >= 2 and word[0] == word[-1]: 
            #if true then increase count by 1
            cnt += 1

    return cnt
  
print("The number of matching string:",count_str(['abc','xyz','cbc','545'])) 

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = input()
    lst.append(item)

print("The number of matching string:",count_str(lst))