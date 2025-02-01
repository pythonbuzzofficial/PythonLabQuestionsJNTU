"""
Write a program that asks the user for two numbers and prints Close if the numbers
are within .001 of each other and Not close otherwise.
"""
num1 =  float(input("Enter first number:"))

num2 = float(input("Enter second number:"))

sum = round(abs(num1-num2),3)
print(sum)
if sum<=0.001:
    print("close")
else:
    print("not close")

