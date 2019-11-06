import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
# Creating a dummy dataset
x=np.arange(30)
y = [39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]

#y=ax + b
a=np.sum((x-np.mean(x))*(y-np.mean(y)))/np.sum(np.power((x-np.mean(x)),2))
c=np.mean(y)-a*np.mean(x)
print(a,c)
print('y=%sx+%s'%(a,c))
ypred=a*x+c
plt.scatter(x,y, color ='red')
plt.plot(x,ypred, color ='blue')
plt.title('Show')   
plt.show()