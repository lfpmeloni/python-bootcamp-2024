"""
exercises_day_10.py
Author: Felipe Meloni  
Date: 2024-10-25
Description: Recursive Functions
"""

# Exercise 2)
# Attention! This exercise is more complex, please don’t get discouraged if it doesn’t work. If you can’t solve this exercise today, then that’s ok. Its more important that you try to find a solution to this problem. But sadly, sometime solutions are wrong. Shit happens.
# You shouldn’t just start with the exercise. Beforehand you should think about the problem and try to think of ways to solve it. You are supposed to use a recursive function, but if you only find a solution without one, then do that. I’d like to see that solution!
# Outline how you should proceed and talk to others.
# Your exercise is to write a function for merge sorting. For mor information on merge sorting you can come and talk to me or ask Wikipedia (https://en.wikipedia.org/wiki/Merge_sort). The video of the sorting: https://www.youtube.com/watch?v=kPRA0W1kECg
# What you should take from this exercise is: How do I start on a problem? What purpose should the smaller parts of the function fulfil?
# Tipp: Merge sort is a very often used technique. You can easily find a solution for merge sort in python online. But please: Try to do it yourself first!
# If you have a functioning solution at the end, please upload your script at KLR337 -> MergeSort -> YourName.py
# I will run all solutions and compare the runtime. The solution of this will be presented on Monday
# The script to run the comparison can be found in the same folder vergleich_mergesort.py

import time
import random

# On merge sort the first step is break the list in smaller ones until  you have individual units

def merge_sort(list) -> list:
    """
    Sorts a list using the merge sort algorithm.

    This function takes a list of elements and recursively divides it into smaller sublists until each sublist contains a single element or is empty. Then, it calls the merge function to merge those sublists back together in sorted order.

    Args:
        lst (list): The list of elements to be sorted.

    Returns:
        list: A new sorted list containing all elements from the input list.
    """    
    if len(list) <= 1:
        return list
    else:
        left = []
        right = []
        for index, x in enumerate(list):
            if index < (len(list)/2):
                left.append(x)
            else:
                right.append(x)
        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right) # We have to build this function

# Then you compare the first unit with the second and sort from smaller to bigger. Then the third with second, and so on

def merge(left, right) -> list:
    """
    Merges two sorted lists into a single sorted list.

    This function takes two sorted lists and combines them into a single sorted list by comparing the first elements of each list and appending the smaller element to the result list until all elements from both lists have been processed.

    Args:
        left (list): The first sorted list to merge.
        right (list): The second sorted list to merge.

    Returns:
        list: A new sorted list containing all elements from both input lists.
    """    
    result = []
    while left and right: # Pythonic way to check if both lists are not empty
        if left[0] <= right[0]: # Compare the first elements
            result.append(left[0]) # Append the first element of left to result
            left = left[1:] # Update left removing first element
        else: # Do the same to right if first right element is smaller
            result.append(right[0])
            right = right[1:]

    # If there are any remaining elements left in only one list
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]

    return result


# Lets start by starting a list:
my_list = [random.uniform(0.0, 1000.0) for _ in range(10000)]

start = time.time()
merge_sort(my_list)
end = time.time()
runtime = end - start
print("Runtime script 1: ", runtime, "\n")
