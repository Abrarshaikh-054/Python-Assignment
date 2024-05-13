'''Python function that takes a list of words and returns the length
of the longest one'''

def find_longest(l):

    max_len = len(l[0])
    max_word = l[0]

    #run a loop through list item
    for i in l:
        #check if length of length of current word is greater than max variable
        if len(i) > max_len:
            #if true then store current word in max variable
            max_len = len(i)
            max_word = i

    print("The longest word:",max_word)
    print("The length :",max_len)

#l = ['hi','hello','how','are','you','by']

l = []

n = int(input("Enter number of list elements:"))

#run a for loop to accept number of list item from user
for i in range(1,n+1):

    print("Enter",i,"element:")
    ele = input()
    l.append(ele)

print(l)

find_longest(l)
    