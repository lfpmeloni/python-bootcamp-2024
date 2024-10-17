import os

print(os.listdir())

mytext = open('bsp.txt','r')

print(mytext)

x = mytext.read()

print(x)

print()
frage = 'Dein Alter?'
age = int(input(frage))
print(age, type(age))