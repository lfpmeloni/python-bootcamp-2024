# Content of Week 1

## Day 1

### Naming best practices

Snakecase and Camelcase

    Snakecase -> my_variable, myvarible, my_function
    Camelcase -> myFunction, MyClass

### Common Markdown lint Rules

Here are some examples of common lint rules:

*Heading Style:*

    Enforces consistent heading styles, like using # for top-level headings and ## for subheadings.
    Example Rule: "Headings should not skip levels."

*Line Length:*

    Enforces a maximum line length for readability (e.g., 80 characters).
    Example Rule: "Lines should be wrapped at 80 characters."

*Code Block Style:*

Ensures consistency in code block styles, like using triple backticks (```) for code snippets. Example Rule:

```Use fenced code blocks instead of indentation.```

### Functions and Methods

    name = "albert einstein"

                print(name.title())
    function -> ^^^^^

                print(name.title())
    method ->              ^^^^^^^

A method is an action that Python can perform on a piece of data.
Every method is followed by a set of parentheses, because methods often need additional information to do their work.

Other examples:

    print(name.upper())
    print(name.lower())

### Working with pip

pip is the standard way to manage Python libraries and dependencies.

    pip freeze > requirements.txt
    pip install -r requirements.txt

Creating a new Virtual Environment (venv)

    python -m venv env_name

### Working with GitHub

1. Create repository in GitHub (github.com)
2. Clone the created repository to workspace

        git clone https://github.com/lfpmeloni/python-bootcamp-2024

3. Create, work on items and add to repository

        git add .

4. Commit and push to main branch

        git commit -m "description of the commit"
        git push origin main

### Usefull Shortcuts on Visual Studio Code

Toggle line comment

    Ctrl+/

Toggle block comment

    Shift+Alt+A

Open the Outline view

    Ctrl+Shift+O

Open Keyboard Shortcuts

    Ctrl+K, Ctrl+S

## Day 2

### Common Comments Tracked in PyCharm

    #TODO
    #FIXME
    #NOTE
    #HACK
    #BUG

I Installed the extension Better Comments to have the same functionality in Visual Studio Code

### Better Understanding Classes, Objects, and Methods in Python

Functions vs. Methods
    A function is a block of code that performs a specific task. It is defined using the def keyword and can be used to operate on different types of data. Functions are called by their name followed by parentheses and can take arguments to process the input data.

Example:
```def greet(name):```
```return f"Hello, {name}!"```
```print(greet("Albert Einstein"))```
```# Output: Hello, Albert Einstein!```

    A method, on the other hand, is a function that is associated with an object and is used to perform operations on that object. Methods are called using dot notation on an object (a variable containing a value), followed by parentheses.

Example:

```name = "albert einstein"```
```print(name.title())  # Method -> title()```

In this example:
    name is an object of the str class (a string).
    title() is a method that capitalizes the first letter of each word in the string.
    Since title() is tied to the name object, it can only be used with instances of strings.

Key Differences:
    - Function: Independent and can work with various types of data. Example: print(), len().
    - Method: Always called on an object and operates on that specific object. Example: name.upper(), name.lower().

Class: A blueprint for creating objects. It defines a structure that can hold data (attributes) and actions (methods). Think of it as a template.

Example:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} starts its engine!")

Object: An instance of a class. It is a specific realization of the class template.

Example:

my_car = Car("Tesla", "Model S")  # 'my_car' is an object of the 'Car' class.
my_car.start()
Output: The Tesla Model S starts its engine!

### Overview of Python Syntax

Python is known for its simple and readable syntax, making it a popular language for beginners and professionals alike. Python uses indentation (whitespace) to define blocks of code, such as functions, loops, and conditionals. This focus on readability allows for writing clean and organized code. Here are some key elements:

Variables are defined without specifying types.
Indentation is used instead of braces ({}) to denote code blocks.
Comments are written with # for single-line and ''' or """ for multi-line comments.

### Python Types

integer (int): Whole numbers, both positive and negative, without decimal points.
Example: 5, -3, 42

float: Numbers with decimal points, used for more precise calculations.
Example: 3.14, -0.001, 2.0

strings (str): Textual data, enclosed in single or double quotes.
Example: "Hello, world!", 'Python'

    x = str(5) == x='5'

boolean (bool): Represents True or False values, used in logical operations.
Example: True, False

list: An ordered, mutable collection of items, which can be of mixed types.
Example: [1, 2, 3], ["apple", "banana", "cherry"]

tuple: An ordered, immutable collection of items, similar to a list but cannot be modified.
Example: (1, 2, 3), ("x", "y", "z")

dictionary (dict): A collection of key-value pairs, where each key is unique.
Example: {"name": "Alice", "age": 25}, {1: "one", 2: "two"}

set: An unordered collection of unique items, useful for eliminating duplicates.
Example: {1, 2, 3}, {"apple", "banana", "cherry"}

### Boolean and Logic Operators in Python

==: Equal to
Example: 5 == 5 ➔ True
!=: Not equal to
Example: 5 != 3 ➔ True
>: Greater than
Example: 7 > 3 ➔ True
<: Less than
Example: 4 < 6 ➔ True
>=: Greater than or equal to
Example: 5 >= 5 ➔ True
<=: Less than or equal to
Example: 3 <= 4 ➔ True
and: Returns True if both statements are True.
Example: (5 > 3) and (2 < 4) ➔ True
or: Returns True if at least one of the statements is True.
Example: (5 > 3) or (2 > 4) ➔ True
not: Inverts the boolean value; returns True if the statement is False and vice versa.
Example: not (5 > 3) ➔ False

### Common operators

