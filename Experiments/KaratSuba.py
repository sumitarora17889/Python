import math
177648187715183390
num1='5455455'
num2='754487458'
num1=num1.rjust(len(num2),'0')
num2=num2.rjust(len(num1),'0')
print(num1)
print(num2)

def multiply(num1,num2):
    mid = math.trunc(len(num2) / 2)
    multiply(num1[:mid],num2[:mid])
