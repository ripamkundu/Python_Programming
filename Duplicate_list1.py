n = eval(input("Enter a List : "))
ls =[]
c = 0
for i in range(len(n)):
    for j in range(len(n)):
        if(n[i] + n[j]):
            c = c+1
    if(c > 1):
        if(n[i] not in ls):
            ls.append(n[i])
    c = 0
print("Orginal list Is : ",n)
print("Duplicate Number form a list : ", ls)

    