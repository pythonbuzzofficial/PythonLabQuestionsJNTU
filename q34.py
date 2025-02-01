'''
 Write a program to demonstrate try/finally and with/as
'''

def try_finally_example():
    
    try:
        x = 10/0
        print(x)
    except Exception as e:
        print(e)
        
    finally:
        print("This finally block will always executed")
    
try_finally_example()

with open("example.txt","r") as file:
    
    print(file.read())


    
    