a = ['A', 'B', 'C', 'D']
b = [10, 20, 30, 40]
def combine(a,b):
    l = []
    for i in range(len(a)):
        l.append(a[i])
        l.append(b[i])
    return l
print(combine(a,b))
