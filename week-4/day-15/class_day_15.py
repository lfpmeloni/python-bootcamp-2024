"""
class_day_15.py
Author: Felipe Meloni  
Date: 2024-11-04
Description: Inheritance in Python
"""

# Super and Sub Classes / Inheritance in Python

class SuperClass:
	class_attribute_puplic = None
	_class_attribute_protected = None
	__class_attribute_privat = None

	def __init__(self, para1, para2, para3):
		self.instanz_attribute_puplic = para1
		self._instanz_attribute_protected = para2
		self.__instanz_attribute_privat = para3

	def methodPuplic(self):
		# puplic method -> usabel everywere
		# prints the puplic attribute
		print("Public Data Member:", self.instanz_attribute_puplic)

	def _methodProtected(self):
		# protected method -> usable in SuperClass and SubClass
		# prints the protected attribute
		print("Protected Data Member:", self._instanz_attribute_protected)

	def __methodPrivat(self):
		# privat method -> usable ONLY in SuperClass
		# prints the privat attribute
		print("Private Data Member:", self.__instanz_attribute_privat)

	def accessPrivateMembers(self):
		# public method -> usable everywere
		# calls the privat method and prints the privat attribute
		self.__methodPrivat()


class SubClass(SuperClass):
	sub_puplic_class_attribute = super()._class_attribute_protected

	def __init__(self, para1, para2, para3):
		SuperClass.__init__(self, para1, para2, para3)
		# super().__init__(para1, para2, para3) # or this

	def accessProtectedMembers(self):
		# puplic method -> usable everywere
		# calls the protected method of SuperClass
		# print the protected attribute of SubClass
		self._methodProtected()

# Multilevel Inheritance

class Animal: # superclass
    def look(self):
        print('It\'s a animal!')


class Ape(Animal): # subclass 1
    def look(self):
        print('It\'s an ape!')


class Gorilla(Ape): # subclass 2
    def look(self):
        Animal.look()
        super().look()
        print('It\'s a gorilla!')


tier = Gorilla()
tier.look()

# Multiple Inheritance (vererbung) test

class A:
	def hi(self):
		print('Method A')

	def a(self):
		print('Method A')


class B:
	def hi(self):
		print('Method B')

	def b(self):
		print('Method B')


class C(A, B):
	def hi(self):
		print('Method C')

	def c(self):
		print('Method C')


class D(C, A):
	def hi(self):
		print('Method D')

	def d(self):
		print('Method D')


test = D()
test.hi()
# test.a()
# test.b()
# test.c()
# test.d()