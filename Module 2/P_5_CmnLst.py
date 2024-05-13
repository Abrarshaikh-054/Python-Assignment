'''Python function that takes two lists and returns true if they have
at least one common member.'''

def comn_lst(ls1,ls2):

    res = False
    cmn = []

    for a in ls1:

        for b in ls2:

            if a==b:
                
                res = True
                
                cmn.append(a)

                return res,cmn
    return res,cmn

lst1 = [10,22,20,44,30]
lst2 = [12,23,19,44,31]
lst3 = [11,21,31,41,51]
lst4 = [12,22,32,42,52]

res1,cmn1 = comn_lst(lst1,lst2)
res2,cmn2 = comn_lst(lst3,lst4)

print(res1,":",cmn1)
print(res2,":",cmn2)
