"""
exercises_day_9.py
Author: Felipe Meloni  
Date: 2024-10-24
Description: Improving Stadt Land Fluss game
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
import os

def print_welcome_message():
    print('~~~======================================~~~')
    print('~~~~~~~====== Stadt Land Fluss ======~~~~~~~')
    print('~~~======================================~~~')
    print()
    print('Let\'s begin!')
    print()

def get_user_input():
    name = input('What\'s your name? >> ')
    letter = input('Choose a letter to play: >> ').upper()
    return name, letter

def get_answers(questions):
    answers = {}
    for question in questions:
        answer = input(f'{question}: >> ')
        answers[question] = answer
    return answers

def filter_answers(answers, letter):
    incorrect_answers = 0
    for question, answer in list(answers.items()):  # Use list() to avoid RuntimeError
        if not answer.upper().startswith(letter):
            print(f"Warning: '{answer}' for {question} does not start with the letter '{letter}'. It will be removed.")
            answers[question] = 'Incorrect'  # Replace with a placeholder
            incorrect_answers += 1
    return answers, incorrect_answers

def generate_output(name, letter, answers, diff, incorrect_answers):
    out = f'''~~~======================================~~~\n
~~~~~~~====== Stadt Land Fluss ======~~~~~~~\n
~~~======================================~~~\n
Name: {name}\n
Letter: {letter}\n
~~~======================================~~~\n'''

    for question, answer in answers.items():
        out += f'{question}: {answer}\n'

    out += f'''~~~======================================~~~\n
Your time: {diff.seconds} seconds\n
Incorrect answers: {incorrect_answers}\n
~~~======================================~~~\n'''
    
    return out

def save_results(name, letter, start):
    start_time_str = start.strftime('%H_%M')
    file_name = f'{name}_{letter}_{start_time_str}.txt'
    os.makedirs('results', exist_ok=True)
    file_path = os.path.join('results', file_name)

    return file_path

def main():
    print_welcome_message()
    
    # Get user inputs
    name, letter = get_user_input()
    print('\t\t\t~~~ START ~~~')
    start = dt.datetime.now()  # Start time

    # Define the questions
    questions = ['City', 'Country', 'River', 'Color', 'Animal']
    
    # Get answers from the user
    answers = get_answers(questions)

    end = dt.datetime.now()  # End time
    diff = end - start  # Calculate time difference

    # Filter answers based on chosen letter
    answers, incorrect_answers = filter_answers(answers, letter)

    # Prepare output
    output = generate_output(name, letter, answers, diff, incorrect_answers)

    # Save results to a file
    file_path = save_results(name, letter, start)
    with open(file_path, 'w') as file:
        file.write(output)

    print(f'Results saved to {file_path}')

if __name__ == "__main__":
    main()
