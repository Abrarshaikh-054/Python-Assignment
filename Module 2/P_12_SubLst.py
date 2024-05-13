'''Python program to check whether a list contains a sub list '''

def isSubLst(ml,sl):

    flag = 0

    if(all(i in ml for i in sl)):

        flag = 1
    
    if flag:

        print(sl,"is sub list of",ml)
    
    else:

        print(sl,"is not a sub list of",ml)    


main_lst = [10,20,30,40,50,60,70]
sub_lst1 = [30,40,50]
sub_lst2 = [20,40,60]
sub_lst3 = [60,70,80] 
isSubLst(main_lst,sub_lst1)
isSubLst(main_lst,sub_lst2)
isSubLst(main_lst,sub_lst3)

