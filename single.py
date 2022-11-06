class Base:
 def __init__(self,data):
  self.data = data
 def show(self):
  print("\n Data \t:",self.data)
  
class Derived(Base):
 def __init__(self,data,data1):
  self.data1 = data1
  Base.__init__(self,data)
  
 def show(self):
  print("\n Data \t:",self.data1,"\n Base class Data \t",self.data)
  
X = Base(1)
X.show() #print(X.data)

Y = Derived(2,3)
Y.show()
