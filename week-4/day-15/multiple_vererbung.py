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
