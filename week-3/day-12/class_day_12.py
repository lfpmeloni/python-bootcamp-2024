"""
class_day_12.py
Author: Felipe Meloni  
Date: 2024-10-28
Description: Error Handling with Try and Except
"""

# Error example

shiva = "Hello"
try:
    print(shiva)
except:
    print('Something went wrong')

# Error with else for positive run

try:
    # Code block to test
    print(shiva)
except:
    # Code to execute if an error occurs
    print('Something went wrong')
else:
    # Code to execute if no error occurs
    print('Everything works fine.')
    

import math # If you dont import math it will throw NameError

x = 'Hello' # also if you don't define x before it will throw NameError 
x = 3

try:
    y = math.sqrt(x)
except TypeError:
    print('Input is not a float or int')
except NameError:
    print('Variable is not defined')

# raise Error example

x = 0
if x > 0:
    raise ValueError('Number has to be below 0')