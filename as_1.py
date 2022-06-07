an_inc=float(input('enter annual income:'))
hra=float(input('enter allowance:'))
od=float(input('enter other deductions:'))
if(od>80000):
    od=80000
ta=an_inc-hra-od
if(ta<300000):
    tax=0
elif(300000<=ta<600000):
    tax=0.10*ta
elif(600000<=ta<1000000):
    tax=0.15*ta
else:
    tax=0.20*ta
print(tax)
