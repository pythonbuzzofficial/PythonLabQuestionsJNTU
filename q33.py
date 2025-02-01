'''
Write a program to demonstrate Try/except/else
'''

def divide_numbers():
    
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        result = num1/num2
    except ZeroDivisionError:
        print("Error: Cannont divide by zero")
    except Exception as e:
        print(e)
    else:
        print(f"The result of dividing {num1} and {num2} is {result}")    
    
divide_numbers()


