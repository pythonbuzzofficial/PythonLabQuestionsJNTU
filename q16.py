"""
Write a program that asks the user to enter a length in feet. The program should then
give the user the option to convert from feet into inches, yards, miles, millimeters,
centimeters, meters, or kilometers. Say if the user enters a 1, then the program
converts to inches, if they enter a 2, then the program converts to yards, etc. While
this can be done with if statements,it is much shorter with lists and it is also easier to
add new conversions if you use lists.
"""

feet = float(input("Enter a length in feet"))

print("""
 1 -> feet to inch
 2 -> feet to yards
 3 -> feet to mile
 4 -> feet to millimeters
 5 -> feet to centimeters
 6 -> feet to meters
 7 -> feet to kilometers

""")
option = int(input("Choose a coversion:"))

li =[
    lambda x:x*12,
    lambda x:x*0.333,
    lambda x:x*0.00018939,
    lambda x:x*304.8,
    lambda x:x*30.48, 
    lambda x:x*0.3048,
    lambda x:x*0.0003048,

    ]

print(li[option-1](feet))