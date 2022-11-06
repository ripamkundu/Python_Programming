class car:
 def getdata(self):
  self.num = input("Enter Registration Number : ")
  self.model = input("Enter car Model Number : ")
  self.make = input("Enter what you want makeing in your car :  ")
  self.year = input("Enter year : ")
  self.owner = input("Enter Name of the Owner : ")
 
 def putdate(self):
  print("Registration Number \t: ", self.num)
  print("Car Moder Number \t : ", self.model)
  print("Makeing is \t : ", self.make)
  print("Year \t : ", self.year)
  print("Name of the Owner \t : ", self.owner)
 
 def __init__(self):
  self.num = "HR51"
  self.model = "Maruti"
  self.make = "Engine"
  self.year =  2007
  self.owner = "Harsh"
 def __del__(self):
  print("done")
 
c1 = car("HR51", "Maruti", "Engine", 2007, "Harsh")
c1.getdata()
c1.putdate()
