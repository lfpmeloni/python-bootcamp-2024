"""
class_day_4.py
Author: Felipe Meloni  
Date: 2024-10-18
Description: Input use case
"""

import os

print(os.listdir())

mytext = open('bsp.txt','r')

print(mytext)

x = mytext.read()

print(x)

print()
frage = 'Dein Alter?'
age = int(input(frage))
print(age, type(age))