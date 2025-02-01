"""
Write a program that asks the user to enter a word and prints out whether that word
contains any vowels.
"""

vowels = "aeiouAEIOU"

word = input("Enter a word: ")

#Ctrat

for char in word:
    if char in vowels:
        print("Your word contains vowels.")
        break
else:
    print("Your word  doestn't contains vowels.")
        
        
    
    




    
        
    
    




