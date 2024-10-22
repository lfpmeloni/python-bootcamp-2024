"""
exercises_day_7.py
Author: Felipe Meloni  
Date: 2024-10-22
Description: Functions
"""

# Calculate and print the runtime for every single exercise with a loop!

import time

# Exercise 1)
# Write a function, that calculates the sum of 0 to X and return the result.

def sum_from_zero(x):
    """Returns the sum from zero to input

    Args:
        x (int): sums up until this number

    Returns:
        int: The resulting sum.
    """    
    return(sum(range(x+1)))

start = time.time()
print(sum_from_zero(10))
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 2)
# Write a Function, that calculates and returns the area of a square. The parameter must be the edge length of the square.

def area_of_square(side):
    """Given the side lenght returns the area of a square

    Args:
        side (float): Lenght of the side of a square

    Returns:
        float: The area of a squere with given input as side
    """    
    return(side**2)

start = time.time()
print(area_of_square(7.5))
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 3)
# Write a function that returns a nice output for a random string. The parameter should be a string to be printed and the width of the output.
# A example:
# +--------------------------------+
# + Juhu! +
# +--------------------------------+

def text_frame(text):
    """Frames a text in a fashionable manner

    Args:
        text (str): Any text
    """    
    i = len(text)
    print('+---' + '-'*i + '---*\n+   ' + text + '   +\n' + '+---' + '-'*i + '---*')

start = time.time()
text_frame('Work of art!')
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 4)
# Write a function that counts the number of letters and numbers inside a string. The result should be plotted in a simple histogram in the consol.

def count_letters_and_numbers(input_string):
    """
    Counts the number of letters and numbers in a string and prints a simple histogram.

    Args:
        input_string (str): The input string to analyze.
    """    
    # Initialize counters
    letter_count = 0
    number_count = 0

    # Count letters and numbers
    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            number_count += 1

    # Print the counts and create the histogram
    print("Letters: " + "*" * letter_count)
    print("Numbers: " + "*" * number_count)

start = time.time()
count_letters_and_numbers('Lets write a big number 168432198547')
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 5)
# Write a function that calculates and returns n! (n factorial).
# Tipp: You need the topics from Monday for this.

def factorial_of_n(n):
    """Calculates and returns n!

    Args:
        n (int): Number to be calculated the factorial (n!)

    Returns:
        int: The factorial of n.
    """ 
    result = 1
    for i in range(1, n+1):
        result *= i # Multiply result by each number in the range
    return(result)

start = time.time()
print(factorial_of_n(10))
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 6)
# Take exercise 1,2,3, 5, 6 or 8 of yesterday. Solve those exercises with the help of for, if and while in a function respectively.

def check_characters_for_loop(input_string):
    """
    Checks each character in the input string and determines whether it is a capital letter,
    small letter, or not a letter using a for loop.

    Args:
        input_string (str): The string to check.
    """
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():
                print(f"'{char}' is a capital letter.")
            else:
                print(f"'{char}' is a small letter.")
        else:
            print(f"'{char}' is not a letter.")

def check_characters_if_loop(input_string, index=0):
    """
    Recursively checks each character in the input string and determines whether it is a capital letter,
    small letter, or not a letter using a conditional (if) structure.

    Args:
        input_string (str): The string to check.
        index (int): The current position in the string being checked.
    """
    if index < len(input_string):  # Base condition to stop recursion
        char = input_string[index]
        if char.isalpha():
            if char.isupper():
                print(f"'{char}' is a capital letter.")
            else:
                print(f"'{char}' is a small letter.")
        else:
            print(f"'{char}' is not a letter.")
        check_characters_if_loop(input_string, index + 1)  # Recursive call to the next character

def check_characters_while_loop(input_string):
    """
    Checks each character in the input string and determines whether it is a capital letter,
    small letter, or not a letter using a while loop.

    Args:
        input_string (str): The string to check.
    """
    index = 0
    while index < len(input_string):
        char = input_string[index]
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():
                print(f"'{char}' is a capital letter.")
            else:
                print(f"'{char}' is a small letter.")
        else:
            print(f"'{char}' is not a letter.")
        index += 1

input_string = input("Enter a string: ")

start = time.time()
check_characters_for_loop(input_string)
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

start = time.time()
check_characters_if_loop(input_string)
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

start = time.time()
check_characters_while_loop(input_string)
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

""" The last one ran in half the time """

# Exercise 7)
# Write a function that evaluates boolean expressions. For this purpose, a string with an expression
# (e.g., '5 >= 3') should be given as a parameter, and the output should indicate whether it is true or
# false. Do not use eval() for this exercise, try to solve it by string manipulation and if statements.

def evaluate_boolean_expression(expression):
    """
    Evaluates a simple boolean expression provided as a string and returns True or False.

    Args:
        expression (str): The boolean expression (e.g., '5 >= 3') to evaluate.

    Returns:
        bool: True if the expression is correct, False otherwise.
    """
    # Remove any extra spaces around the operator
    expression = expression.strip()
    
    # Check and split the expression based on different boolean operators
    if '>=' in expression:
        left, right = expression.split('>=')
        return float(left.strip()) >= float(right.strip())
    
    elif '<=' in expression:
        left, right = expression.split('<=')
        return float(left.strip()) <= float(right.strip())
    
    elif '>' in expression:
        left, right = expression.split('>')
        return float(left.strip()) > float(right.strip())
    
    elif '<' in expression:
        left, right = expression.split('<')
        return float(left.strip()) < float(right.strip())
    
    elif '==' in expression:
        left, right = expression.split('==')
        return float(left.strip()) == float(right.strip())
    
    elif '!=' in expression:
        left, right = expression.split('!=')
        return float(left.strip()) != float(right.strip())
    
    else:
        return "Invalid expression or unsupported operator."

# Example usage:
print(evaluate_boolean_expression('5 >= 3'))   # True
print(evaluate_boolean_expression('2 < 4'))    # True
print(evaluate_boolean_expression('7 == 8'))   # False
print(evaluate_boolean_expression('5 != 5'))   # False
print(evaluate_boolean_expression('10 > 2'))   # True
