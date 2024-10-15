"""
exercices_day_2.py
Author: Felipe Meloni  
Date: 2024-10-15
Description: Second steps in Python
"""

print(7%2)  #remainder of division (modulus)
print(7//2) #floor division

# Part 1: Data Types
# Exercise 1)
# Calculate 2 divided by 4 and store this value in a variable.
# - Consider what type the result should be.
# - Check the type of the variable.
# - Display the variable as an integer and a float.

result = 2/4
""" Should be float because it is not whole number """
print(type(result))
print(int(result))
print(float(result))

# Exercise 2)
# Store the value one million in a variable, once in the 'normal' notation and once in a more readable
# notation. What type do the respective variables have?

million = 1000000
print(million)

million = 1_000_000
print(million)

million = 10**6
print(million)
print(type(million))

""" I personally prefer cientific notation (note that is float) """
million = 1E6
print(million)
print(type(million))

# Part 2: Boolean Expressions
# Exercise 3)
# Decide whether the following statements should output True or False. First, think about the answer
# for each statement, and then verify it in the Python Console. Pay attention to parentheses.

# 3 > 2
""" TRUE """
print("3>2",3>2)

# 5 != 6
""" TRUE """
print("5 != 6",5 != 6)

# 5 == 2
""" FALSE """
print("5 == 2", 5 == 2)

# 3 < 2 or 2 > 1
""" TRUE | 2 is bigger than 1 """
print("3 < 2 or 2 > 1", 3 < 2 or 2 > 1)

# 5 != 9 and 7 < 10
""" TRUE | both conditions are true """
print("5 != 9 and 7 < 10", 5 != 9 and 7 < 10)

# not 5 != 9 and not 7 < 10
""" FALSE | both false """
print("not 5 != 9 and not 7 < 10",not 5 != 9 and not 7 < 10)

# (not 5 != 9 and 7 < 10) or 2 * 3 > 7
""" (FALSE and TRUE) or FALSE -> FALSE """
print("(not 5 != 9 and 7 < 10) or 2 * 3 > 7",(not 5 != 9 and 7 < 10) or 2 * 3 > 7)

# not (5 != 9 and 7 < 10) or 2 * 3 > 7
""" FALSE or FALSE -> FALSE """
print("not (5 != 9 and 7 < 10) or 2 * 3 > 7",not (5 != 9 and 7 < 10) or 2 * 3 > 7)

# Part 3: Importing and Using Packages
# Exercise 4)
# Install the colorama packages.
""" pip install colorama -> OK """

# Exercise 5)
# Import the math package into your script and calculate the square root of 9.
# Hint: Refer to the documentation of the math package. Try finding it first in PyCharm or using Google.
# https://docs.python.org/3/library/math.html

import math
#help(math)
""" https://docs.python.org/3/library/math.html """

# Exercise 6)
# Store infinity (∞) and negative infinity (-∞) in separate variables.

positive_infinity = math.inf
negative_infinity = -math.inf

# Exercise 7)
# Calculate π * e using the math package.

print("π * e =",math.pi * math.e)

# Exercise 8)
# Calculate log10(3) and ln(3) using the math package.

print("log10(3) =",math.log10(3))
print("ln(3) =", math.log(3))

# Exercise 9)
# Define the list: mylist = [1, 2, 3, 4]
# Calculate the following values using numpy:
# - Mean
# - Sum
# - Standard deviation
# Hint: Refer to the documentation of the numpy package. Try finding it first in PyCharm or using
# Google. https://numpy.org/doc/stable/

import numpy as np

mylist = [1, 2, 3, 4]
print("Mean:", np.mean(mylist))
print("Sum:", np.sum(mylist))
print("Standard deviation:", np.std(mylist))

# Afterward:
# Assist other participants (which will help you understand the content better) or read Chapter 1 and 2
# of the book "Python 3 Crashkurs".