import os

file = os.stat('assign4.py')
print("Result is : ",file.st_size)