import scipy.stats as ss
from matplotlib import pyplot as plt

b = ss.norm.rvs(0, 1, size=1000)
xb = b.mean()
s = b.std(ddof=1)

res = ss.kstest(b, 'norm', (xb, s))
print(res)
res = ss.normaltest(b)
print(res)
res = ss.shapiro(b)
print(res)

plt.plot(range(len(b)), sorted(b))
plt.show()
