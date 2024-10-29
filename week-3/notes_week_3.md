# Content of Week 3

## Day 11

### Programming Paradigms

Programming Paradigms are fundamental styles or approaches in software development that influence how developers structure and write their code. Understanding these paradigms helps in selecting the right tools and techniques for various programming tasks.

General Programming Paradigms:

1. Imperative Programing: Focuses on **how** to perform tasks by giving the computer a sequence of instructions that change the program's state step by step. Key features: Sequential execution, state manipulation and control structures like loops and conditionals. **Usual languages**: C, Java, Python. **Use cases:** System programming, performance-critical applications
2. Declarative Programming: Emphasizes **what** the program should accomplish without specifying **how** to achieve it. Key Features: High-level abstraction,Immutable data, Use of expressions over statements **Usual languages:** SQL, HTML, Haskell. **Use Cases:** Database queries, configuration management, UI design.
3. Object-Oriented Programming (OOP): Organizes software design around **objects** and **classes** that encapsulate data and behavior. **Key Features:** Encapsulation, Inheritance, Polymorphism, Abstraction. **Usual languages:** Java, C++, Python. **Use Cases:** Large-scale systems, GUI applications, game development
4. Data Stream-Oriented Programming: Centers on the flow of data through a series of operations or transformations. **Key Features:** Continuous data streams, Functional transformations (map, filter, reduce), Asynchronous processing. **Usual languages:** Reactive Extensions (Rx), Apache Kafka. **Use Cases:** Real-time data processing, event-driven applications, streaming services
5. Esoteric Programming: Designed for experimentation, entertainment, or to challenge conventional programming concepts rather than practical use. **Key Features:** Unconventional syntax and semantics, Minimalistic or overly complex designs, Artistic or intellectual challenges
6. Multiparadigm Programming: Utilizes multiple programming paradigms within a single program or language to leverage their strengths. **Key Features:** Flexibility to switch paradigms, Composability of different concepts, Support from the programming language. **Usual languages:** Python, JavaScript, Scala. **Use Cases:** Complex software systems, projects benefiting from diverse approaches

### Programming Paradigms in Python

Python is a **multiparadigm** language, supporting various programming styles. Here's how Python implements key paradigms:

#### 1. Functional Programming

**Definition:** Treats computation as the evaluation of mathematical functions, avoiding state and mutable data.

**Features in Python:**

- First-class and higher-order functions
- Lambda expressions
- Built-in functions like `map()`, `filter()`, `reduce()`
- List comprehensions and generator expressions

**Example:**

    # Using map and lambda
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))

#### 2. Imperative Programming

**Definition:** Focuses on how to perform tasks with explicit statements that change program state.

**Features in Python:**

- Sequential execution of statements
- Control structures: for, while, if, else

**Example:**

    total = 0
    for i in range(1, 6):
        total += i
    print(total)  # Output: 15

#### 3. Object-Oriented Programming (OOP)

**Definition:** Uses objects and classes to model real-world entities and their interactions.

**Features in Python:**

- Class and object definitions
- Inheritance (single and multiple)
- Polymorphism and encapsulation

**Example:**

    class Animal:
        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    dog = Dog()
    print(dog.speak())  # Output: Woof!

#### 4. Structured Programming

**Definition:** A subset of imperative programming that emphasizes clear, linear structure using sequences, selections, and iterations.

**Features in Python:**

- Modular code with functions and modules
- Clear control flow without goto

**Example:**

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)

    print(factorial(5))  # Output: 120

#### 5. Reflective Programming

**Definition:** Allows programs to inspect and modify their own structure and behavior at runtime.

**Features in Python:**

- Introspection with functions like dir(), type()
- Metaprogramming using decorators and dynamic class creation
- Dynamic typing

**Example:**

    # Introspection
    class MyClass:
        def method(self):
            pass

    obj = MyClass()
    print(dir(obj))  # Lists attributes and methods

    # Metaprogramming with decorators
    def my_decorator(func):
        def wrapper():
            print("Before function")
            func()
            print("After function")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
    # Output:
    # Before function
    # Hello!
    # After function

#### Other Concepts

