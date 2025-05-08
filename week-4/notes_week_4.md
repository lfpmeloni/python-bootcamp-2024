# Content of Week 4

## Day 15

### Inheritance in Python

Introduction to Inheritance

Motivation: Programmers leverage inheritance to automate repetitive tasks.

Inheritance Principle

Inheritance is a classification system where a main class (parent) shares attributes and methods with subclasses.

Example: Animals
3
Creating multiple animal classes with shared methods, e.g., makeSound(), to avoid redundant coding.

Defining the Main Class

Main classes are defined with relevant attributes, which can be inherited by subclasses.

The super() Function

super() allows calling methods from the main class within a subclass, making code maintenance easier.

Inheritance of Attributes

All attributes from the main class are inherited by default, but subclasses can have unique attributes.

Inheritance of Methods

Methods from the main class can be accessed by subclasses without redefinition, enhancing code reuse.

Access Modifiers

Types:
Public: Accessible inside and outside the class.
Protected: Accessible within the class and subclasses.
Private: Accessible only within the class.

Multi-Level Inheritance

Attributes and methods can be inherited from a subclass to another level of subclass, creating hierarchical inheritance.
Multiple 3

A subclass can inherit from multiple main classes, though it should be used with caution due to complexity.

Method Resolution Order (MRO)

Defines the order in which classes are inherited, prioritizing from bottom to top and left to right if on the same level.

Example Use Case: Dungeon Crawler Game

Illustrates multiple inheritance with an example from game design to handle complex object interactions.

## Day 16

### Generator and Iterator

Every Generatir is a Iterator but not all itarator is a Generator

Iterables and Iterators:

Iterable: An object that can be looped over (e.g., lists, tuples).
Iterator: An object that can traverse through an iterable.
next(): Retrieves the next item in an iterator.
iter(): Converts an iterable to an iterator.

Generators:

Defined using yield instead of return, generating items one by one.
Shorter code than iterators, as it doesn’t store local variables.

Comparison:

Iterators: Implemented through classes, longer code, store local variables.

Generators: Implemented as functions, shorter code, do not store local variables.

### Decorators and Data Classes

#### Decorators

Function Decorators: Shortcuts for modifying functions. Used by prefixing @decorator.
Class Decorators: Similar to functions, allowing class attributes to be defined as objects within a class.

##### Data Classes

Introduced in Python 3.7 to simplify class creation, reducing boilerplate code.

Created using the @dataclass decorator, making classes behave like regular classes but with predefined properties.

Main features: Sortable (@dataclass(order=True)), Immutable (@dataclass(frozen=True)), tuple/dict conversion, and enhanced print() and debugging support.

field() Function:

Specifies attribute behavior within a dataclass.
Allows setting whether an attribute should be defined during or after __init__.

Method Decorators:

@staticmethod: Defines methods independent of the instance.
@classmethod: Uses the class itself as the first argument rather than an instance.

### Graphical User Interfaces with Tkinter

Tkinter Overview:

Tkinter is Python’s built-in GUI package.
Follows an event-driven paradigm, where events (like button clicks) trigger actions.
Creating a Basic Interface:

Initialize Tkinter: root = tk.Tk()
Set Attributes: root.title(), root.geometry()
Start the Interface: root.mainloop()
Layout Management:

Three methods to position elements:
pack(), grid(), and place().
Buttons and Widgets:

Widgets are elements like buttons, text fields, sliders, etc.
Buttons are created with ttk.Button() and positioned using layout methods.
Binding Events:

Command Binding: Directly links an event to a function.
Event Binding: Binds a function to a specific event using .bind().
Additional GUI Elements:

Common widgets: labels, text fields, progress bars, checkboxes, sliders, etc.
