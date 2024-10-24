"""
class_day_9.py
Author: Felipe Meloni  
Date: 2024-10-24
Description: References
"""

# Print the id of the objects after every step
# Create a variable with value lesser than 256
# Overwrite the object with another number
# Calculate things with those variables
# Repeat with integer bigger than 256 and with floats
# Explain what is happening by using graphics

print('Integer < 256')

x = 255
id_x_original = id(x)
print(id(x))

x = 1
id_x_overwriten = id(x)
print(id(x))
print('After I overwrite the id is the same:', id_x_original == id_x_overwriten)

""" 
This happens because the variable x is now referencing a different object in memory. 
Immutability: In Python, integers are immutable. This means that when you perform operations on an integer, a new object is created in memory rather than modifying the existing object.
Reassignment: When you assign a new value to x, the reference of x is updated to point to a new object in memory. 
"""

y = 25
id_y_different = id(y)
print(id(y))
print('Different objects with different values same id:', id_y_different == id_x_overwriten)

y = 1
id_y_same = id(y)
print(id(y))
print('Different objects with same values same id:', id_y_same == id_x_overwriten)

"""
Integer Caching: Python caches integers between -5 and 256, so reassigning variables within this range reuses the same memory address (id() remains the same for the same values).
"""

print(x**2)
id_x_after_calculation = id(x)
print(id(x))
print('After I calculate the id is the same:', id_x_after_calculation == id_x_overwriten)

"""
Calculations do not change the id() of the original variable because the result is stored in a new object. The original variable still points to the same object.
"""

print('Integer > 256')

x = 350
id_x_original = id(x)
print(id(x))

x = 400
id_x_overwriten = id(x)
print(id(x))
print('After I overwrite the id is the same:', id_x_original == id_x_overwriten)

y = 299
id_y_different = id(y)
print(id(y))
print('Different objects with different values same id:', id_y_different == id_x_overwriten)

y = 400
id_y_same = id(y)
print(id(y))
print('Different objects with same values same id:', id_y_same == id_x_overwriten)

"""
Larger Integers: For integers outside this range, Python creates a new object each time an assignment occurs, resulting in a different id().
"""

print('Float')

x = 3.50
id_x_original = id(x)
print(id(x))

x = 40.0
id_x_overwriten = id(x)
print(id(x))
print('After I overwrite the id is the same:', id_x_original == id_x_overwriten)

y = 29.9
id_y_different = id(y)
print(id(y))
print('Different objects with different values same id:', id_y_different == id_x_overwriten)

y = 40.0
id_y_same = id(y)
print(id(y))
print('Different objects with same values same id:', id_y_same == id_x_overwriten)

"""
Floats: Floats are not cached, so even if you reassign the same float value multiple times, a new object with a different memory address is created each time.
"""

"""
Python can reuse the same memory address (same id) for identical values. This behavior is different from what we initially assumed, but it aligns with Python's internal optimizations, which might involve object reusability for performance, even beyond simple integer caching.
"""

## Now to strings
# Create a string with length bigger than 1
# Create a new variable with the same string
# Change the string with methods
# Create x = '12'
# Print the id of the objects and their elements after every step for loop

# Step 1: Create a string with length bigger than 1
original_string = "Hello, World!"  # The original string is created

# Step 2: Create a new variable with the same string
copied_string = original_string  # copied_string references the same object as original_string

# Function to print the id and content of the strings
def print_info(step, string1, string2):
    print(f"Step {step}:")
    print(f"Original string id: {id(string1)}, content: '{string1}'")
    print(f"Copied string id: {id(string2)}, content: '{string2}'")
    
    # Check if the ids are the same
    if id(string1) == id(string2):
        print("The ids are the same: both variables point to the same object.")
    else:
        print("The ids are different: the variables point to different objects.")
    
    print("---")

# Initial print
print_info(0, original_string, copied_string)

