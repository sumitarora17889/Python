import numpy as np
import statsmodels.api as sm

import matplotlib.pyplot as plt

X=np.arange(30)
Y = [39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
x = sm.add_constant(X)
# print(X)
# beta = [3,  5]
# y = np.dot(X, beta) + noise

# Fit regression model
# class statsmodels.regression.linear_model.OLS(endog, exog=None, missing='none', hasconst=None, **kwargs)[source]
# OLS= Ordinary Least Squares
# endogarray_like
# A 1-d endogenous response variable. The dependent variable.

# exogarray_like
# A nobs x k array where nobs is the number of observations and k is the number of regressors. An intercept is not included by default and should be added by the user.

# missingstr
# Available options are ‘none’, ‘drop’, and ‘raise’. If ‘none’, no nan checking is done. If ‘drop’, any observations with nans are dropped. If ‘raise’, an error is raised. Default is ‘none’.

# hasconstNone or bool
# Indicates whether the RHS includes a user-supplied constant. If True, a constant is not checked for and k_constant is set to 1 and all result statistics are calculated as if a constant is present. If False, a constant is not checked for and k_constant is set to 0.

# **kwargs
# Extra arguments that are used to set model properties when using the formula interface.

model = sm.OLS(Y, x).fit()

# Inspect the results
print(model.summary())
print(model.params)

plt.scatter(X,Y)
Ypred=model.params[0] + model.params[1]*X
plt.plot(X,Ypred)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Regression X-Y')
plt.show()
