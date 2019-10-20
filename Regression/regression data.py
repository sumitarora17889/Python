import numpy as np
import matplotlib.pyplot as plt
X=np.arange(30)
Y = [39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]

plt.scatter(X,Y)

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Regression X-Y')
# plt.show()
plt.scatter(X, Y)
A = np.vstack([X, np.ones(len(X))]).T
model = np.linalg.lstsq(A, Y, rcond=None)
Ypred=model[0][1] + model[0][0]*X
plt.plot(X,Ypred)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Regression X-Y')
plt.show()
print('X vs Y\r\nResidue: %s\t Equation: Y=%s+%sX' %(model[1][0],model[0][1],model[0][0]))
