"""
exercises_day_16.py
Author: Felipe Meloni  
Date: 2024-11-05
Description: Generator and Iterator
"""

from dataclasses import dataclass, field, asdict, astuple


@dataclass(order=True)
class Teilnehmer:
	sort_index: int = field(init=False, repr=False)
	age: int
	name: str
	legal_drinking: bool = field(init=False)

	def __post_init__(self):
		self.legal_drinking = self.age >= 18
		self.sort_index = self.age

	def printAttributes(self):
		print(f'{self.name} is {self.age} years old')


bsp_teilnehmer = Teilnehmer(7, 'Shiva')
bsp_teilnehmer2 = Teilnehmer(1, 'Luna')
bsp_teilnehmer3 = Teilnehmer(14, 'Tessy')
bsp_teilnehmer4 = Teilnehmer(3210, 'Medusa')

print(bsp_teilnehmer)
#bsp_teilnehmer.printAttributes()
print(asdict(bsp_teilnehmer))
print(astuple(bsp_teilnehmer))

myteilnehmer = [bsp_teilnehmer4, bsp_teilnehmer2, bsp_teilnehmer, bsp_teilnehmer3]
print(myteilnehmer)
myteilnehmer_sort = sorted(myteilnehmer)
print(myteilnehmer_sort)


''' 4 Methods to calculate the fibonacci sequenz '''

'''As recursiv function'''


def fib_recu(n):
	if n <= 1:
		return n
	else:
		return (fib_recu(n - 1) + fib_recu(n - 2))


for i in range(14):
	print(fib_recu(i))

''' As iterator '''


class FibIter:
	def __init__(self, howMany):
		self.counter = howMany
		self.curFib = 0
		self.nextFib = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.counter == 0:
			raise StopIteration

		self.counter -= 1

		nextFib = self.curFib + self.nextFib
		self.curFib = self.nextFib
		self.nextFib = nextFib

		return self.curFib


for fib in FibIter(14):
	print(fib)

''' As generator '''
stop_point = 600
fib_out = [0, 1]
while fib_out[-1] < stop_point:
	print(fib_out)
	fib_out.append(fib_out[-1] + fib_out[-2])

''' As generator function '''


def fib_fkt():
	a = 0
	b = 1
	while True:
		yield a
		a, b = b, a + b


counter = 0
stop_counter = 14
for x in fib_fkt():
	print(x, " ", end="")
	counter += 1
	if (counter > stop_counter):
		break
