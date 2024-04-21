def uniq_ele(lst):

    u = []

    for i in lst:

        if i not in u:

            u.append(i)

    return u

lst = [10,11,11,22,22,33,44,44,55]

print("Original List:",lst)
print("New Unique List:",uniq_ele(lst))