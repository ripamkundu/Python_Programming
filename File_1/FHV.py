a = input("Enter some Contain : ")
f = open('Vowel.txt', 'w')
f.write(a)
f.close()

f = open('Vowel.txt', 'r')
n = f.read()
v = 0
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        v = v + 1
print("Number Of vowel in this file : ", v)