Lazy Evaluation: Lazy evaluation is a programming technique where expressions are not computed until their values are actually needed. This approach can improve performance by avoiding unnecessary calculations and can help in handling infinite data structures efficiently.

No goto in Python: Python does not include a goto statement, which encourages the use of structured programming constructs like loops and functions. This design choice helps maintain clear and readable code by preventing arbitrary jumps in the program flow, reducing the likelihood of errors and making the code easier to debug and maintain.

### Python Functional Programming

#### 1. The Lambda Function

Lambda functions are useful for creating small, throwaway functions without the need for a full `def` statement. They are often used in higher-order functions like `map()`, `filter()`, and `reduce()`.

- **Lambda functions** provide a concise way to create simple, anonymous functions.
- They typically accept **one argument**.
- Usually **applied directly** rather than assigned to a variable.

Example:

    # Lambda function to add 10 to the input
    add_ten = lambda x: x + 10
    print(add_ten(5))  # Output: 15

    # Using lambda directly with map
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]

#### 2. The map() Function

`map()` transforms each element in the iterable by applying the specified function, returning a map object which can be converted to a list or other collection types.

- `map()` applies a given function to each item of an iterable (like a list or tuple).
- Takes two arguments: A function and an iterable.
- Often used with lambda functions for inline operations.
- The output of the `map()` function is always a map-Object with the generator and the iterable.

Example

    # Using map with a lambda to square numbers
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]

#### 3. The filter() function

Unlike `map()`, which transforms each element, `filter()` selects elements based on a condition, effectively reducing the iterable to only those elements that meet the criteria.

- `filter()` creates a new iterable containing elements that satisfy a given condition.
- Takes two arguments: A function that returns True or False and
an iterable.
- Often used with lambda functions for inline filtering.

Example:
    # Filter strings that end with 'o'
    mystring = ['Hello', 'Hallihallo', 'Yo', 'Lölle']
    filtered_string = filter(lambda s: s[-1].lower() == 'o', mystring)
    print(list(filtered_string))  # Output: ['Hello', 'Hallihallo', 'Yo']

**`map()` transforms each element.**
**`filter()` selects elements based on a condition.**

#### 4. The reduce() Function

`reduce()` processes the iterable by applying the function to the first two elements, then to the result and the next element, and so on, until only one value remains.

- `reduce()` applies a function cumulatively to the items of an iterable, reducing it to a single value.
- Must be imported from functools.
- Takes two arguments: A function that takes two arguments and an iterable.

from functools import reduce

Example:

    # Multiply all numbers in a list
    numbers = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)  # Output: 24

**Understanding `lambda`, `map()`, `filter()`, and `reduce()` enhances your ability to write concise and efficient Python code. These functional programming tools allow for elegant data processing and transformation, making your code more readable and maintainable.**

## Day 12

### Error Handling with Try and Except

**Introduction:** Error handling is a crucial aspect of programming that ensures your programs can handle unexpected situations gracefully without crashing. Python provides robust mechanisms to manage errors using `try`, `except`, `else`, and `finally` blocks.

#### 1. Errors in Programs

**Summary:** Errors, or exceptions, occur when something goes wrong during the execution of a program. They can halt the program unless properly handled.

**Common Types of Errors:**

- **NameError:** Occurs when a variable is not defined.
- **TypeError:** Happens when an operation is applied to an object of inappropriate type.
- **MemoryError / OverflowError:** Triggered when the program runs out of memory or exceeds limits.

**Implications of Errors:**

- **Program Termination:** Unhandled errors stop the program.
- **Debugging Challenges:** Errors can be hard to locate, especially in large codebases.
- **Incorrect Execution:** Code may run but produce unexpected results.

**Example:**

    print(undefined_variable)  # Raises NameError

#### 2. try and except

**Summary:**

The try block lets you test a block of code for errors, while the except block lets you handle the error.

    try:
        # Code block to test
        print(shiva)
    except:
        # Code to execute if an error occurs
        print('Something went wrong')

try: Contains code that might throw an error.
except: Executes if an error occurs in the try block.

    try:
        print(shiva)
    except:
        print('Something went wrong')  # Output: Something went wrong

