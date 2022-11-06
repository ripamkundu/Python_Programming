def monthly_emi(p,r,t):
 print('The principal is  :', p)
 print('The number of month is : ',t)
 print('The annual interest rate is : ',r)
 r = r / (12*100)
 emi = p * r * ((1+r)**t)/((1+r)**t - 1)
 print("Monthly EMI = ", emi)
