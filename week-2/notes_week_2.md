# Content of Week 2

## Day 6

### Lists

A list is a collection of items in a particular order. It can contain the letters of the alphabet, digits from 0-9, names of people, or anything else you want and they dont have to be related in any particular way. **It is common practice to name a list in plural: letters, digits, names.** Syntax:

    bicycles = ['trek', 'specialized', 'cube']
    print(bicycles) -> ['trek', 'specialized', 'cube']

Accessing Elements in a List **Index Positions Start at 0, Not 1**:

    print(bicycles[0]) -> 'trek'
    bicycles[0].title() -> 'Trek'

Python has a special syntax for accessing the last element in a list. This is specially useful when you dont know the complete size of a list:

    print(bicycles[-1]) -> 'cube'

Modifying Elements in a list:

    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles[0] = 'ducati'
    print(motorcycles) ->['ducati', 'yamaha', 'suzuki']

Adding Elements to a list:

    motorcycles.append('ducati')

In running programms with input from user this is usefull, just remember to start by defining an empty list that will hold users values:

    motorcycles = []

Inserting Elements into a List (at any position):

    motorcycles.insert(0,'ducati')
    print(motorcycles) ->['ducati', 'honda', 'yamaha', 'suzuki']

Removing Elemnts from a list (from any position using index):

    del motorcycles[0]

Removing using pop() Method: This method removes the last item in a list, but lets you work with that item later. Usefull when you wnat to work with the last element in a time series.

    motorcycles = ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motorcycles.pop()
    print(popped_motorcycle) -> suzuki #and motorcycles will not have this element on it

Popping Items from Any Position in a list. Remember that each time you pop an item it is no longer in the original list.

    first_owned = motorcycles.pop(0)

Removing an item by Value. The remove method tells Python to find the item in the list and remove that element. You can also remove by defining a list to be removed. Note: The remove method removes only the first occurrence of the value. If it is possible to have more than one item with same value, an interation should be used.

    motorcycles.remove('honda')

Sorting a list permanently with the sort() Method

    motorcycles.sort()
    motorcycles.sort(reverse=True)

Sorting a List Temporarily with the sorted() Function. **Note that sorting strings that start with Upper and Lower Cases and must be specified accordingly.**

    print(sorted(motorcycles))

Printing a list in reverse order. Simply reverses the order of the list:

    motorcycles.reverse()

Finding the length of a list. **This count starts at 1**

    len(motorcycles)

Avoiding Index Error when working with Lists

    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles[3]) -> IndexError: list index out of range

    motorcycles = []
    print(motorcycles[-1]) -> IndexError: list index out of range

### Loops

Why are they usefull? Move all items a same amount, perform statistical operation on every element and so on.

Looping through an entire list. **Common practice is to name the interaction element in singular: cat in cats, dog in dogs, etc.

    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician)

Avoiding indentation Errors

    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
    print(magician) -> IndentationError: expected an indented block after 'for' statement on line 2

    message = "Hello Python world!"
    print(message) -> IndentationError: unexpected indent

Working with numerical lists

    for value in range(1,5):
        print(value) -> prints 1 through 4

    for value in range(6)
        print(value) -> prints 0 through 5

Making a list of numbers

    numbers = list(range(1,6))
    print(numbers) -> [1, 2, 3, 4, 5]

Skip numbers in given range

    even_numbers = list(range(2,11,2))
    print(even_numbers) -> [2, 4, 6, 8, 10]

You can create almost any set of numbers

    squares = []
    for value in range (1,11):
        square = value ** 2
        squares.append(square)
        # Or a more Pythonic way inside the loop
        # squares.append(value**2)
    print(squares) -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Simple statistics with a List of Numbers

    min(squares) -> 1
    max(squares) -> 100
    sum(digits) -> 385

List Comprehensions: Allows to generate the same outcome above in just one line of code by combining the for loop and the creation of new elements into one single line.

    squares = [value**2 for value in range (1,11)]
    print (squares) -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Working with Part of a List

Slicing a list: As with the range() function, Python stops one item before the secong index specifies. **You can include a third value in the brackets indicating a slice. If a third value is
included, this tells Python how many items to skip between items in the specified
range.**

    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3]) -> ['charles', 'martina', 'michael']
    print(players[-3:]) -> ['michael', 'florence', 'eli']

Looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title()) -> Here are the first three players on my team:
    Charles
    Martina
    Michael

Copying a list: Useful when you start with a list and want to edit it without altering the original one. [:] -> This tells Python to make a copy of the entire list

    my_foods = ['pizza', 'falafel', 'carrot cake']
    1 friend_foods = my_foods[:]
    print("My favorite foods are:")
    print(my_foods)
    print("\nMy friend's favorite foods are:")
    print(friend_foods)

## Day 7

### Functions

