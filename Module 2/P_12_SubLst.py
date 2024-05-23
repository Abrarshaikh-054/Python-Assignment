'''Python program to check whether a list contains a sub list '''

#define function which take two list as parameter
def isSubLst(ml,sl):
    #initialize 0 to flag
    flag = 0
    #check if all the items of sub list is present in main list
    if(all(i in ml for i in sl)):
        #if true then assign 1 to flag
        flag = 1

    #check if flag returns true
    if flag:
        #if yes then passed list is sublist
        print(sl,"is sub list of",ml)
    
    else:
        #if no then it is not a sublist
        print(sl,"is not a sub list of",ml)    

#create main list and sub list
main_lst = [10,20,30,40,50,60,70]
sub_lst1 = [30,40,50]
sub_lst2 = [20,40,60]
sub_lst3 = [60,70,80] 
#and call the function with main and sub lists
isSubLst(main_lst,sub_lst1)
isSubLst(main_lst,sub_lst2)
isSubLst(main_lst,sub_lst3)