#Write a python program Insert a node a single element. 

class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next
class LinkedList:
  def __init__(self):  
    self.head = None
    self.last_node = None
 
  def append(self, data):
    if self.last_node is None:
        self.head = Node(data)
        self.last_node = self.head
    else:
        self.last_node.next = Node(data)
        self.last_node = self.last_node.next
        
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
      
  def Display(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
      
if __name__ = "__main__":
 l = LinkedList()
 print("How many Elemnet would you like to want : ")
 for i in range(n):
    n = int(input("Enter the data : ")
    l.append(data)
print("The Link list is  : ", end =' ')
l.Display()