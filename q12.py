"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
"""

from random import randint

li = []

for i in range(20):
    li.append(randint(1,100))
    
print("Random list",li)
print("The average of the elements in the list:", sum(li)/len(li))
print(f"The largest value is {max(li)} and the smallest value is {min(li)}")
sorted_list = sorted(li)
print(f"The second largest value is {sorted_list[-2]} and the second smallest value is {sorted_list[1]}")
print(f"There are {len([i for i in li if i%2==0])} even numbers are in the list")
