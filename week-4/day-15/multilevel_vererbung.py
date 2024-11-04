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

