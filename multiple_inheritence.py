class addition:
    def add(self,a,b):
        print(a+b)
class subtraction:
    def sub(self,a,b):
        print(a-b)
class multiplication:
    def mult(self,a,b):
        print(a*b)
class division:
    def div(self,a,b):
        print(a/b)
class result(addition, subtraction, multiplication, division):
    def _init_(self):
        super()
r = result()

r.add(4,5)
r.sub(5,8)
r.mult(5,6)
r.div(47,2)