# Step 3: Change the string with methods
# 3.1 Changing to uppercase
original_string = original_string.upper()  # Expectation: original_string is modified, copied_string remains unchanged
print_info(1, original_string, copied_string)

# 3.2 Changing to lowercase
original_string = original_string.lower()  # Expectation: original_string is modified again, copied_string remains unchanged
print_info(2, original_string, copied_string)

# 3.3 Replacing a substring
original_string = original_string.replace("hello", "hi")  # Expectation: original_string is modified, copied_string remains unchanged
print_info(3, original_string, copied_string)

# Step 4: Create x = '12'
x = '12'  # New string created
print_info(4, original_string, x)  # Expectation: original_string and x will have different ids

# Final print to show the ids after all modifications
print("Final Results:")
print(f"Final Original string id: {id(original_string)}, content: '{original_string}'")
print(f"Final Copied string id: {id(copied_string)}, content: '{copied_string}'")
print(f"Final x id: {id(x)}, content: '{x}'")

"""
String Creation: The original string is created and has a specific id.
Copying the String: The copied string references the same object initially, so their ids are the same.
String Modifications:
Uppercase Conversion: After converting to uppercase, original_string changes while copied_string remains the same, resulting in different ids.
Lowercase Conversion: This again modifies original_string, leading to different ids.
Substring Replacement: Similar to previous steps, this will modify original_string but not copied_string, ensuring their ids differ.
Creating Variable x: This creates a new string that is expected to have a different id from original_string.

Explanation:
Step 0: Both original_string and copied_string reference the same object, resulting in the same ID.
Step 1: original_string is modified to uppercase, creating a new object (ID2), while copied_string retains its original ID (ID1).
Step 2: original_string is converted to lowercase, creating another new object (ID3) that is different from both previous IDs.
Step 3: When replacing a substring, original_string retains the ID from the uppercase modification (ID4) since strings are immutable and Python reuses the existing string object when possible. The copied_string still has its own ID (ID1).
Step 4: The new string x is created, which has a unique ID (ID5), while original_string and copied_string retain their previous IDs.
"""

original_str = "Hello"
new_str = original_str

x = "12"

steps = [
("Original String", original_str),
("Neue Variable mit gleichem String", new_str),
("Uppercase", original_str.upper()),
("Ersetze 'e' mit 'a'", original_str.replace('e', 'a')),
("Füge Zeichen hinzu", original_str + " World!"),
("x initialisieren", x)]

for step_name, step_value in steps:
    print(f"{step_name}: Wert = {step_value}, ID = {id(step_value)}")

## Now for list and tuples
# Create a list (ml) and a tuple (mt) with the same elements
# Change the list with methods
# Run: ml2 = ml and ml3 = ml.copy()
# change ml and print ml, ml2 and ml3
# Create a tuple mt = (ml, 1, ...)
# Change ml

#Function that prints the comparisson
def print_step(step, step_name, list_value, tuple_value):
    """Prints the step information in the specified format."""
    print(f"Step {step}: {step_name}")
    print(f" Obj1 Value: {list_value} -> ID: {id(list_value)}")
    print(f" Obj2 Value: {tuple_value} -> ID: {id(tuple_value)}")
    print(f" The same: {id(list_value) == id(tuple_value)}")
    print("---")

#Initial setup
ml = [1, 2, 3]
mt = (ml, 2, 3)

print_step(1, "Originals ml and mt", ml, mt)
print_step(2, "ml using append", ml, ml.append(4))
ml2 = ml
print_step(3, "ml2 = ml", ml, ml2)
ml3 = ml.copy()
print_step(4, "ml3 = ml.copy()", ml, ml3)
ml = [4,3,2,1]
print_step(5, "Changed ml, printing ml and ml2", ml, ml2)
print_step(6, "Changed ml, printing ml and ml3", ml, ml3)
print_step(7, "And what happen to mt (tuple?)", ml, mt)
ml = [1,2,3]
print_step(8, "After we change ml", ml, mt)