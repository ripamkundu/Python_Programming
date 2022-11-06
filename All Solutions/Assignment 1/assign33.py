#Access Index of a List Using for Loop

list = [[10], [20,30],[21, 44, 35], [46, 32, 22, 12],
            [23,65,41,21], [32, 25, 18], [76, 55], [12]]

for index, val in enumerate(list):
    print(index, val)