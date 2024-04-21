def count_str(words):

    cnt = 0

    for word in words:

        if len(word) >= 2 and word[0] == word[-1]:

            cnt += 1

    return cnt

print(count_str(['abc','xyz','cbc','545']))

lst = []

num = int(input("Enter number of list item:"))

for i in range(1,num+1):

    print("Enter item",i,":")
    item = input()
    lst.append(item)

print("The number of matching string:",count_str(lst))