'''Python function that takes two lists and returns true if they have at least one common member.'''

#define a functin which take two list as parameters
def comn_lst(ls1,ls2):

    #intilize result as false
    res = False
    #create a empty list to store common members
    cmn = []

    #run a nested for loop through each itmes of list 1 and list 2
    for a in ls1:
        
        for b in ls2:
            #compare each item of list 1 to every item of list 2
            if a==b:
                #if both are eqaul then assign true in result 
                res = True
                #and append item in commom list
                cmn.append(a)

    return res,cmn

#create list of members to compare
lst1 = [10,22,20,44,30]
lst2 = [12,23,21,44,31]
lst3 = [11,21,31,41,51]
lst4 = [12,22,32,42,52]

#call defined function with two list as argumets
res1,cmn1 = comn_lst(lst1,lst2)
res2,cmn2 = comn_lst(lst3,lst4)

#print the result and common member if any
print(res1,":",cmn1)
print(res2,":",cmn2)
