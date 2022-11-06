class Product:
    def __init__(self, pid, product_name, stock_balance, price):
        self.pid = pid
        self.product_name = product_name
        self.stock_balance = stock_balance
        self.price = price
    def show_data(self):
        print("Product Id : ", self.pid)
        print("Product name : ", self.product_name)
        print("Stock balance : ", self.stock_balance)
        print("Price : ", self.price)
        
    def issue_product(self,quantity):
        self.stock_balance = self.stock_balance - quantity
    
p1 = Product(101,"Banana",20,345)
p1.show_data()
p1.issue_product(5)
p1.show_data()


p2 = Product(102,"Apple",40,1200)
p2.show_data()
p2.issue_product(15)
p2.show_data()

p3 = Product(103, "Mango",40,1200)
p3.show_data()
p3.issue_product(10)
p3.show_data()
    