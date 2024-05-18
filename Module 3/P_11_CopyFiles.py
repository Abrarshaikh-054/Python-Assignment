''' Python program to copy the contents of a file to another file '''

#open the first file with the read mode
file1 = open("Assig work\\Module 3\\Text Files\\text9.txt","r")

#open the second file with the append mode
file2 = open("Assig work\\Module 3\\Text Files\\text8.txt","a")

file2.write('\n-------------------------\n')
#iterate through content of file1 and write it in file2
for line in file1:
    file2.write(line)

#open file2 with the read mode
file2 = open("Assig work\\Module 3\\Text Files\\text8.txt","r")

#read all the content and print it 
txt = file2.read()

print(txt)

