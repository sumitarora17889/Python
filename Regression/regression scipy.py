import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
X=np.arange(30)
Y = [39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]

plt.scatter(X,Y)
slope, intercept, rvalue, pvalue, stderr = stats.linregress(X,Y)
Ypred=intercept + slope*X
plt.plot(X,Ypred)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Regression X-Y')
plt.show()
print('X vs Y\r\nEquation: Y=%s+%sX\r\n rvalue: %s\r\n pvalue: %s\r\nstderr: %s' %(intercept,slope,rvalue,pvalue,stderr))
