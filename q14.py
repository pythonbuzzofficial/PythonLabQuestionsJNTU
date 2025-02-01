"""
 Write a program that generates 100 random integers that are either 0 or 1. Then find
the longest run of zeros, the largest number of zeros in a row. For instance, the longest
run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
"""

from random import randint

li =[]

for i in range(100):
     li.append(randint(0,1))
     
current = 0
longest = 0
for num in li:
    
    if num == 0:
        current+=1
        longest = max(current,longest)
    else:
        current =0
    

print(li)
print("The longest run of zeros :",longest)
