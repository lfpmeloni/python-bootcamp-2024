# Übung
# • Teil 1: Einführung:
# • Sucht für alle vier Objekttypen die Dokumentation.

""" On notes of day 5 """

# • Erstellt zu jedem Objekttyp ein Objekt

my_list = [1,2,3]
my_tuple = (1,1,2,3)
my_dict = {'number':1,'name':'one'}
my_set = {1, 2, 3, 4, "banane"}

# • Wendet alle hier besprochenen Methoden an
my_list.remove(1)
my_list.append(0)
#print(my_list.append(4)) -> None
print(my_list)

my_list.append('5')
my_list.insert(1,99)
print(my_list)

my_list.extend([7,8,9])
print(my_list)

print(my_set)
my_set.remove(4)
my_set.discard(2)
my_set.add("Tschüss")
my_set.update([3,2,0])
print(my_set)

my_list.remove('5')
print(sorted(my_list, reverse = True))

print(my_list.index(99))
print(my_list.pop(0))

newlist = my_list.copy()
print(newlist)
newlist = my_list[:]
print(newlist)

n = my_dict.get('name')
print(n)

my_dict.pop('number')
print(my_dict)

# • Wendet mindestens eine Methode zu jedem Objekttyp an, die hier nicht besprochen wurde

my_list.reverse() # Reverses the oprder of the elements
my_tuple.count(1) # Counts how many 1 there is
my_dict.update({'color':'red'}) # Adds new key value set
new_set = {9, 99 ,3, 4, "banane"}
print(my_set.intersection(new_set))

# • Teil 2: Ausprobieren:
# • Was passiert wenn
# • mytuple=(mylist, 3, 6)

my_tuple=(my_list, 3, 6)
print(my_tuple) 

""" A tuple now holds reference to a list and not a copy of it so any changes to my_list will be reflected inside my_tuple """

# • mynewlist = mylist

new_list = my_list

""" This points to the same list as my_list and are pointing to the same list in memory """

# • mylist.append(8)

my_list.append(8)

""" appends 8 to the original list and will also be visible when accessing new_list """

# • print(mynewlist, mytuple)

print(my_list,my_tuple)

""" Will print the updated list, including the appended 8 """

# • Versucht zu verstehen, was hier passiert -> Tiefere Erklärung folgt Donnerstag mit den Referenzen