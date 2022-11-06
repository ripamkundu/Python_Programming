class staff:
    def getdata(self):
        self.name=input("Enter the name :")
        self.salary=input("Enter a salary :")
    def putdata(self):
        print("Name \t:", self.name)
        print("salary \t :", self.salary)
class employee:
    def getdata(self):
        self.name=input("Enter a Employee department : ")
        self.pro=input("Enter a project name :")
    def putdata(self):
        print("Employee Department \t :", self.name)
        print("Project Name \t :", self.pro)
class company(staff,employee):
    def getdata(self):
        self.com=input("company Name :")
        staff.getdata(self)
        employee.getdata(self)
    def putdata(self):
        staff.putdata(self)
        employee.putdata(self)
        print("Company Name \t :", self.com)
if __name__=="__main__":
    x = staff()
    x.getdata()
    x.putdata()

    y = employee()
    y.getdata()
    y.putdata()

    z = company()
    z.getdata()
    z.putdata()

    

