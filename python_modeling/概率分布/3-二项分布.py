###------------------------------------------------------------------------###
# *scipy.stats.binom.pmf()函数用于生成二项分布下输入值对应函数值
# *第一个参数k：事件发生（为1）的次数
# *参数p：设置事件发生（为1）的概率
# *参数n：设置重复次数
###
# *scipy.stats.binom.cdf()函数用于生成二项分布下输入值处累计的函数值
# *各参数与pdf()函数相同
###------------------------------------------------------------------------###

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

plt.rcParams['font.sans-serif'] = ['SimHei']

x = np.arange(40)
y1 = binom.pmf(x, p=0.5, n=40)
y2 = binom.pmf(x, p=0.5, n=20)
y3 = binom.pmf(x, p=0.5, n=60)
y4 = binom.pmf(x, p=0.25, n=40)
yc = binom.cdf(x, p=0.5, n=40)

plt.plot(x, y1, color="red", label="p=0.5,n=40")
plt.fill_between(x, y1, color="red", alpha=0.25)
plt.plot(x, y2, color="green", label="p=0.5,n=20")
plt.plot(x, y3, color="yellow", label="p=0.5,n=60")
plt.plot(x, y4, color="blue", label="p=0.25,n=40")
plt.xlabel("事件成立（为1）的次数")
plt.legend()
plt.show()

plt.scatter(x, y1, color="red")
plt.plot(x, yc, color="blue")
plt.xlabel("事件成立（为1）的次数")
plt.show()
