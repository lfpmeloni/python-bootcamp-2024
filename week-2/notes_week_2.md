# Content of Week 2

## Day 1

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