docstring best practice

    def beispiel():
        """
        Just an example that prints some text :return: None
        """
        print('Some random Text: Panda!')

Passing information to a Function

    def greet_user(username):
        """Display a simple greeting."""
        print(f"Hello, {username.title()}!")
    greet_user('jesse')

Arguments and Parameters

## Day 8

### Arguments

Notes and exercises are being done directly on the class_day_8.py file

Introduction to Typing in Python Functions
Typing allows you to specify the expected data types for function parameters and return values. It helps in making code more readable, reducing errors, and enhancing development tools like IDEs and linters to provide better suggestions and warnings. Python uses type hints to define types but doesn't enforce them strictly, meaning incorrect types won't stop the code from running (unless there is a type-related runtime error).

Syntax for Typing:

    def function_name(param_name: data_type) -> return_type:
        # function logic here
    param_name: data_type: Specifies the type of the parameter.
    -> return_type: Specifies the type of the return value.

Example with Typing:

    def add_numbers(x: int, y: int) -> int:
        return x + y
    This function expects two integers x and y as input and returns an integer.

Using Typing with Default Values:

When defining a default value for a parameter, you still specify the type, and then assign the default value:

    def greet(name: str, age: int = 18) -> str:
        return f"Hello {name}, you are {age} years old."

In this case name must be a string, age is an integer with a default value of 18.

What Happens if You Call the Function with the Wrong Type?

Python does not enforce types at runtime. If you call the function with the wrong type, the function will still run unless the operation inside the function depends on the correct type and raises an error.

Example:

    def add_numbers(x: int, y: int) -> int:
        return x + y
    If you call it with:

    print(add_numbers("3", 5))  # Incorrect types
    It will raise a TypeError at runtime because Python cannot add a string to an integer:

    TypeError: can only concatenate str (not "int") to str
    Using Typing with Calculations:

If you specify a type (e.g., int) and pass a wrong type like str, you will get an error during calculations:

    def multiply(x: int, y: int) -> int:
        return x * y

Calling:

    print(multiply("3", 2))  # Wrong type, string instead of integer

Results in:

    333  # It repeats the string "3" twice instead of performing multiplication.

What Happens When Printing?

If you print a value that doesn't match the expected type, Python will still print it without any issue because print() accepts any object. However, the function logic might not behave as expected.

Example:

    def concat_strings(a: str, b: str) -> str:
        return a + b

Calling:

    print(concat_strings(3, " apples"))  # Wrong type
    Will result in:

    TypeError: unsupported operand type(s) for +: 'int' and 'str'

Conclusion:

Typing helps you specify the types of inputs and outputs for functions.
Python doesn't enforce types at runtime but helps developers by providing clearer intent and possible warnings in IDEs.
If wrong types are used in calculations or operations, it will result in runtime errors.
Default values work seamlessly with typing, as long as the default value matches the specified type.

The -> str in def concat_strings(a: str, b: str) -> str: indicates that the function is expected to return a value of type str (string).

## Day 9

Lesson Summary: References in Python
In Python, references are how variables point to the memory location where an object is stored. When you assign a variable to an object (e.g., a list or dictionary), the variable holds a reference to that object in memory, rather than the actual data itself.

Key Points:

### Variables are References

When you assign a value to a variable, that variable doesn't hold the value directly. Instead, it holds a reference to the object in memory.
Example:

    a = [1, 2, 3]
    b = a  # `b` now references the same list as `a`
    b.append(4)
    print(a)  # Output: [1, 2, 3, 4]

In this case, a and b reference the same list, so changes made through b are reflected in a.

### Mutable vs. Immutable Types

Mutable objects (e.g., lists, dictionaries, sets) can be modified in place, meaning changes via one reference affect all references.
Immutable objects (e.g., integers, strings, tuples) cannot be changed. If you modify an immutable object, a new object is created, and the variable will reference the new object.
Example with immutable objects:

    x = 10
    y = x
    y += 1
    print(x)  # Output: 10 (unchanged, because integers are immutable)

### Copying Objects

If you want to create a new independent object instead of a reference, you need to copy the object.
For shallow copies (copies only the outer structure, not the nested objects):

    import copy
    a = [1, [2, 3]]
    b = copy.copy(a)
    b[0] = 9
    b[1].append(4)
    print(a)  # Output: [1, [2, 3, 4]] (the nested list is still shared)

For deep copies (copies everything, including nested objects):

    b = copy.deepcopy(a)

### Object Identity

The id() function returns the memory address of an object.

    a = [1, 2, 3]
    print(id(a))  # Prints the memory address of `a`

### Pass-by-Reference

Function arguments are passed by reference in Python. This means that if a mutable object is passed into a function, the function can modify the original object.

    def modify_list(lst):
        lst.append(4)

    my_list = [1, 2, 3]
    modify_list(my_list)
    print(my_list)  # Output: [1, 2, 3, 4]

