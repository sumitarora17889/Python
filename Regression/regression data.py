import numpy as np
import matplotlib.pyplot as plt
X=np.arange(30)
Y = [39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]

plt.scatter(X,Y)

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Regression X-Y')
# plt.show()
residue=[]
slope=[]
intercept=[]
for i in range(1,6):
    plt.scatter(X, Y)
    Xpow=np.power(X,i)
    A = np.vstack([Xpow, np.ones(len(Xpow))]).T
    model = np.linalg.lstsq(A, Y, rcond=None)
    slope.append(model[0][0])
    intercept.append(model[0][1])
    residue.append(model[1][0])
    Ypred=model[0][1] + model[0][0]*Xpow
    plt.plot(X,Ypred)
    plt.xlabel('x^%s - axis' % i)
    plt.ylabel('y - axis')
    plt.title('Regression X^%s-Y' % i)
    plt.show()
sort_index=np.argsort(residue,kind = 'stable')
print(sort_index)
print('In the order of fitness')
for i in sort_index:
    print(i)
    print('X^%s vs Y\r\nResidue: %s\t Equation: Y=%s+%sX^%s' %(i,residue[i],intercept[i],slope[i],i))
