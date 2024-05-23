'''Python programe to print a dictionary where the keys are numbers
between 1 and 15'''

#take empty dictionary
dic = {}

#run a loop in range of 1 to 15
for i in range(1,16):
    #take each number as key and square of number as value
    dic[i] = i*i

#print the created dictionary
print(dic)