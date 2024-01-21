###------------------------------------------------------------------------###
# *scipy.stats.chi2.pdf()函数用于生成卡方分布下输入值对应函数值
# *第一个参数x：卡方分布的横坐标
# *参数df：设置自由度
###
# *scipy.stats.chi2.cdf()函数用于生成卡方分布下输入值处累计的函数值
# *各参数与pdf()函数相同
###------------------------------------------------------------------------###

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

x = np.arange(40)
y1 = chi2.pdf(x, df=20)
y2 = chi2.pdf(x, df=1)
y3 = chi2.pdf(x, df=10)
y4 = chi2.pdf(x, df=30)
yc = chi2.cdf(x, df=20)

plt.plot(x, y1, color="red", label="df=20")
plt.fill_between(x, y1, color="red", alpha=0.25)
plt.plot(x, y2, color="green", label="df=1")
plt.plot(x, y3, color="yellow", label="df=10")
plt.plot(x, y4, color="blue", label="df=30")
plt.legend()
plt.show()

plt.scatter(x, y1, color="red")
plt.plot(x, yc, color="blue")
plt.show()
