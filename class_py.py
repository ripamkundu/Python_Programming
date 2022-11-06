class A:
	def test(self):
		print("Test of A Called")
class B(A):
	def test(self):
		print("Test of B Called")
		super().test()

class C(A):
	def test(self):
		print("Test of C Called")
		super().test()

class D(B, C):
	def test2(self):
		print("Test of D Called")
ob = D()
ob.test()
