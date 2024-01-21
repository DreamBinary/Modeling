import numpy as np
import statsmodels.api as sm
import pylab as plt

a = np.array([[ 7.1,  6.8,  9.2, 11.4,  8.7,  6.6, 10.3, 10.6],
              [11.1, 10.8, 12.4, 10.9,  9.6,  9.0, 10.5, 12.4],
              [15.4, 15.0, 22.8, 27.8, 19.5, 13.1, 24.9, 26.2]])
# plt.rc('text', usetex=True)
# plt.rc('font', size=16)
plt.plot(a[0], a[2], '*', label='$x_1$')
plt.plot(a[1], a[2], 'o', label='$x_2$')
plt.legend(loc='upper left')
d = {'x1': a[0], 'x2': a[1], 'y': a[2]}
re = sm.formula.ols('y~x1+x2', d).fit()
print(re.summary())
print(re.params.values)
yh = re.predict({'x1': [9, 10], 'x2': [10, 9]})
print('残差的方差:', re.mse_resid)
print('预测值:', yh.values)
plt.show()
