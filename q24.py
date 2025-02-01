"""
Write a program that asks the user for a word and finds all the smaller words that can
be made from the letters of that word. The number of occurrences of a letter in a
smaller word can’t exceed the number of occurrences of the letter in the user’s word
"""

from itertools import permutations

def smaller_words(word):
    words_set = set()
    for i in range(1,len(word)):
        for perm in permutations(word,i):
            words_set.add("".join(perm))
            
    return words_set


word = input("Enter a word:")

result = smaller_words(word)

print("Smaller words that can be formed:",result)