"""
class_day_10.py
Author: Felipe Meloni  
Date: 2024-10-25
Description: Recursive functions
"""

# Exercise 1: Test recursive factorial function with debugger break

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Exercise 2: Write a recursive function to return the sum from 0 to n

n = 10
total_sum = sum(i for i in range(n+1))
print(total_sum)

def sum_zero_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_zero_to_n(n-1)
    
print(sum_zero_to_n(10))
