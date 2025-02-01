"""
Write a program that asks the user for their name and how many times to print it. The
program should print out the user’s name the specified number of times.

input:
What is your name? python_buzz
How many times would you like to repeat? 3

output:
python_buzz
python_buzz
python_buzz

"""
name = input("What is your name? ")
repeat = int(input("How many times would you like to repeat?"))
print((name+"\n")*repeat)




