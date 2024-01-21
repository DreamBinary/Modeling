import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


def showErrorBar(result, datas):
    """绘制数据预测残差分布图"""
    pre = result.get_prediction(datas)
    df = pre.summary_frame(alpha=0.05)
    dfv = df.values
    low, upp = dfv[:, 4:].T  # 置信下限上限
    r = (upp-low)/2  # 置信半径
    num = np.arange(1, len(x0)+1)
    plt.errorbar(num, result.resid, r, fmt='o')


x0 = np.array([0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.20, 0.22, 0.24])
y0 = np.array([42.0, 42.5, 45.0, 45.5, 45.0, 47.5, 49.0, 51.0, 50.0, 55.0, 57.5, 59.5])
datas = {'x': x0, 'y': y0}
result = sm.formula.ols('y~x', datas).fit()  # 拟合线性回归模型
print(result.summary())
print(result.outlier_test())  # 输出已知数据的野值检测
print('残差的方差:', result.mse_resid)  # 残差的方差
print(result.predict({"x": 0.2}))  # 预测
pre = result
showErrorBar(result, datas)
plt.show()
