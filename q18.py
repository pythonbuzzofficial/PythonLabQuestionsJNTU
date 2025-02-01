"""
 Write a function called first_diff that is given two strings and returns the first location
in which the strings differ. If the strings are identical, it should return -1.
"""

def first_diff(str1,str2):

         min_length = min(len(str1),len(str2))
         
         for i in range(min_length):
             
             if str1[i]!=str2[i]:
                 
                   return i
         if str1!=str2:     
               
             return min_length      
         else:
            return -1

str1 = "hello"

str2 ="helo"

result = first_diff(str1,str2)

print("The first difference is at index:",result)