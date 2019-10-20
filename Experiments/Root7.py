import math
cycles=int(input("Enter the number of terms in expansion"))

coeff=1
value=0
n=1/3
pow=1
a=8
a3=2
# Calculate 7^1/3 using binomial
# 7^1/3 = (8-1)^1/3
# Expanding that using binomial
# 8^1/3 -1/3*8^(1/3-1)+1/3*(1/3-1)/2 * 8^(1/3-2)
# 8^1/3 -1/3*8^(1/3-1)+1/3*(1/3-1)/2 * 8^(1/3-2)
# and 8^n=2^(3n)

for i in range(cycles):
    coeff = math.pow(-1, i)
    for j in range(i):
        coeff=coeff*(n-j)/(j+1)
    pow=pow-3*i
    value = value + (coeff * math.pow(a3, pow))

print(value)