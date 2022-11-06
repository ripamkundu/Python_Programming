import os

# folder path
file = r'E:\\Python Programming\\'
res = []

for path in os.listdir(file):
    if os.path.isfile(os.path.join(file, path)):
        res.append(path)
print(res)