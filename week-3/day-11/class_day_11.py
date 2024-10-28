"""
class_day_11.py
Author: Felipe Meloni  
Date: 2024-10-28
Description: Lambda, map and filter functions
"""

# Lambda function: Write a lambda function that returns the input parameter to the power of 3

power_of_3 = lambda x: x**3
print(power_of_3(3))

# map(): Generate a list of random numbers and apply the x**2 and math.sqrt() to mapit using map

import random
import math

random_numbers = [random.uniform(1,100) for _ in range(10)]
print("Random Numbers:", random_numbers)

squared = list(map(lambda x: x**2, random_numbers))
print("Squared:", squared)

square_roots = list(map(math.sqrt, random_numbers))
print("Square Roots:", square_roots)

# filter(): Generate a list of random numbers and apply 

random_numbers = [random.randint(1,20) for _ in range(10)]
print("Random Numbers:", random_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, random_numbers))
print("Even Numbers:", even_numbers)

# reduce(): Write a function that calculates x * y then applt this function to a list of random numbers using reduce()

from functools import reduce

def multipply(x,y):
    return x * y

product = reduce(multipply, random_numbers)
print("Product:", product)

# Or using lambda to make it single lined

product_lambda = reduce(lambda x, y: x * y, random_numbers)
print("Product using lambda:", product_lambda)