#### 3. try, except, and else

**Summary:** The else block runs if no errors occur in the try block, allowing you to execute code that should only run when the try block is successful.

    try:
        # Code block to test
        print(shiva)
    except:
        # Code to execute if an error occurs
        print('Something went wrong')
    else:
        # Code to execute if no error occurs
        print('Everything works fine.')

#### 4. try, except, and finally

**Summary:** The finally block executes no matter what, whether an error occurred or not. It's useful for cleaning up resources.

    try:
        # Code block to test
        print(shiva)
    except:
        # Code to execute if an error occurs
        print('Something went wrong')
    else:
        # Code to execute if no error occurs
        print('Everything works fine.')
    finally:
        # Code to execute regardless of error occurrence
        print('In the finally statement')

#### 5. Error Types

**Summary:** Different errors in Python are categorized by specific types, each indicating the nature of the problem.

Common Error Types and Their Meanings
Error Type -> Meaning
Exception -> General error message; too broad for production use.
NameError -> Variable name is not defined.
TypeError -> Incorrect type used for an operation.
RecursionError -> Maximum recursion depth exceeded.
KeyError -> Key not found in a dictionary.
IndexError -> Index out of range in a list.
MemoryError -> Not enough memory to execute the operation.
OverflowError -> Numerical result too large to be represented.

#### 6. Specific except Blocks

**Summary:** Handling specific error types allows for more precise error management and prevents catching unexpected errors.

    try:
        # Code block to test
        y = math.sqrt(x)
    except TypeError:
        print('Input is not a float or int')
    except NameError:
        print('Variable is not defined')

Explanation: Specific Except Blocks: Each except handles a specific error type.
Order Matters: More specific exceptions should be listed before more general ones.

    import math

    x = 'Hello'
    try:
        y = math.sqrt(x)
    except TypeError:
        print('Input is not a float or int')
    except NameError:
        print('Variable is not defined')
    # Output: Input is not a float or int

Best Practices
Avoid General Except: Never use a bare except: without specifying the error type.
Handle Specific Errors: This ensures that only expected errors are caught and handled appropriately.

#### 7. Raising Exceptions with raise

**Summary:** The raise statement allows you to manually trigger exceptions, which is useful for enforcing certain conditions in your code.

    raise ErrorType('Error message')

Example 1: Raising ValueError

    x = 5
    if x > 0:
        raise ValueError('Number has to be below 0')
    # Output: Raises ValueError: Number has to be below 0

Example 2: Raising TypeError

    x = 5
    if type(x) is not str:
        raise TypeError(f'Input {x} has to be a string')
    # Output: Raises TypeError: Input 5 has to be a string

**Use Cases:**

- Input Validation: Ensuring that functions receive valid inputs.
- Enforcing Invariants: Maintaining certain conditions within your program logic.

**Conclusion:** Effective error handling in Python using try, except, else, and finally blocks allows your programs to manage unexpected situations gracefully. By understanding and handling specific error types, you can create more robust and reliable code. Additionally, using raise enables you to enforce custom error conditions, enhancing the integrity of your applications.

## Day 13

### Classes in Python

- A **class** is a blueprint for creating objects.
- It encapsulates data for the object and methods to manipulate that data.

#### 0. Attributes and Methods

- **Attributes:** Variables that belong to the class.
- **Methods:** Functions defined inside a class that operate on the class's attributes.

    class Dog:
        def bark(self):
            return "Woof!"

#### 1. The `__init__` Method

- The `__init__` method is a special method that initializes new objects. It is the constructor method.

    class Dog:
        def `__init__`(self, name):
            self.name = name

        def bark(self):
            return f"{self.name} says Woof!"

#### 2. Inheritance

- Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):
        def bark(self):
            return "Woof!"

#### 3. Polymorphism

- Polymorphism allows methods to do different things based on the object it is acting upon.

    def animal_sound(animal):
        print(animal.speak())

    dog = Dog()
    animal_sound(dog)  # Output: Animal speaks

#### 4. Encapsulation