Modulus or Modulo: 7%2
Floor of division: 7//2
Power: 2**3
Adition: x = x + y or x += y
Subtraction: x = x - y or x -= y
x *= y
x /= y
Readability: 1000000 == 1_000_000 == 10**6 == 1E6
By mixing float and int will result in float
Type of representation 2e4 and 2e-2 are floats
import math for more operators such as Average, Root, e, Std deviation, etc

### Handling Strings

f-strings (f is for format)
To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark.
Example: full_name = f"{first_name} {last_name}"

Whitespace in Strings can be used to organize the output making easier for users to read.
\t -> tab
\n -> newline
\\ -> backlash
\' -> Ein Anfuhungszeichen

string.rstrip() -> removes right whitespace to avoid confusion
string.lstrip() -> same but left
string.lstrip() -> both left and right
string.removeprefix('https:') -> removes content from prefix

## Day 3

### Date and Time

Dates (Day, Month, Year)
Time (Hours, Minutes, Seconds, Milliseconds)
Timezone
Days of the week

The way that time is stored can vary depending on Country, system and so on.

Python solves this with the datetime package.

## Day 4

### Date and Time (continuation)

Defining a date
import datetime as dt
date = dt.datetime(year, month, day, hour, ...)
date = dt.datetime(2024, 3, 4) # Uses positional Arguments
date = dt.datetime(month = 3, year = 2024, day = 4) #is equivalent but uses Keywords Arguments
date = dt.today() #classmethode
date = dt.datetime.now()

date Object
y = dt.date.today(year, month, day) # Recieves year, month and day as parameters

time Object
y = dt.time(hour, minute, second, microsecond)
pause = dt.time(10,5,8) -> 10:05:08 as String

datetime Object
y = dt.dateime.combine(date, time)

dt objects can be added or subtracted but must not mix the objects
Input of the datetime Objects must be integers so to work with strings we use:
dt.datetime.strptime(date_string, format)

Argument Meaning
%A Weekday name, such as Monday
%a Weekday short, such as Mon
%B Month name, such as January
%b Month short, such as Jan
%m Month, as a number (01 to 12)
%d Day of the month, as a number (01 to 31)
%Y Four-digit year, such as 2019
%y Two-digit year, such as 19
%H Hour, in 24-hour format (00 to 23)
%I Hour, in 12-hour format (01 to 12)
%p AM or PM
%M Minutes (00 to 59)
%S Seconds (00 to 61)

Example:
test_date = "05/01/2010 and 11:08:00"
new_date = dt.datetime.strptime(test_date, "%d/%m/%Y and %H:%M:%S")
                                                     ^^^ case sensitive

String format to time function
strftime() -> Converts dt Objects to Strings
y = datetimeobject.strdtime(format)

### Working with data

    Opening a .txt file
    mytext = open('bsp.txt','r')
    <_io.TextIOWrapper name='bsp.txt' mode='r' encoding='cp1252'>
    x = mytext.read() -> reads the text
if i add a number inside read(5) it will retrieve only the first n lines

Input function -> The input() function prompts the user for input and returns that input as a string. It waits until the user enters data and presses Enter.

    user_input = input("Please enter your name: ")
    print("Hello, " + user_input + "!")

Since input() returns data as a string, if you need to work with numeric input, you'll have to convert it.

    age = input("Please enter your age: ")
    age = int(age)  # Convert the string input to an integer
    print("In 5 years, you will be " + str(age + 5) + " years old.")

It's a good practice to handle cases where the user might enter invalid data.

    while True:
        try:
            number = int(input("Please enter a number: "))
            break  # Exit loop if conversion is successful
        except ValueError:
            print("That's not a valid number. Please try again.")
    print("You entered the number: " + str(number))

## Day 5

### list, tuble, dict, set

list -> Collection of ordered, changeable (mutable) Objects
tuple -> collection of ordered, unchangeable (unmutable) objects
dict -> A mutable, ordered collection of Objects saved with a Key
set -> A mutable, unordered collection of unmutable Objects

### List

A mutable, ordered collection that allows duplicate elements. It is often used when you need to store a sequence of items that can be changed (added or removed). Example:
``` my_list = [1, 2, 3, 4] ```
[Python Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Tuple

An immutable, ordered collection that allows duplicate elements. It is useful when you need to store a sequence of items that should not change. Example:
```my_tuple = (1, 2, 3, 4)```
[Python Documentation - Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

### Dictionary

A mutable, unordered collection of key-value pairs. Each key must be unique, and it allows quick access to values based on keys.Example:
```my_dict = {'name': 'Alice', 'age': 30}```
[Python Documentation - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Set

A mutable, unordered collection of unique elements. Sets are commonly used for membership testing and eliminating duplicate entries. Example:
```my_set = {1, 2, 3, 4}```
[Python Documentation - Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

| **Property**      | **List**                    | **Tuple**                   | **Dictionary**                            | **Set**                          |
|-------------------|-----------------------------|-----------------------------|-------------------------------------------|----------------------------------|
| **Order**         | Ordered                     | Ordered                     | Unordered (as of Python 3.7+ maintains insertion order) | Unordered                        |
| **Mutable**       | Yes                         | No                          | Yes                                       | Yes                              |
| **Duplicates**    | Allows duplicates           | Allows duplicates           | Keys must be unique                       | No duplicates                     |
| **Syntax**        | `[1, 2, 3]`                 | `(1, 2, 3)`                 | `{'key': 'value'}`                        | `{1, 2, 3}`                       |
| **Indexing**      | Supports indexing           | Supports indexing           | Access through keys                       | No indexing                       |
| **Use Cases**     | Dynamic collections         | Fixed data that shouldn’t change | Key-value associations for fast lookup | Unique collections for membership testing |
| **Documentation** | [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) | [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) | [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) | [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) |
