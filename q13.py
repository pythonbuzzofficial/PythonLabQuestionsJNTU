"""
Write a program that asks the user for an integer and creates a list that consists of the
factors of that integer.
"""

number = int(input("Enter a number to find its factors:"))

factors = []

for i in range(1,number+1):
    
    if number%i ==0:
        factors.append(i)
        
print(f"The factors of given number {number} is {factors}")
    
    

     
        
        
        
    