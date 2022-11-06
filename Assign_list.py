print("Enter Two Different list")
m = eval(input("Enter 1st List Of value : "))
n = eval(input("Enter 2nd List Of value : "))
l=[]
for i in range(len(m)):
    l.append(m[i] + n[i])
print("List Is : ",l)
