import bank_lone
import simple_int

p = int(input("Enter principal amount is: "))
r = int(input("Enter rate of interest is: "))
t = int(input("Enter the time is: " ))
n = simple_int.simple_interest(p,r,t)

p = int(input("Enter principal amount: "))
r = int(input("Enter annual interest rate: "))
t = int(input("Enter number of months: " ))
n = bank_lone.monthly_emi(p,r,t)