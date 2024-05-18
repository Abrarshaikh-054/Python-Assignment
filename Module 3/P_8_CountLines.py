'''Python program to count the number of lines in a text file'''

#open existing file using read mode
file = open("Assig work\\Module 3\\Text Files\\text2.txt","r")

#read the lines using readlines() method
lines = file.readlines()

#initilize zero to count variable
cnt = 0

#run for loop through each lines
for line in lines:
    #increase the count by 1 for each line
    cnt += 1  #cnt = cnt + 1

#print the count variable 
print("The number of lines:",cnt)

file.close()


