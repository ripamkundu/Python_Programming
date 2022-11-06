#Sort a Dictionary by Value

data = {5:4, 1:6, 6:3, 4:2, 9:3, 5:-2, -6:2}
sorted = {key: value for key, value in sorted(data.items(), key = lambda item: item[1])}
print(sorted)