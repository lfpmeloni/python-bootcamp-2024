"""
exercises_day_6.py
Author: Felipe Meloni  
Date: 2024-10-21
Description: Loops
"""

# Calculate and print the runtime for every single exercise!

import time

""" 
start = time.time()
end = time.time()
runtime = end - start
print("Runtime: ", runtime)
 """

# Exercise 1)
# Write a script with a for loop, that prints out the even numbers between 1 and 30.

start = time.time()

for i in range (0, 30):
    if i%2 == 0:
        print(i)

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Optional: Research how to generate a random number. Use this number as the start of the loop, so that the loop goes from random number to random number + 30.

import random

start = time.time()

random_number = random.randint(1, 999999999)
for i in range(random_number, random_number+30):
    if i%2 == 0:
        print(i)

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 2)
# Write a program that calculates the sum of all numbers between 1 and 100. Use a while loop for this exercise and print the sum at the end.

start = time.time()

count = 0
i = 1
while i <= 100:
    count += i
    i += 1
print(count)

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

""" the pythonic way of doing this is: """

start = time.time()
print(sum(range(1,101)))
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# After this, put in a control statement, that breaks the loop, when the sum gets bigger than 1000. The printed sum should be then under 1000 and print the last added number.

start = time.time()

count = 0
i = 1
while i <= 100:
    if count + i > 1000:
        break
    count += i
    i += 1
print("Count was in ", count, "with last addition being ", i)

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 3)
# Write a script, that prints the Fibonacci series. The script should have a control, that you do not print values above a value of your choosing.
# The Fibonacci series starts as follows: 0,1,1,2,3,5,8,13, …

start = time.time()

x=0 # forelast fibonacci number
print(x)
y=1 # last fibonacci number
print(y)
z=0 # auxiliary
while x+y < 2200:
    z = x
    x = y
    y = z + x
    print(y)

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

""" a more pythonic approach """

start = time.time()

x, y = 0, 1 # Fibonaccis initial values
while x < 2200:
    print(x)
    x, y = y, x + y # Do both calculations on a single line to eliminate the auxiliary

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 4)
# Write a loop, that calculates the prime numbers for a range of numbers. Remember for this exercise what prime numbers are.
# Save the prime numbers in a list.

start = time.time()

primes = [2]
for i in range(3, 1000):
    if sum(i % p == 0 for p in primes) == 0:
        primes.append(i)
print(primes)    

end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

""" A more Pythonic way using Sieve of Eratosthenes """

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p +=1
    return [p for p in range(2, n + 1) if primes[p]]

start = time.time()
primes = sieve_of_eratosthenes(1000)
print(primes)
end = time.time()
runtime = end - start
print("Runtime: ", runtime, "\n")

# Exercise 5)
# Check if a given password is correct. For this there should be a string as input. This string needs to be compared with the actual password. As output generate a message whether the password was correct or not.

"""
true_psw = "jurassic park"
test_psw = input("> access main security grid\naccess: ")
if test_psw == true_psw:
    print("Access granted.")
else:
    print("YOU DIDN'T SAY THE MAGIC WORD!")
"""

# Exercise 6)
# Write a script that translates any given text into Pig Latin! Pig Latin is a children's language that operates according to the following rules:
# 1. The initial letter is moved to the end of the word: Word -> Ordw
# 2. Add -ay to the end -> Word -> Ordway
# 3. If the first letter is a vowel, step 1 is skipped.
# 4. For words starting with th or ch, the h is moved to the end as well -> They -> Eythay
# Step 1 is also skipped for silent consonants, but you do not need to consider this.
# Tip: Wikipedia explains how Pig Latin works: https://en.wikipedia.org/wiki/Pig_Latin

word = input("Pig Latin translator! Type a word to see magic: ")
vowels = ['a','e','i','o','u']
if word[0] in vowels: # Step 3: If start with vowel skip step 1
    if word[0] == 'c' or 't' and word[1] == 'h': # Step 4
        word = word[2:]+word[:2]
    word = word + 'ay' # Step 2
else:
    word = word[1:]+word[:1] # Step 1
    if word[0] == 'c' or 't' and word[1] == 'h': # Step 4
        word = word[2:]+word[:2]
    word = word + 'ay' # Step 2
print("Pig Latin word: ", word)

""" A more Pythonic approach """

# Pig Latin translator
word = input("Pig Latin translator! Type a word to see the magic: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']

# Step 4: Check for words starting with "th" or "ch"
if word[:2] in ['th', 'ch']:
    pig_latin = word[2:] + word[:2] + 'ay'
# Step 3: Check if the word starts with a vowel
elif word[0] in vowels:
    pig_latin = word + 'ay'
# Step 1 and Step 2: Consonant case
else:
    pig_latin = word[1:] + word[0] + 'ay'

print("Pig Latin word:", pig_latin)

# Exercise 7)
# Decode the Zen of Python from the this package. To do this, load the Zen via import this, and with this.s you will get the Zen of Python encoded in ROT-13. Decode this into readable text using loops and statements. Do NOT use encode() for this.
# Tip: More information about ROT-13: https://en.wikipedia.org/wiki/ROT13

import this
encoded_zen = this.s
rot13_input = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rot13_output = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
decoded_zen = ""
# Interate letter by letter
for char in encoded_zen:
    # If a letter switch from input to output using index
    if char in rot13_input:
        index = rot13_input.index(char)
        decoded_zen += rot13_output[index]
    # Else not a letter mantain inaltered
    else:
        decoded_zen+= char
print(decoded_zen)

# Exercise 8)
# Write a loop, that prints, if a letter in a string is a capital letter or small letter. The string should be from a input.

# Get the input string from the user
input_string = input("Enter a string: ")

# Loop through each character in the input string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char.isupper():
            print(f"'{char}' is a capital letter.")
        else:
            print(f"'{char}' is a small letter.")
    else:
        print(f"'{char}' is not a letter.")

# Exercise 9)
# Create an empty list that contains two empty lists as elements.
# Then write a loop (large loop) that varies the loop from task 1 (small loop) by making the end value of the small loop dependent on the iteration parameter of the large loop. So, in the first run, the small loop should run from 1 to 30, in the next run from 1 to 31, and so on.
# Measure the runtime of the small loop and store this in one of the sublists. In the second sublist, store the number of iterations (30, 31, ...).
# Create a graph where you visualize the runtime and the number of repeats of the loop.
# Tip: For the creating the graph you can use the matlibplot.pyplot package.
# Tip2: Choose larger parameters, to measure the runtime. E.g. 10000+

import matplotlib.pyplot as plt

results = [[], []]

large_loop_iterations = 1000

# large loop
for n in range(0, large_loop_iterations):
    # small loop
    start = time.time()
    print("Start of run: ", n)
    for i in range (1, 30+n):
        if i%2 == 0:
            #print(i)
            pass # The small loop does nothing 
    end = time.time()
    runtime = end - start
    print("Runtime: ", runtime, "\n")
    # Store the runtime and iteration number (number of iterations)
    results[0].append(n)
    results[1].append(runtime)

plt.plot(results[0], results[1], marker='o', linestyle='-', color='b', label='Runtime of small loop')
plt.xlabel('Number of Iterations')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime vs. Number of Iterations')
plt.grid(True)
plt.legend()
plt.show()