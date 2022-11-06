class A:
	def test(self):
		print("Test of a called")
class B(A):
	def test(self):
		print("Test of b called")
        super().test()
class C(A):
	def test(self):
		print("Test of C called")
        super().test()
class D(B,C):
	def test2(self):
		print("Test of D called")
obj = D()
obj.test()
