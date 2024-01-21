###------------------------------------------------------------------------###
# *scipy.stats.poisson.pmf()函数用于生成泊松分布下输入值对应函数值
# *第一个参数k：泊松分布中的横坐标
# *参数mu：设置泊松分布最大值处
###
# *scipy.stats.poisson.cdf()函数用于生成泊松分布下输入值处累计的函数值
# *各参数与pdf()函数相同
###------------------------------------------------------------------------###

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

x = np.arange(20)
y1 = poisson.pmf(x, mu=5)
y2 = poisson.pmf(x, mu=10)
y3 = poisson.pmf(x, mu=15)
y4 = poisson.pmf(x, mu=1)
yc = poisson.cdf(x, mu=5)


plt.plot(x, y1, color="blue", label="μ=5")
plt.fill_between(x, y1, color="blue", alpha=0.25)
plt.plot(x, y2, color="green", label="μ=10")
plt.plot(x, y3, color="yellow", label="μ=15")
plt.plot(x, y4, color="red", label="μ=1")
plt.legend()
plt.show()


plt.bar(x, y1, width=0.75, alpha=0.75)
plt.plot(x, yc, color="#fc4f30")
plt.show()
