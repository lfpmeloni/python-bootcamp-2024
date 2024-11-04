# Content of Week 4

## Day 15

### Inheritance in Python

Introduction to Inheritance

Motivation: Programmers leverage inheritance to automate repetitive tasks.

Inheritance Principle

Inheritance is a classification system where a main class (parent) shares attributes and methods with subclasses.

Example: Animals

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
Multiple Inheritance

A subclass can inherit from multiple main classes, though it should be used with caution due to complexity.

Method Resolution Order (MRO)

Defines the order in which classes are inherited, prioritizing from bottom to top and left to right if on the same level.

Example Use Case: Dungeon Crawler Game

Illustrates multiple inheritance with an example from game design to handle complex object interactions.
