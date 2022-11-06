a = [10,25,30,20,10,50,60,40,80,50,40]

dup = set()
uniq = []
for x in a:
    if x not in dup:
        uniq.append(x)
        dup.add(x)

print("List is : ", dup)
