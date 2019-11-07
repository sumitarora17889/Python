import math
from datetime import datetime
177648187715183390
num1='5455455'
num2='754487458'
print(num1)
print(num2)


def sum(*args):
    sumval=0
    for a in args:
        sumval=sumval+int(a)
    return str(sumval)

def subtract(a,b,c):
    return str(int(a)-int(b)-int(c))

def multiply(num1,num2):
    num1 = num1.rjust(len(num2), '0')
    num2 = num2.rjust(len(num1), '0')
    if len(num1)==0:
        return ''
    if len(num1)==1:
        return str(int(num1)*int(num2))
    mid = math.trunc((len(num2))/ 2)
    firsts=multiply(num1[:mid],num2[:mid])
    firstsecond=multiply(num1[mid:],num2[mid:])
    answer=sum(     firsts+('0'*((len(num1)-mid)*2)),   subtract(multiply(sum(num1[:mid],num1[mid:]),sum(num2[:mid],num2[mid:])),firstsecond,firsts)+('0'*(len(num1)-mid)),     firstsecond)
    return answer

start = datetime.now()
for i in range(5000):
    a=multiply(num1,num2)
end=datetime.now()
print(end-start)

start = datetime.now()
for i in range(5000):
    a=5455455*754487458
end=datetime.now()
print(end-start)

