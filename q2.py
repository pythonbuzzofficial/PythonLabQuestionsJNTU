"""
Write a program that asks the user to enter three numbers (use three separate input
statements). Create variables called total and average that hold the sum and average of
the three numbers and print out the values of total and average.

input:
4
6
2
output:
Total:12.0
Average:4.0
"""
print("Enter three numbers")
var1 = int(input("Enter first number:"))
var2 = int(input("Enter second number:"))
var3 = int(input("Enter third number:"))
total = var1+var2+var3
average = total/3

print(f"Total:{total}")
print(f"Average:{average:.1f}")




