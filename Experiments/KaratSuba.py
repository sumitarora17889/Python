import math
from datetime import datetime
num1=9876789
num2=6756321

# def sum(*args):
#     sumval=0
#     for a in args:
#         sumval=sumval+int(a)
#     return str(sumval)
#
# def subtract(a,b,c):
#     return str(int(a)-int(b)-int(c))

def multiply(num1,num2):
    if num1==0 or num2==0:
        return 0
    mid = max(num1, num2).bit_length() >> 1
    if mid==0:
        return 0
    if mid==2:
        return num1&num2
    num11=num1>>mid
    num12=num1 & ((1<<mid)-1)
    num21=num2>>mid
    num22=num2 & ((1<<mid)-1)
    firsts=multiply(num11,num21)
    firstsecond=multiply(num12,num22)
    answer=(firsts<<(mid<<1))+  ((multiply((num11+num12),(num21+num22))-firstsecond-firsts)<<mid)+ firstsecond
    return answer

def multiply1(num1,num2):
    return num1*num2

start = datetime.now()
for i in range(5000):
    a=multiply(num1,num2)
end=datetime.now()
print((a,end-start))

start = datetime.now()
for i in range(5000):
    a=multiply1(num1,num2)
end=datetime.now()
print((a,end-start))

