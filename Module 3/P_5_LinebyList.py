'''Python program to read a file line by line and store it into a list'''

#create a list with multiple strings
lst = ['Shaikh\n','Abrar\n','Ahemad\n']

#open a new file with write mode
file = open("Assig work\\Module 3\\Text Files\\text3.txt","w")

#write the content of list into file using 'writelines()' method
file.writelines(lst)

#open the same file again with the read mode
file = open("Assig work\\Module 3\\Text Files\\text3.txt","r")

#read the content of file using 'readlines()' method
lines = file.readlines()

#assign 1 to counter variable  
c = 1

#run a for loop to print the content line by line
for line in lines:

    print("Line",c,":",line)
    #increment counter by 1 after each line
    c+=1

file.close()
