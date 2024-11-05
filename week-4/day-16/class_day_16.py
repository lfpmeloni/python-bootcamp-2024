"""
class_day_16.py
Author: Felipe Meloni  
Date: 2024-11-05
Description: Generator and Iterator
"""

# Get an iterator from an object

mylist = ['a','b','c']
print(mylist)
mylist = iter(mylist)
print(mylist)
print(next(mylist))
print(next(mylist))
print(next(mylist))

# What is the meaning of sentinel in programming? -> Is a special value used to terminate a loop. It is chosen as to not be a legitimate data value that the loop will encounter and attempt to perform with.

class Durchzaehlen:
    #create the attributes -> an iterable variable
    def __init__(self, iterable_variable):
        self.iterable_variable = iterable_variable
        self.iterable_object = iter(self.iterable_variable)
    
    # definition of iteration (beginn of iteration)
    def __iter__(self):
        return self

    # definition on what should be the next element of iteration
    def __next__(self):
        while True:
            try:
                next_obj = next(self.iterable_object)
                return next_obj
            except StopIteration:
                self.iterable_object = iter(self.iterable_variable)

example = Durchzaehlen('abc')
for i in range (10):
    print(next(example), end=' ')

# Generatores -> wird durch wine Funcktion definiert

def counter(n):
    """
    return: Exits the function and returns a single result immediately.
    yield: Pauses the function, returning a value but saving its state, allowing the function to resume and produce multiple results over time (used in generators).

    Args:
        n (int): any number of interactions

    Yields:
        _type_: _description_
    """    
    for i in range(n + 1):
        yield i

for num in counter(10):
    print(num)

# A generator is a special type of iterator created with a function that uses yield. In this example, counter yields each number from 0 to n one by one, pausing after each yield. When for num in counter(10): is run, it retrieves each yielded value, printing 0 to 10 sequentially without storing all values in memory at once.

# Decorator exercise

def myDecorator(fkt):
    """
    A decorator in Python is a function that takes another function and extends or alters its behavior without modifying the original function's code. It wraps the original function, adding code before and/or after it.

    Args:
        fkt (_type_): _description_
    """    
    def fktWrapper():
        print("Before fundtion call")
        fkt()
        print("After function call")
    return fktWrapper

@myDecorator # oder myFkt = myDecorator(myFkt)
def myFkt():
    print("Inside the Function")

myFkt()

# Decorators can also be used as Classes

def myDecorator(aclass):
    class MyWraper:
        def __init__(self, *args, **kwargs):
            self.wrapped = aclass(*args, **kwargs)
            # Atributes wrapped is a object from aclass object

        def decorator_method(self):
            print("Before method call")
            self.wrapped.original_method()
            print("After method call")

    return MyWraper

@myDecorator
class MyClass:
    def __init__(self, name):
        self.name = name

    def original_method(self):
        print(f"Hello, {self.name}!")

test = MyClass('Frada')
test.decorator_method()

# Dataclass

from dataclasses import dataclass

@dataclass
class Participant:
    age: int
    name: str = 'muh'
    def printAttributes(self):
        print(f'{self.name} is {self.age} years old')

example_participant = Participant(3, 'Frada')
example_participant.printAttributes()