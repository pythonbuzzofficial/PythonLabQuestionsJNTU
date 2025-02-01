"""
Write a function called merge that takes two already sorted lists of possibly different
lengths, and merges them into a single sorted list.
(a) Do this using the sort method. (b) Do this without using the sort method.
"""

def merge_with_sort_method(li1,li2):
    
    return sorted(li1+li2)
    

def merge_without_sort_method(li1,li2):
    
    li = li1+li2
    
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            
            if li[i] >li[j]:
                 li[i],li[j] = li[j],li[i]
                 
    return li
        
    
result1 = merge_with_sort_method([7,8,9],[3,4,5,6])
result2 = merge_without_sort_method([5,6,7,8],[1,2,3,4])
print("The merged list with using sort method:",result1)
print("The merged list without using sort method:",result2)

