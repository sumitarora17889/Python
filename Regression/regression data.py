import numpy as np
import matplotlib.pyplot as plt
X=[1,1.5,2,2.5,3]

Y=[1,5,18,36,80]

# plt.plot(X,Y)
#
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Regression X-Y')
# plt.show()
residue=[]
slope=[]
intercept=[]
for i in range(1,6):
    Xpow=np.power(X,i)
    plt.plot(Xpow,Y)
    plt.xlabel('x^%s - axis'%i)
    plt.ylabel('y - axis')
    plt.title('Regression X^%s-Y'%i)
    plt.show()
    A = np.vstack([Xpow, np.ones(len(Xpow))]).T
    model = np.linalg.lstsq(A, Y, rcond=None)
    slope.append(model[0][0])
    intercept.append(model[0][1])
    residue.append(model[1][0])
sort_index=np.argsort(residue,kind = 'stable')
print(sort_index)
print('In the order of fitness')
for i in sort_index:
    print(i)
    print('X^%s vs Y\r\nResidue: %s\t Equation: Y=%s+%sX^%s' %(i,residue[i],intercept[i],slope[i],i))
