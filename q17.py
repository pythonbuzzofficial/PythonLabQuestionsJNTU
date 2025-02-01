"""
Write a function called sum_digits that is given an integer num and returns the sum of
the digits of num
"""
#num = 12345 1+2+3+4+5 = 15

def sum_digits(num):
    
    total = sum(int(i) for i in str(num))
    
    return total
    


num = int(input("Enter a number:"))

print(sum_digits(num))
