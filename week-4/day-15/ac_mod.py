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
