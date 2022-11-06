def compute(a,b):
    s = a + b
    m = a * b
    return s, m()
if __name__ = "__main__" :
    x = int(input("Enter Frist Number : "))
    y = int(input("Enter Second Number : "))
    r = compute(x, y)
    print("Result is : ", r)