### Key points

1. Variables in Python hold references to objects in memory.
2. Mutable objects can be modified through references, while immutable objects cannot.
3. Copying objects is necessary to avoid unintentional modifications when working with mutable objects.

### Understanding String References in Python

In Python, strings are immutable objects, meaning that once a string is created, its content cannot be changed. When you work with strings, it’s essential to understand how references, objects, attributes, and indexes work together.

Objects and References
String Object: A string is an object that holds a sequence of characters.

Reference: When you assign a string to a variable, you’re creating a reference to the string object in memory, not a copy of the string. Multiple variables can reference the same string object.

    s1 = "Hello"
    s2 = s1  # s2 references the same string object as s1

In this example, both s1 and s2 refer to the same string object in memory.

Attributes
Strings in Python come with built-in methods (attributes) that you can use to manipulate or retrieve information from them.

    s = "Hello, World!"
    upper_s = s.upper()  # Calls the upper() method to return a new string

The method upper() creates a new string object with all characters converted to uppercase. The original string s remains unchanged because strings are immutable.

Indexes
Strings can be accessed using indexes, which are integer values that represent the position of each character in the string, starting from 0.

    s = "Hello"
    first_character = s[0]  # 'H'
    last_character = s[-1]  # 'o'

In this example, s[0] retrieves the first character of the string, while s[-1] retrieves the last character.

Modifying Strings
Since strings are immutable, any method that appears to modify a string will instead return a new string object. For example:

    original = "Hello"
    modified = original.replace("H", "J")  # Creates a new string

Here, original remains "Hello", while modified becomes "Jello". The reference for original does not change; it still points to the original string object.

Memory Management
When multiple variables reference the same string object, they share that object in memory. Modifying one variable’s string (e.g., through methods) creates a new string object, leaving the original object intact.

Strings are Immutable: Once created, their content cannot be changed. Any "modification" returns a new string object.

References: Variables can refer to the same string object in memory.

Methods and Attributes: Strings have built-in methods to perform operations; these return new strings rather than modifying the original.

Indexing: You can access characters in a string using indexing, with 0 being the first position.

## Day 10

### Recursive Functions in Python

Definition:
A recursive function is a function that calls itself in order to solve a problem. It typically breaks down a complex problem into simpler sub-problems of the same type.

Key Characteristics:
Base Case: Every recursive function must have at least one base case that stops the recursion. This prevents infinite loops and ensures the function eventually terminates.

Recursive Case: This part of the function calls itself with a modified argument, moving towards the base case.

Example:
Here's a simple example that computes the factorial of a number using recursion:

    def factorial(n):
        if n == 0 or n == 1:  # Base case
            return 1
        else:
            return n * factorial(n - 1)  # Recursive case

Example usage:

    result = factorial(5)  # 5! = 120
    print(result)  # Output: 120

Advantages:
Simplicity: Recursive solutions can be more intuitive and easier to read, especially for problems that naturally fit recursive structures (e.g., tree traversals).

Conciseness: They can reduce the amount of code needed compared to iterative solutions.

Disadvantages:
Performance: Recursive functions can be less efficient due to the overhead of multiple function calls, leading to increased memory usage.

Stack Overflow: Deep recursion can lead to a stack overflow error if the base case is not reached.

### Importance of Debugging Recursive Functions

Why Use a Debugger?
Visualizing the Call Stack: Recursive functions can create many nested calls. A debugger helps you see the call stack, making it easier to understand the flow of execution.

Tracking Variable States: You can monitor variable values at each level of recursion, helping identify issues.

Identifying Base Case Issues: A debugger ensures that the base case is reached and prevents infinite recursion.

Step-by-Step Execution: You can execute code line by line, making it easier to see how recursion unfolds.

Using the Debugger in Visual Studio Code (VSCode)
Setup:
Open VSCode: Launch Visual Studio Code.
Create a New Python File: Write a recursive function (e.g., factorial).
Set Up the Debugger:
Click on the "Run and Debug" icon and create a launch.json file for configurations.
Set Breakpoints: Click in the gutter next to the line number to set breakpoints for debugging.
Debugging Controls:

    Continue (F5): Run until the next breakpoint.
    Step Over (F10): Execute the next line without stepping into functions.
    Step Into (F11): Step into the function to see inner workings.
    Step Out (Shift + F11): Step out of the current function.
    Restart (Ctrl + Shift + F5): Restart debugging.
    Stop (Shift + F5): Stop debugging.

Observations:
Watch Variables: Monitor variable values at each point.
Call Stack: Review the order of function calls.
Debug Console: Evaluate expressions and see outputs during debugging.
Summary of IDs and Changes in Recursive Functions
While debugging recursive functions, you can visualize how each function call affects variable states and how control flows through the recursive structure. Understanding these concepts is crucial for effectively debugging recursive logic.
