def find_longest(l):

    max_len = len(l[0])
    max_word = l[0]

    for i in l:

        if len(i) > max_len:

            max_len = len(i)
            max_word = i

    print("The longest word:",max_word)
    print("The length :",max_len)

#l = ['hi','hello','how','are','you','by']

l = []

n = int(input("Enter number of list elements:"))

for i in range(1,n+1):

    print("Enter",i,"element:")
    ele = input()
    l.append(ele)

print(l)

find_longest(l)
    