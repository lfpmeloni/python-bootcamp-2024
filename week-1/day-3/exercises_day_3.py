# Part 1: Date and Time
# Exercise 1)
# Save the current date and time as a variable.

import datetime

current_time = datetime.datetime.now()
print(current_time)

# Exercise 2)
# Figure out, how to access and print the elements (year, month, day, hour, etc.) of the datetime.
# Hints: PyCharm gives you some hints!

print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hours:", current_time.hour)
print("Minutes:", current_time.minute)
print("Seconds:", current_time.second)

# Part 2: String Manipulation
# Exercise 3)
# Save the zen of python as a block string.
# Hint: You can use the function import this to print the zen.
# Hint 2: It is possible to save the zen as a block string, but not with the known packages.

#import this
#print(this)

zen_of_python = """ 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
#print(zen_of_python)

# Exercises 4) to 13) are for the zen of python. Save every change in a separate variable and print it.
# Exercise 4)
# Delete all P in the variable.

zen_no_p = zen_of_python.replace("P","").replace("p","")
#print(zen_no_p)

# Exercise 5)
# Split the variable at every y.

zen_split_y = zen_of_python.split("y")
#print(zen_split_y)

# Exercise 6)
# Split the variable at every dot.

zen_split_dot = zen_of_python.split(".")
#print(zen_split_dot)

# Exercise 7)
# Replace every y with a Y.

zen_y_to_y = zen_of_python.replace("y","Y")
#print(zen_y_to_y)

# For the following Exercises you can find the pdf String_Befehle in the Datenaustausch. For further
# questions go to the documentation.
# Exercise 8)
# Figure out at which index the word complex is in the variable.

print("'Complex' index:", zen_of_python.find("complex")) #123
print(zen_of_python[zen_of_python.find("complex"):zen_of_python.find("complex")+7])

# Exercise 9)
# Figure out how often the word “than” is used in the variable.

print("Count of 'than:'",zen_of_python.count("than"))

# Exercise 10)
# Replace every dot with a {}
# - Figure out how often {} is inside the variable.
# - Print the variable with a number in every {}.

zen_var_dot = zen_of_python.replace(".","{}")
dot_count = zen_var_dot.count("{}")
for i in range(1, dot_count+1):
    zen_var_dot = zen_var_dot.replace("{}",str(i),1)
print(zen_var_dot)

# Exercise 11)
# How long is this variable?

print("Is ",len(zen_var_dot)," char long")

# Exercise 12)
# How many whitespaces are inside the variable?

print("Whitespaces: ",zen_var_dot.count(" "))

# Exercise 13)
# How long is the variable without the whitespaces and without the dots?

print("Size of letters: ",len(zen_of_python.replace(" ","").replace(".","")))

# Exercise 14)
# Save your name as a variable.
# Exercises 15) to 18) are for your name as variable.

my_name = "Luis Felipe Pellegrini Meloni"

# Exercise 15)
# Delete every whitespace in the variable.

print(my_name.replace(" ",""))

# Exercise 16)
# Change the format of the variable to the following:
# - Only capital letters
# - Only small letters
# - Every first letter as capital, the rest small
# - Every first letter as small, the rest capital

print(my_name.upper())
print(my_name.casefold())
print(my_name.title())
print(my_name.title().swapcase())

# Exercise 17)
# Add your age to your name.

my_age = "32 years old"
print(my_name+my_age)
#print(my_name," ",my_age)

# Exercise 18)
# Fill the variable from the beginning with three zeros.
# Hint: Remember that a string is a list.

print(my_name.zfill(len(my_name)+3))

# Afterward: Assist other participants (which will help you understand the content better) or read the
# book "Python 3 Crashkurs" or try out the other commands from the pdf String_Befehle.