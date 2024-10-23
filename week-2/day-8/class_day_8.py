"""
class_day_8.py
Author: Felipe Meloni  
Date: 2024-10-23
Description: Functions
"""

# Example of arguments

def bsp(name, age):
    print(name, age)

bsp(name='Frade', age=3)
bsp(age=3,name='Frada')
bsp('Frada',3)

# List/Tuple/dict as arguments

# Write a function that takes a list as parameter and one that takes a tuple as parameter. Add 1 to each element in the list/tuple and return the changed list/tuple

def bsp_1(input_list):
    """Adds 1 to each element in the input list.

    Args:
        input_list (list): A list of numbers.

    Returns:
        list: A new list with each element incremented by 1.
    """    
    return [i + 1 for i in input_list]

print(bsp_1([1,2,3]))

def bsp_2(input_tuple):
    """Adds 1 to each element in the input tuple.

    Args:
        input_tuple (tuple): A tuple of numbers.

    Returns:
        tuple: A new tuple with each element incremented by 1.
    """    
    return [i + 1 for i in input_tuple]

print(bsp_2((1,2)))

# Dafault parameter

def greet(name='A girl has no name'):
    print('Hello', name)

greet()
greet('Jack')

# Take exercise 3 from yesterday and replace all parameters with default parameters and call the function withou any arguments

def text_frame(text='Work of art!'):
    """Frames a text in a fashionable manner

    Args:
        text (str): Any text
    """    
    i = len(text)
    print('+---' + '-'*i + '---*\n+   ' + text + '   +\n' + '+---' + '-'*i + '---*')

text_frame()

# *args list and list: Accepts a variable number of arguments and prints each of them.

def bsp_3(*alist):
    for arg in alist:
        print(arg)

# Example usage:
bsp_3(1, 2, 3)  
bsp_3("apple", "banana", "cherry")

# **kwargs allows you to pass a variable number of keyword arguments (i.e., arguments with a name) to a function. The main difference between *args and **kwargs is that *args is used to pass a variable number of positional arguments, while **kwargs is used to pass a variable number of named (keyword) arguments

def bsp_kwargs(**kwargs):
    print(kwargs)

bsp_kwargs(fufu=4, puff='Muh')
bsp_kwargs(shiva='Beste', lina='Granzdebil', momo='Irre')

# Typing: Defining which input type is accepted

def bsp_4(x: int, text: str) -> list:
    out = [x, text]
    return out

print(bsp_4(3, 'hello'))

# Take any function of the last couple of days, use typing for this function, try to compine typing with default paramenters for this function. What happens if you call the function with the wrong type of object?

def bsp_5(side:float=1.0):
    print(side)
    return(side**2)

print(bsp_5(1.0))

""" TypeError if wrong type"""

# The -> str in def concat_strings(a: str, b: str) -> str: indicates that the function is expected to return a value of type str (string).

# Functions as parameters

import math
myfun = math.sqrt # Without Klammers
print(myfun(9))

#Exercise: Create two functions: one returns x**2 and on x**0.5
# Write afterwwards a function, that takes one of theses functions as argument and uses it with a as parameter 

def fun_1(input):
    return(input**2)

def fun_2(input):
    return(input**0.5)

def fun_3(function, int):
    print(function(int))

fun_3(fun_2,3)