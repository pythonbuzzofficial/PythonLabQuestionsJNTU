"""
Write a program that reads a file consisting of email addresses, each on its own line.
Your program should print out a string consisting of those email addresses separated
by semicolons.
"""

file_path = "emails.txt"

with open(file_path,"r") as file:
    
    emails = [line.strip() for line in file]
    
    print(";".join(emails))