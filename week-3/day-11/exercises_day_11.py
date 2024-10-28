"""
exercises_day_11.py
Author: Felipe Meloni  
Date: 2024-10-28
Description: Lambda, map and filter functions
"""

# Exercises day 11
# Consider using lambda, map, reduce, or filter for solving all tasks.

# Exercise 1)
# Read the file woerter.txt into the script and save the word as list of strings.

file = open('woerter.txt', 'r')
content = file.read()
words = content.split(',') # split in commas to generate list
print(words)

# Exercise 2)
# Clean up the string list:
# - Delete every whitespace or regular expression.
# - Every word must begin with a capital letter, the rest must be small.
# Save the cleaned list of strings as .txt

stripped_words = list(map(lambda word: word.strip(), words))
#print(stripped_words)
cleaned_words = list(map(lambda word: word.title(), stripped_words))
print(cleaned_words)

with open('sauber_woerter.txt', 'w') as file:
    file.writelines(map(lambda word: word + '\n', cleaned_words))

# Exercise 3)
# Figure out the following things about the list of strings. Check the right format of your variable with the help of try/except or raise.
# - Length of the words
# - Which words have “n”, “fe” or “dr” as part of the word. Create a new list for each with just those words.

try:
    words_length = list(map(lambda word:len(word),cleaned_words))
except TypeError:
    print('Input is not a string')
else:
    print('Get lenght of words was a success:', '\n', words_length)

filtered_words = list(filter(lambda word: 'n' in word.lower() or 'fe' in word.lower() or 'dr' in word.lower(), cleaned_words))
print(filtered_words)

# A different approach could use substring

substrings = ['n', 'fe', 'dr']
filtered_words = list(filter(lambda word: any(sub in word.lower() for sub in substrings), cleaned_words))
print(filtered_words)

# Exercise 4)
# Read the file buchstaben.txt into the script and save this as a list. Create a new list out of this, where every element is a single string of a word.
# Example: [‘H‘,‘e‘,‘l‘,‘l‘,‘o‘,‘ ‘,‘W‘,‘o‘,‘r‘,‘l‘,‘d‘] to [‘Hello‘,‘World‘]

file = open('buchstaben.txt', 'r')
content = file.read()
letters = content.split(',') # split in commas to generate list
print(letters)

filtered_letters = list(filter(lambda word: word, ''.join(letters).split(' ')))
print(filtered_letters)

# Exercise 5)
# Write a script, that gets a string (zen of python or some other text) as parameter. After this you should be able to input a word to search for inside the string. Afterward the program must tell you how often the word appeared in the string. If the word didn’t appear in the string, tell the user this.

text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

search_word = input('Enter the word you want to search for:').strip().lower()

words = list(map(lambda word: word.lower(), text.split()))
print(words)

count = len(list(filter(lambda word: word == search_word, words)))

print(f"The word '{search_word}' appeared {count} times in the text." if count > 0 else f"The word '{search_word}' did not appear in the text.")

# Exercise 6)
# Read the file zahlen.txt into the script and save the numbers as list of integers.

with open ('zahlen.txt', 'r') as file:
    numbers = list(map(int, file.read().split(',')))

print(numbers)
