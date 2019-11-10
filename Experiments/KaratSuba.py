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
    bitlength=max(num1.bit_length(),num2.bit_length())
    if bitlength==0 or num1==0 or num2==0:
        return 0
    if bitlength==1:
        return num1*num2
    mid=bitlength>>1
    num11=num1>>mid
    mask=(1<<mid)-1
    num12=num1 & mask
    num21=num2>>mid
    num22=num2 & mask
    firsts=multiply(num11,num21)
    firstsecond=multiply(num12,num22)
    answer=(firsts<<(mid<<1))+  ((multiply((num11+num12),(num21+num22))-firstsecond-firsts)<<mid)+     firstsecond
    return answer

start = datetime.now()
for i in range(5000):
    a=multiply(num1,num2)
end=datetime.now()
print((a,end-start))

start = datetime.now()
for i in range(5000):
    a=num1*num2
end=datetime.now()
print((a,end-start))

