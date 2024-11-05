"""
exercises_day_16.py
Author: Felipe Meloni  
Date: 2024-11-04
Description: Inheritance in Python
"""

# Beispiel von Vererbung

# class Dog:
#     """ class for dogs, without inheritance"""
#     def __init__(self, name, color, breed):
#         self.name = name
#         self.color = color
#         self.breed = breed
#
#
# class Cat:
#     """ class for cats, without inheritance"""
#     def __init__(self, name, color, breed):
#         self.name = name
#         self.color = color
#         self.breed = breed
#
#
# class Bird:
#     """ class for birds, without inheritance"""
#     def __init__(self, name, color, breed):
#         self.name = name
#         self.color = color
#         self.breed = breed


# class with inheritance
# class Animal:
#     """ superclass for animals, with inheritance"""
#     def __init__(self, name_super, color_super, breed_super):
#         self.name = name_super
#         self.color = color_super
#         self.breed = breed_super
#
#
# class Dog(Animal):
#     """ class for dogs, with inheritance"""
#     def __init__(self, name_dog, color_dog, breed_dog):
#         self.name = 'Pupi'
#         super().__init__(color_super=color_dog, breed_super=breed_dog, name_super='Schnarchnase')
#
#
#
# class Cat(Animal):
#     """ class for cats, with inheritance"""
#     def __init__(self, name, color, breed, free_roamer):
#         Animal.__init__(self, name, color, breed)
#         self.free_roamer = free_roamer
#
#
# class Bird(Animal):
#     """ class for birds, with inheritance"""
#     def __init__(self, name_bird, color_bird, breed_bird, singing):
#         super().__init__(name_bird, color_bird, breed_bird)
#         self.singing = singing
#
#
# dog1 = Dog('Shiva', 'black', 'Mud')
# cat1 = Cat('Mina', 'Ginger', 'Ragdoll', True)
# print(dog1.name)

# class with inheritance and method
class Animal:
	""" superclass for animals, with inheritance"""

	def __init__(self, name: str = 'Bla',
	             color: str = 'Bunt',
	             breed: int = 0):
		self.name = name
		self.color = color
		self.breed = breed
		self.sound = "Never more!"

	def makingSound(self):
		print(f"{self.name} says: {self.sound}")

	def __str__(self):
		return f'{self.__class__.__name__}: {vars(self)}'


class Dog(Animal):
	""" class for dogs, with inheritance"""

	def __init__(self, name: str, color: str, breed_dog: str = 'Idiot'):
		super().__init__(name, color, breed_dog)
		self.breed = 'Schnarchnase'
		self.sound = "Woof!"

	def __str__(self):
		return 'bla ' + super().__str__()


class Bird(Animal):
	""" class for birds, with inheritance"""

	def __init__(self, name, color, breed, singing):
		super().__init__(name, color, breed)
		self.singing = singing
		self.set_sound(self.singing)

	def set_sound(self, singing):
		self.singing = singing
		if self.singing:
			self.sound = "Chirp Chirp!"
		else:
			self.sound = "Kwack Kwack!"


class Cat(Animal):
	""" class for cats, with inheritance"""

	def __init__(self, name, color, breed, free_roamer):
		super().__init__(name, color, breed)
		self.free_roamer = free_roamer
		self.sound = "Miau!"

	def __str__(self):
		return 'Cat: was anderes\t' + Animal.__str__(self)


dog1 = Dog('Shiva', 'black', 'Mud')
birdy = Bird('Tweety', 'Bunt', 'Kanarienvogel', True)
cat1 = Cat('Armageddon', 'Ginger', 'Mud', True)

birdy.makingSound()
birdy.set_sound(False)
birdy.makingSound()

print(dog1)
print(birdy)
print(cat1)

# class Animal:
#     """ superclass for animals, with inheritance"""
#     def __init__(self, name, color, breed):
#         self.name = name
#         self.color = color
#         self.breed = breed
#         self.sound = "Never more!"
#
#     def makingSound(self):
#         print(f"{self.name} says: {self.sound}")
#
#
# class Mammal:
#     """ superclass for mammals, with inheritance"""
#     def __init__(self, num_nipple, gestation_period):
#         self.num_nipple = num_nipple
#         self.gestation_period = gestation_period
#
#     def makingSound(self):
#         print(f"No Sound, but {self.num_nipple} nipple!")
#
#
# class Dog(Animal, Mammal):
#     """ class for dogs, with inheritance"""
#     def __init__(self, name, color, breed, gestation_period):
#         super().__init__(name, color, breed)
#         self.sound = "Woof!"
#         Mammal.__init__(self,
#                         num_nipple=8,
#                         gestation_period=gestation_period)