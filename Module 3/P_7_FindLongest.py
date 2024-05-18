''' python program to find the longest words '''

#open a new text file with 'w+' method
file = open("Assig work\\Module 3\\Text Files\\text5.txt","w+")

#get any string from user
txt = input("Enter any string:")

#write the string to text file 
file.write(txt)

#point at the begining of file
file.seek(0)

#read and split the content of file 
lines = file.read().split()

#take the first word as max
max = lines[0]

#run for loop through each word
for line in lines:
    #check if length of the current word is larger than max word
    if len(line) > len(max):
        #if true then store it in max variable
        max = line

#print the longest word
print("Longest word:",max)

file.close()

