"""
 Write a function called number_of_factors that takes an integer and returns how many
factors the number has.
"""
def number_of_factors(number):
     
    factors=[]
    for i in range(1,number+1):
        if number%i ==0:
            factors.append(i)
        
    return factors
      
     
number = int(input("Enter a number to find its factors:"))

factors = number_of_factors(number)

print(f"The factors of given number{number} is {factors}")



