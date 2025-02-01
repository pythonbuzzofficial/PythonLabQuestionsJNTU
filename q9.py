"""
Write a program that asks the user to enter two strings of the same length. The
program should then check to see if the strings are of the same length. If they are not,
the program should print an appropriate message and exit. If they are of the same
length, the program should alternate the characters of the two strings. For example, if
the user enters abcde and ABCDE the program should print out AaBbCcDdEe.

input:
python_buzz
PYTHON_BUZZ

output:
pPyYtThHoOnN__bBuUzZzZ
"""
str1 =input("Enter first string: ")
str2 =input("Enter second string: ")

if len(str1) == len(str2):
    for s1,s2  in zip(str1,str2):
        
        print(s1+s2,end="")
else:
    print("Given two strings are not of same length.")
    


