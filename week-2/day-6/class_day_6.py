"""
class_day_6.py
Author: Felipe Meloni  
Date: 2024-10-21
Description: Interations class
"""

#Exercise 1)
#Create a variable with your name as string and loop over this variable with the for loop

my_name = "Luis Felipe Pellegrini Meloni"
for i in my_name:
    print(i)

#Exercise 2)
#Create lists to interate with the zip method

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for i, j in zip(list1, list2):
    print('List 1:', i, "List 2:", j)

#Exercise 3)
#Enumerate through list

for key, value in enumerate(list1):
    print(key, ":", value)

#Enumerate through dictionary

alien = {'color': 'green', 'points': 5}

for key, value in enumerate(alien):
    print(key, ":", value)

for key, value in alien.items():
    print(key, ":", value)

bsp = zip(list1,list2)
print(list(bsp))

# What zip, enumerate and dict.items have in common?

""" They all allow for iteration over multiple values at once, yielding pairs or sets of elements, which makes them especially useful in loops. 
zip() -> Combines multiple iterables (e.g., lists, tuples) into a single iterable of tuples.
enumerate() -> Adds a counter to an iterable, like a list, tuple, or string.
dict.items() -> Iterates over key-value pairs of a dictionary.
"""
# if, else, elif
age = 5
if age == 5:
    print("equal")
elif age > 5:
    print("greater")
else:
    print("lesser")

# while

while age < 18:
    print('Still under age')
    age += 1

# break, continue

for i in ['a','b','c','d']:
    if i == 'b':
        break
    print(i)

for i in ['a','b','c','d']:
    if i == 'b':
        continue
    print(i)
    
# list comprehension

mylist = [x**2 for x in range (0,8)]

# equivalent to 

ml = []
for x in range(8):
    ml.append(x**2)

mylist2 = [x for x in range (0,8) if x % 2 == 0 and x < 5]