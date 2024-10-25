"""
exercises_day_10.py
Author: Felipe Meloni  
Date: 2024-10-25
Description: Recursive Functions
"""

# Exercise 1)
# Take your exercise of this week. Try to solve every exercise where you used a loop to solve with a
# recursive function.

# for i in range (0, 30):
#     if i%2 == 0:
#         print(i)
# The function above takes a range and prints the even numbers between 1 and 30

"""
def even_numbers():
    print()


count = 0
i = 1
while i <= 100:
    if count + i > 1000:
        break
    count += i
    i += 1
print("Count was in ", count, "with last addition being ", i)




x, y = 0, 1 # Fibonaccis initial values
while x < 2200:
    print(x)
    x, y = y, x + y # Do both calculations on a single line to eliminate the auxiliary

primes = [2]
for i in range(3, 1000):
    if sum(i % p == 0 for p in primes) == 0:
        primes.append(i)
print(primes)

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p +=1
    return [p for p in range(2, n + 1) if primes[p]]
"""
# Function 1: Print if number is even up to 30

def even_number(start=0, end=30):
    if start > end:
        return
    if start % 2 == 0:
        print(start)
    even_number(start + 1, end)

even_number()
even_number(40,100)

# Function 2: Count up to 100 andf stop before sum passes 1000

def count_function(i=1, count=0):
    if i > 100 or count + i > 1000:
        return count, i
    return count_function(i + 1, count + i)

count, last_i = count_function()
print("Count was in", count, "with last addition beign", last_i)

# Function 3: Fibonacci sequence

def fibonacci_recursive(x=0,y=1):
    if x>=2200:
        return
    print(x)
    fibonacci_recursive(y, x+y)

fibonacci_recursive()

