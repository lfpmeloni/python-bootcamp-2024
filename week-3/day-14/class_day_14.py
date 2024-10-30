"""
class_day_14.py
Author: Felipe Meloni  
Date: 2024-10-30
Description: Mutable and Immutable Objects
"""

# Exercise 1: Create a list, print the storage location of the list using print(id(name_list)), Replace an element of the list with somethging different (another number, string, ...), have the storage location displayed again. What do you see?

# Demonstrating Mutable and Immutable Objects in Python

# Part A: Demonstrating Mutable Objects (Lists)
# Step 1: Create a list and print its storage location

my_list = [1, 2, 3, "test"]
print("Initial list ID:", id(my_list))

# Step 2: Replace an element of the list and print the storage location again

my_list[2] = "change"  # Changing the third element from 3 to "change"
print("Modified list ID after changing an element:", id(my_list))

"""
Expected Outcome: The memory ID of the list remains the same after changing an element.
Explanation: Lists are mutable objects in Python. When we modify an element within the list, 
the object itself is not changed; only its contents are updated. Hence, the memory location (ID) remains unchanged.
"""

# Part B: Reassigning the List
# Step 3: Create a new list and assign it to the same variable

my_list = [1, 2, 3, "test"]
print("Initial list ID before reassignment:", id(my_list))

# Step 4: Reassign the list variable to a new list
my_list = ["test", 4, 5, 6]
print("New list ID after reassignment:", id(my_list))

"""
Expected Outcome: The memory ID of the list changes after reassignment.
Explanation: When we reassign my_list to a new list, we create a new list object in memory and 
point the variable my_list to this new object. Therefore, the memory location (ID) changes.
"""

# Discuss the storage principles of mutable objects
# Graphically display the references with storage location

mylist = [2,4,5]
mynewlist = mylist

# Change elements in mynewlist and then have mylist output
# Do the same again wioth a dict
# Have the id of the objects displayed


# Part C: Storage Principles of Mutable Objects
# Graphically displaying the references (conceptual representation)

# Creating two references to the same list
mylist = [2, 4, 5]  # Original list
mynewlist = mylist  # Reference to the same list
print("mylist ID:", id(mylist))
print("mynewlist ID:", id(mynewlist))

# Step 5: Change an element in mynewlist and observe mylist
mynewlist[0] = "changed"  # Modifying the first element in the new list reference
print("mylist after changing mynewlist:", mylist)

"""
Expected Outcome: Changes in mynewlist affect mylist.
Explanation: Both variables mylist and mynewlist point to the same list object in memory. 
Thus, any changes made through one reference will be reflected in the other.
"""

# Part D: Demonstrating Mutable Objects with Dictionaries
# Creating two references to the same dictionary
mydict = {"name": "Alice", "age": 30}  # Original dictionary
mynewdict = mydict  # Reference to the same dictionary
print("mydict ID:", id(mydict))
print("mynewdict ID:", id(mynewdict))

# Step 6: Modify an element in mynewdict and observe mydict
mynewdict["age"] = 31  # Changing the age value in the new dictionary reference
print("mydict after changing mynewdict:", mydict)

"""
Expected Outcome: Changes in mynewdict affect mydict.
Explanation: Similar to lists, dictionaries are also mutable objects. 
Both mydict and mynewdict refer to the same dictionary object in memory. 
Changes made through one reference are reflected in the other.
"""

# Exercise 3: Create a tuple, print the storage location of the tuple using print(id(name_tuple)), replace an element of the tuple with something else (different number, string, etc). Have the storage location displayed again. What do you see? Compare this to the exercise with list.

# Exercise 3: Demonstrating Immutable Objects (Tuples)

# Step 1: Create a tuple and print its storage location
name_tuple = (1, 2, 3, "test")
print("Initial tuple ID:", id(name_tuple))

