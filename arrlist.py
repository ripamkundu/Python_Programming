l =[]
print("How Mnay Number You Want ?")
n=int(input())
print("Give " + str(n) + " Data List For")
for i in range(n):
    print("Enter Data list : ")
    d = int(input())
    l.append(d)

p =[]
print("How Mnay Number You Want ?")
n=int(input())
print("Give " + str(n) + " Data List For")
for i in range(n):
    print("Enter Data list : ")
    d = int(input())
    p.append(d)
t = []
for i in range(n):
    t.append(l[i] + p[i])
print("Sum of result is : "+str(t))