- Encapsulation restricts access to certain components of an object, Use private attributes and methods to prevent access from outside the class.

    class Account:
        def `__init__`(self, balance):
            self.__balance = balance  # Private attribute

        def deposit(self, amount):
            self.__balance += amount

#### 5. Class vs. Instance Variables

- **Instance Variables:** Unique to each instance of a class.
- **Class Varibles:** Shared across all intances of a class.

    class Dog:
        species = "Canis familiaris"  # Class variable

        def __init__(self, name):
            self.name = name  # Instance variable

#### 6. Static and Class Methods

- **Static Method:** Does not modify class or instance state.
- **Class Methdos:** Modifies class state and takes `cls` as the first parameter.

    class Dog:
        species = "Canis familiaris"

        @classmethod
        def get_species(cls):
            return cls.species

        @staticmethod
        def info():
            return "Dogs are domesticated mammals."

#### 7. Magic Methods (also known as Dunder Methods)

- Magic methods are special methods in Python that start and end with double underscores (`__`).
- They allow you to define how objects of your class behave with built-in functions and operators.
- Enable operator overloading: Define custom behavior for operators like `+`, `-`, `*`, etc.
- Allow for integration with Python's built-in functions: Use methods with functions like `len()`, `str()`, `repr()`, etc.

#### 8. Common Magic Methods

- Object Creation and Initialization
- **`__init__(self, ...)`**: Initializes a new object.

        class MyClass:
            def __init__(self, value):
                self.value = value

- String Representation
- **`__str__(self)`**: Defines the string representation of an object (for `print()` and `str()`).

        class MyClass:
            def __str__(self):
                return f"MyClass with value {self.value}"

- **`__repr__(self)`**: Defines the official string representation of an object (for `repr()`).

        class MyClass:
            def __repr__(self):
                return f"MyClass({self.value})"

- Comparison Operators
- **`__eq__(self, other)`**: Defines behavior for the equality operator (`==`).
- **`__lt__(self, other)`**: Defines behavior for the less-than operator (`<`).

        class MyClass:
            def __eq__(self, other):
                return self.value == other.value

- Arithmetic Operators
- **`__add__(self, other)`**: Defines behavior for addition (`+`).
- **`__sub__(self, other)`**: Defines behavior for subtraction (`-`).

        class MyClass:
            def __add__(self, other):
                return MyClass(self.value + other.value)

- Container Methods
- **`__len__(self)`**: Defines behavior for `len()`.

        class MyContainer:
            def __len__(self):
                return len(self.items)  # Assuming items is a list

- **`__getitem__(self, key)`**: Defines behavior for indexing (`[]`).

        class MyContainer:
            def __getitem__(self, index):
                return self.items[index]

#### 9. Access Modifiers in Python

Access modifiers in Python define the visibility and accessibility of class attributes and methods. They control how and where these members can be accessed. Python primarily uses three access modifiers: **public**, **protected**, and **private**.

- Public members (attributes and methods) are accessible from anywhere in the code.
- By default, all members in Python classes are public.

        class MyClass:
            def __init__(self):
                self.public_attribute = "I am public!"

            def public_method(self):
                return "This is a public method."

        # Usage
        obj = MyClass()
        print(obj.public_attribute)  # Accessible
        print(obj.public_method())    # Accessible

- Protected members are intended for internal use within the class and its subclasses.
- In Python, protected members are indicated by a single underscore (_) prefix.

        class MyClass:
            def __init__(self):
                self._protected_attribute = "I am protected!"

            def _protected_method(self):
                return "This is a protected method."

        class SubClass(MyClass):
            def access_protected(self):
                return self._protected_attribute

        # Usage
        obj = SubClass()
        print(obj.access_protected())  # Accessible through subclass method
        print(obj._protected_attribute)  # Direct access (not recommended)

- Private members are restricted to the class in which they are defined.
- They are indicated by a double underscore (__) prefix.

        class MyClass:
            def __init__(self):
                self.__private_attribute = "I am private!"

            def __private_method(self):
                return "This is a private method."

            def access_private(self):
                return self.__private_attribute

        # Usage
        obj = MyClass()
        print(obj.access_private())  # Accessible through a public method
        # print(obj.__private_attribute)  # Raises AttributeError
