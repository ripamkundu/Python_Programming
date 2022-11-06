n = input("Please enter your thought: ")
f=open('write.txt', 'w')
f.write(n)
f.close()
f = open('write.txt', 'r')
data = f.read()
print(data)

with open('write_1.txt','a')as f:
    f.write(data)
    f.close()
    
f=open("write_1.txt","r")
print(f.read())
