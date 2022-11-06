class queue:
 def __init__(self,n):
  self.front = -1
  self.rear = -1
  self.a =[]
  self.n = n
 def overflow(self):
  if self.rear == (self.n-1):
   return True
  else:
   return False
 def underflow(self):
  if self.front == 1:
   return True
  else:
   return False
 def insert(self, data):
  if queue.overflow(Self):
   print("overflow")
  elif self.front == -1:
   self.front = self.front + 1
   self.rear =   self.rear + 1
   self.a.append(data)
   print("Front = ", str(self.front), "\tRear", str(self.rear),"\tData\t : ", str(self.a[self.rear]))
  else:
   self.rear =  self.rear+1
   self.a.append(data)
   print("Front = ", str(self.front), "\tRear", str(self.rear),"\tData\t : ", str(self.a[self.rear]))
 def delete(self):
  if self.front == -1:
    print("ubderflow")
    return (-1)
  elif self.front == self.rear:
   temp = self.a[self.front]
   print("Front = ", self.front)
   self.front =  -1
   self.rear = -1
   return temp
  else:
   temp =  self.a[self.front]
   self.front =  self.front + 1
   print("Front = ", self.front)
   return(temp)
  q = queue(5)
  q.insert(5)
  q.insert(3)
  q.insert(5)
  q.insert(9)
  q.insert(21)
  q.insert(71)
  i =  0
  while i<6:
   temp = q.delete()
   if temp!= -1:
    print(temp)
   else:
    print("ubderflow")
   i = i+1
