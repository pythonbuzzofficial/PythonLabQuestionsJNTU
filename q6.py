"""
Generate a random number between 1 and 10. Ask the user to guess the number and
print a message based on whether they get it right or not.
"""
import random

random_number = random.randint(1,10)
print(random_number)

guess = int(input("Guess a number between 1 to 10:"))

if random_number == guess:
    print("Congratulations,you guessed it right.")
else:
    print("Sorry,you guessed wrong.")