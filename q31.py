'''
Write a Python class to reverse a string word by word.
'''

class StringReverser:
    def __init__(self,input_string):
        self.input_string = input_string
    
    def reverse_words(self):
        
        words = self.input_string.split()
        return ' '.join(words[::-1])
    
    
input = "Python is very easy programming language"   
reverser = StringReverser(input)

print(reverser.reverse_words())


