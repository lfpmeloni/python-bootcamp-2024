"""
exercices_day_1.py
Author: Felipe Meloni  
Date: 2024-10-14
Description: First steps in Python
"""

#Exercise 3)
#Calculate and print the following:
#▪ 3+4
#▪ 4/2
#▪ 3*3
#▪ 3-4

print(3+4)
print(4/2)
print(3*3)
print(3-4)

#Exercise 4)
#Assign an arbitrary value to a variable

variable = 4

#Exercise 5)
#Add 5 to the new variable of exercise 4) and store the result in #a new variable.

new_variable = variable + 5

# Exercise 6)
# Display the value of the variable from exercise 4) and exercise 5) once combined in a single
# command, and once separately. What difference do you observe?

print(variable, new_variable)
print(variable)
print(new_variable)

""" Response: When combined it comes in a single line and separately it breaks lines """

# Exercise 7)
# Look at the Structure of your script.

""" Response: Would the equivalent of Structure in PyCharm be the Outline View in Visual Studio Code? Ctrl+Shift+O shows the varibles created but in complete projects should also bring functions, classes, methods, etc. """

# Exercise 8)
# Calculate and print the following:
# - 3*4-5/6
# - 4-8*(3/2)+9
# - 5/2-3*(5-1)
# - 3/(5*8-(4/2)*3)

print(3*4-5/6) #11.166666666666666
print(4-8*(3/2)+9) #1.0
print(5/2-3*(5-1)) #-9.5
print(3/(5*8-(4/2)*3)) #0.08823529411764706

# Extra)
# Create a script that converts Celsius to Fahrenheit and another script that converts Fahrenheit to
# Celsius.

temp_in_c = 32  #Temperature in Celsius input
temp_in_f = 89  #Temperature in Fahrenheit input

def c_to_f (temp_in):
    """ Convert input in Celsius to Fahrenheit and print """
    temp_out = (9/5)*temp_in+32
    print(temp_out, "F")

def f_to_c (temp_in):
    """ Convert input in Fahrenheit to Celsius and print """
    temp_out = (5/9)*(temp_in-32)
    print(temp_out, "C")

c_to_f(temp_in_c)
f_to_c(temp_in_f)