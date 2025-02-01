"""
 Write a program that removes any repeated items from a list so that each item appears
at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
"""

li = [1,1,2,3,4,3,0,0]

unique_list = list(dict.fromkeys(li))

print(unique_list)

