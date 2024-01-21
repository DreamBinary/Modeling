###------------------------------------------------------------------------###
# *scipy.stats.uniform.pdf()函数用于生成均匀分布下输入值对应函数值
# *第一个参数x：均匀分布的横坐标
###
# *scipy.stats.uniform.cdf()函数用于生成均匀分布下输入值处累计的函数值
# *各参数与pdf()函数相同
###------------------------------------------------------------------------###

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform

plt.rcParams['axes.unicode_minus'] = False

x1 = np.linspace(0, 1, 20)
y1 = uniform.pdf(x1)
yc = uniform.cdf(x1)
x2 = np.linspace(-2, 2, 20)
y2 = uniform.pdf(x2)
x3 = np.linspace(-5, 5, 20)
y3 = uniform.pdf(x3)
x4 = np.linspace(-2, 2, 50)
y4 = uniform.pdf(x4)

plt.plot(x1, y1, color="red")
plt.plot(x2, y2, color="green", alpha=0.7)
plt.plot(x3, y3, color="yellow", alpha=0.7)
plt.plot(x4, y4, color="blue", alpha=0.7)
plt.show()

plt.scatter(x1, y1, color="red")
plt.plot(x1, yc, color="blue")
plt.show()
