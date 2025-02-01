"""
Write a function called is_sorted that is given a list and returns True if the list is
sorted and False otherwise.
"""


def is_sorted(li):
    
    
    return li == sorted(li)

print(is_sorted([1,2,3,4,5]))
