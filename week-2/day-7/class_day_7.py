"""
class_day_7.py
Author: Felipe Meloni  
Date: 2024-10-22
Description: Functions
"""

# Exercise 1
# Write a function that prints a string
# Call the docstring of this function by hovering with your mouse over the function call

def function_example():
    """
    This is an example function that prints 'Blop!'
    """
    print('Blop!')

function_example()

# Using input parameters

def greeting_example(name):
    """"
    This is an example of a function with input Parameter.
    It prints 'Hello Parameter'
    :param name: str - a name to greet
    :return: None
    """
    print ('Hello', name)

greeting_example('Frada')

# Write an input that checks if it is a string before calling the greeting function

# name = input("Hi, what is your name?") # Python always interprets input as a sting so the validation bellow is useless with input
name = 123
if isinstance(name, str):
    greeting_example(name)
else:
    print("Your name is not a string")

# Testing autoDocstring - Python extension
# ctrl + shift + 2 - creates """  """

def test_autodocstring(input):
    """_summary_

    Args:
        input (_type_): _description_
    """

# Exercise 3: Use a function with a return parameter

def do_math(x,y,z):
    """
    Sum 3 argumetns

    Args:
        x (int): Any int to be summed
        y (int): Any int to be summed
        z (int): Any int to be summed

    Returns:
        int: result of the sum of 3 input parameters
    """    
    out = x + y + z
    return out

# Exercise 4: Use of local and global parameters

def myfkt(x,y):
    """Testing with local and global parameters

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """    
    global a
    a = x + y
    z = a * x
    return z
b = myfkt(1,2)
print(a,b) 