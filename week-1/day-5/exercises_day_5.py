"""
exercises_day_5.py
Author: Felipe Meloni  
Date: 2024-10-18
Description: Modifing Stadt Land Fluss game
"""

# Exercise Stadt Land Fluss v.2)
# Expand Stadt Land Fluss with the following points:
# - Safe the results in a dict with the question as key and the answer(input) as value
# - Every time the program is used, a new file with the results should be saved as
# Name_Letter_Time(HH_MM at begin)
# - For advanced, if-statements have to be used:
# o Remove all values, that do not start with the chosen letter.
# o All values that have to be removed should have a warning.
# o Add information to the output how many questions where wrong.
# If you finish earlier, you can continue working in the book, help other participants, or start working on
# application documents.

import datetime as dt

print('~~~======================================~~~')
print('~~~~~~~====== Stadt Land Fluss ======~~~~~~~')
print('~~~======================================~~~')
print()

print('Let\'s begin!')
print()
# Get user inputs
name = input('What\'s your name? >> ')
letter = input('Choose a letter to play: >> ').upper()
print()
print('\t\t\t~~~ START ~~~')
start = dt.datetime.now()  # Start time

# Define the questions
questions = ['City', 'Country', 'River', 'Color', 'Animal']
answers = {}  # Dictionary to store answers

# Loop through each question and get the answer
for question in questions:
    answer = input(f'{question}: >> ')
    answers[question] = answer

end = dt.datetime.now()  # End time
diff = end - start  # Calculate time difference

# Check if the answers start with the chosen letter
incorrect_answers = 0
for question, answer in answers.items():
    if not answer.upper().startswith(letter):
        print(f"Warning: '{answer}' for {question} does not start with the letter '{letter}'. It will be removed.")
        answers[question] = 'Incorrect'  # Replace with a placeholder
        incorrect_answers += 1

# Prepare output
out = f'''~~~======================================~~~
~~~~~~~====== Stadt Land Fluss ======~~~~~~~
~~~======================================~~~

Name: {name}
Letter: {letter}
~~~======================================~~~
'''

# Add answers to output
for question, answer in answers.items():
    out += f'{question}: {answer}\n'

out += f'''~~~======================================~~~
Your time: {diff.seconds} seconds
Incorrect answers: {incorrect_answers}
~~~======================================~~~
'''

# Generate file name
start_time_str = start.strftime('%H_%M')
file_name = f'{name}_{letter}_{start_time_str}.txt'

# Save output to a file in a subdirectory called 'results'
import os
os.makedirs('results', exist_ok=True)
file_path = os.path.join('results', file_name)

with open(file_path, 'w') as file:
    file.write(out)

print(f'Results saved to {file_path}')
