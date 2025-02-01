"""
In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or
3(x+5). Computers prefer those expressions to include the multiplication symbol, like
3*x+4*y or 3*(x+5). Write a program that asks the user for an algebraic expression
and then inserts multiplication symbols where appropriate.
"""
#possibilities
# Add * between a number and a variable (e.g., 3x -> 3*x)
# Add * between a variable and an opening parenthesis (e.g., x( -> x*()  x(y+5)
# Add * between a number and an opening parenthesis (e.g., 3( -> 3*())
# Add * between a closing parenthesis and a variable (e.g., )x -> )*x)   (x+5)y
# Add * between a closing parenthesis and a number (e.g., )x -> )*x)   (x+5)10
# Add * between two parentheses (e.g., )( -> )*())    (x+5)(y+7)

import re

def add_multiplication(expression):
     
     #re.sub(pattern,replacement,string)
     expression = re.sub(r'(\d)([a-zA-Z])',r'\1*\2',expression)
     expression = re.sub(r'([a-zA-Z])(\()',r'\1*\2',expression)
     expression = re.sub(r'([\d])(\()',r'\1*\2',expression)
     expression = re.sub(r'(\))([a-zA-Z])',r'\1*\2',expression)
     expression = re.sub(r'(\))(\d)',r'\1*\2',expression)
     expression = re.sub(r'(\))(\()',r'\1*\2',expression)
    
     return expression


expression = input("Enter a algebric expression: ")
result = add_multiplication(expression)
print(result)