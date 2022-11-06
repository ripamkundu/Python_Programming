list = eval(input("Enter a list : "))
dup = []
n = 1
while n < len(list):
    for i in list:
        if list.count(i) != 1:
            list.remove(i)
            dup.append(i)
    n = n+1
list.sort()
print("Orginal list Is : ", list)
print("Duplicate list Is : ",dup)
print("New list Is : ", list+dup)