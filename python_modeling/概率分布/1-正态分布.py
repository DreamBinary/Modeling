###------------------------------------------------------------------------###
# *scipy.stats.norm.pdf()函数用于生成正态分布分布下输入值对应函数值
# *第一个参数x：正态分布中的横坐标
# *参数loc：设置正态分布的平均值
# *参数scale：设置正态分布的标准差
###
# *scipy.stats.norm.cdf()函数用于生成正态分布分布下输入值处累计的函数值
# *各参数与pdf()函数相同
###------------------------------------------------------------------------###

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x = np.linspace(-5, 5, 100)
y0 = norm.pdf(x)
y1 = norm.pdf(x, loc=2)
y2 = norm.pdf(x, loc=-2)
y3 = norm.pdf(x, scale=0.5)
y4 = norm.pdf(x, scale=2)

plt.plot(x, y0, c='red', label="(0,1²)")
plt.fill_between(x, y0, color="red", alpha=0.25)
plt.plot(x, y1, c='blue', label="(-2,1²)")
plt.plot(x, y2, c='green', label="(2,1²)")
plt.plot(x, y3, c='yellow', label="(0,0.5²)")
plt.plot(x, y4, c='orange', label="(0,2²)")

plt.legend()
plt.show()


yc = norm.cdf(x)
plt.scatter(x, y0, color='red', alpha=1)
plt.plot(x, yc)
plt.show()
