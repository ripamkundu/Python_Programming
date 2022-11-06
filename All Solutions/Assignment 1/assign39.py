# Catch Multiple Exceptions in One Line

string = input("Enter Value : ")
try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)