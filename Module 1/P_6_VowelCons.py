'''Python program to test whether a passed letter is a vowel or
not.

Vowels is a,e,i,o,u and rest of alphabets are consonents
'''

ch = input("Enter any alphabet from A to Z:")

#check if given letter is present in vowels
if ch in('a','e','i','o','u','A','E','I','O','U'):
    #if true print as vowles
    print(ch,"is vowel..")

else:
    #else print as consonent
    print(ch,"is consonent..")