# Step 2: Attempt to replace an element of the tuple
# Since tuples are immutable, we cannot directly change an element.
# Uncommenting the following line will result in a TypeError.
# name_tuple[2] = "change"  # This line will raise an error if uncommented

# Instead, we'll create a new tuple to demonstrate immutability
new_tuple = (name_tuple[0], name_tuple[1], "change", name_tuple[3])
print("New tuple ID after creating a modified version:", id(new_tuple))

"""
Expected Outcome: 
1. The memory ID of the original tuple remains the same after the attempted modification (which is not allowed).
2. The new tuple, created as a modified version, has a different memory ID.
   
Explanation: Tuples are immutable in Python. When we try to modify an element of a tuple, it results in an error because the structure cannot be changed in place. 
Instead, we can create a new tuple with the desired changes, which allocates a new memory location, resulting in a different memory ID.
"""

# Step 3: Compare to the previous exercise with lists
print("Comparing with lists:")
my_list = [1, 2, 3, "test"]
print("List initial ID:", id(my_list))

# Modify the list
my_list[2] = "change"
print("List modified ID after changing an element:", id(my_list))

"""
Comparison:
- For the list: The memory ID remains the same after modifying an element, indicating that the object is mutable.
- For the tuple: The memory ID remains the same after the attempted modification, and a new tuple must be created to reflect changes, indicating that the tuple is immutable.
"""

# Consider a class from the previous exercises, create a set, determine whether the class or set is a mutable or immutable object. Graph the references if it helps. For a set and classes, think of a reason why this is mutable/immutable.

# Exercise 4: Demonstrating Mutable and Immutable Objects with Sets and Classes

# Part A: Demonstrating a Set
# Step 1: Create a set and print its storage location
my_set = {1, 2, 3, "test"}
print("Initial set ID:", id(my_set))

# Step 2: Modify the set by adding an element
my_set.add("change")
print("Modified set ID after adding an element:", id(my_set))

"""
Expected Outcome: The memory ID of the set remains the same after adding an element.
Explanation: Sets are mutable objects in Python. When we modify a set (e.g., adding an element), 
the object itself is not replaced, and its memory location (ID) stays the same.
"""

# Part B: Graphically Displaying References for Sets
# Conceptual Representation
print("\nGraphical Representation of Set Reference:")
print(f"my_set -> {my_set} (ID: {id(my_set)})")
print("After adding 'change':")
print(f"my_set -> {my_set} (ID: {id(my_set)})")

# Part C: Demonstrating a Class
# Step 3: Create a simple class
class MyClass:
    def __init__(self, value):
        self.value = value

# Step 4: Create an instance of the class and print its storage location
my_object = MyClass(10)
print("\nInitial class instance ID:", id(my_object))

# Step 5: Modify an attribute of the class instance
my_object.value = 20
print("Modified class instance ID after changing an attribute:", id(my_object))

"""
Expected Outcome: The memory ID of the class instance remains the same after modifying an attribute.
Explanation: Instances of classes are mutable. When we modify an attribute of the class instance, 
the object itself is not replaced, and its memory location (ID) stays the same, indicating that the object is mutable.
"""

# Part D: Graphically Displaying References for Class Instances
# Conceptual Representation
print("\nGraphical Representation of Class Reference:")
print(f"my_object -> MyClass(value={10}) (ID: {id(my_object)})")
print("After changing value to 20:")
print(f"my_object -> MyClass(value={my_object.value}) (ID: {id(my_object)})")

# Summary of Mutability
"""
- **Sets**: Mutable objects that allow for changes in their elements without creating a new object.
- **Classes**: Instances of classes are also mutable, allowing for changes in their attributes.

Reasons for Mutability:
- **Sets**: Designed to be mutable to allow dynamic updates, making them useful for tasks like maintaining a unique collection of items.
- **Classes**: Designed for mutability to model real-world objects, where attributes often change over time, allowing for flexible object behavior.
"""
