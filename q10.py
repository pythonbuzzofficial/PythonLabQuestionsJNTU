"""
Write a program that asks the user for a large integer and inserts commas into it
according to the standard American convention for commas in large numbers. For
instance, if the user enters 1000000, the output should be 1,000,000.
"""
num = int(input("Enter a large number"))

formatted = "{:,}".format(num)

print(formatted)
