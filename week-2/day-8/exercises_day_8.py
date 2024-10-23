"""
exercises_day_8.py
Author: Felipe Meloni  
Date: 2024-10-23
Description: Functions
"""

# Use the typing for all tasks!
    
#     Task 1)
# Write a function that takes one or more lists as parameters. Within the function, check whether the elements of the list(s) are even or odd. All even elements should be returned in one variable, and all odd elements in another.

def even_odd_counter(*lists: list):
    """
    Counts the number of odd and even numbers across multiple lists.

    Args:
        *lists (list): A variable number of lists containing integers.

    Returns:
        tuple: A tuple with two integers:
            - The first integer represents the count of odd numbers.
            - The second integer represents the count of even numbers.
    """  
    odd_count = 0
    even_count = 0
    for list in lists:
        for i in list:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return(odd_count, even_count)

print(even_odd_counter([1,2,3],[4,5,6]))

# Task 2)
# Write a function that counts all uppercase letters, lowercase letters, and spaces in a string and outputs the result as a dictionary.

def check_characters(input_string: str):
    """
    Analyzes the given string and counts the number of uppercase letters, lowercase letters, and spaces.
    It also prints a message for any non-letter character that is not a space.

    Args:
        input_string (str): The string to analyze.

    Returns:
        tuple: A tuple containing three integers:
        - upper_count (int): The number of uppercase letters.
        - lower_count (int): The number of lowercase letters.
        - space_count (int): The number of spaces.

    Example:
    >>> check_characters("Hello World!")
    '!' is not a letter.
    (2, 8, 1)
    """
    upper_count = 0
    lower_count = 0
    space_count = 0
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():
                upper_count += 1
            else:
                lower_count += 1
        else:
            if char == ' ':
                space_count += 1
            else:
                print(f"'{char}' is not a letter.")
    return(upper_count, lower_count, space_count)

print(check_characters("Hello World!"))

# Task 3)
# Write a function that outputs a sorted argument (list or string). Optionally, it should be possible to specify whether a sorting function is used and whether the sorting should be in ascending or descending order.

def sort_fun(arg: list | str, order = "asc"):
    """
    Sorts a list or string in ascending or descending order.

    Args:
        arg (list or str): The list or string to be sorted.
        order (str, optional): The sorting order, either "asc" for ascending (default) or "desc" for descending.

    Returns:
        list or str: The sorted list or string in the specified order.

    Example:
        >>> sort_fun([3, 1, 4, 2])
        [1, 2, 3, 4]

        >>> sort_fun([3, 1, 4, 2], order="desc")
        [4, 3, 2, 1]
    """
    if order == "asc":
        arg.sort()
    elif order == "desc":
        arg.sort(reverse = True)
    else:
        print("Order not correctly specified.")
    return arg

print(sort_fun([1,5,3]))
print(sort_fun([3, 1, 4, 2], order="desc"))

# Task 4)
# Write a function for calculating the volume of a cone, sphere, cuboid, and any arbitrary shape respectively. Each function should take the relevant dimensions (diameter, ...) as parameters. Then, write a function where, based on a string input ('sphere' or similar), the appropriate function is automatically selected, and the volume is outputted. The necessary parameters (such as radius) should also be provided.

import math

def volume_cone(radius: float, height: float) -> float:
    """
    Calculates the volume of a cone.
    
    Args:
        radius (float): The radius of the base of the cone.
        height (float): The height of the cone.
    
    Returns:
        float: The volume of the cone.
    """
    return(1/3) * math.pi * (radius ** 2) * height

def volume_sphere(radius: float) -> float:
    """
    Calculates the volume of a sphere.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    return (4/3) * math.pi * (radius ** 3)

def volume_cuboid(length: float, width: float, height: float) -> float:
    """
    Calculates the volume of a cuboid.
    
    Args:
        length (float): The length of the cuboid.
        width (float): The width of the cuboid.
        height (float): The height of the cuboid.
    
    Returns:
        float: The volume of the cuboid.
    """
    return length * width * height

def volume_arbitrary_shape(base_area: float, height: float) -> float:
    """
    Calculates the volume of an arbitrary shape, such as a prism.
    
    Args:
        base_area (float): The area of the base of the shape.
        height (float): The height of the shape.
    
    Returns:
        float: The volume of the arbitrary shape.
    """
    return base_area * height

def calculate_volume(shape: str, **kwargs) -> float:
    """
    Selects the appropriate volume function based on the shape name and calculates the volume.
    
    Args:
        shape (str): The name of the shape (e.g., 'cone', 'sphere', 'cuboid', 'arbitrary_shape').
        **kwargs: The parameters required for the volume calculation (e.g., radius, height).
    
    Returns:
        float: The volume of the specified shape.
    
    Raises:
        ValueError: If the shape is not recognized.
    """
    shape = shape.lower()
    
    if shape == "cone":
        return volume_cone(kwargs['radius'], kwargs['height'])
    elif shape == "sphere":
        return volume_sphere(kwargs['radius'])
    elif shape == "cuboid":
        return volume_cuboid(kwargs['length'], kwargs['width'], kwargs['height'])
    elif shape == "arbitrary_shape":
        return volume_arbitrary_shape(kwargs['base_area'], kwargs['height'])
    else:
        raise ValueError("Shape not recognized. Please provide 'cone', 'sphere', 'cuboid', or 'arbitrary_shape'.")
    
# Volume of a cone
print(calculate_volume("cone", radius=3, height=5))  # Output: 47.12

# Volume of a sphere
print(calculate_volume("sphere", radius=3))  # Output: 113.10

# Volume of a cuboid
print(calculate_volume("cuboid", length=4, width=3, height=5))  # Output: 60

# Volume of an arbitrary shape (e.g., prism)
print(calculate_volume("arbitrary_shape", base_area=10, height=7))  # Output: 70