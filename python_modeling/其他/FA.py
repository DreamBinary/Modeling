import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer as FA
from scipy.stats import zscore


class MyFA(object):
    def __init__(self, n_components: int, rotation='varimax') -> None:
        """自己写的FA(因子分析)"""
        self.fa = FA(n_components, rotation=rotation)  # 构建模型

    def fit(self, X: pd.DataFrame):
        self.X = X
        self.fa.fit(X)  # 求解方差最大的模型
        return self

    def getFactorContributionRatio(self) -> np.ndarray:
        A = self.fa.loadings_
        gx = np.sum(A ** 2, axis=0)  # 计算信息贡献
        self.factorConRation = gx / sum(gx)
        return self.factorConRation

    def getFactorScore(self) -> np.ndarray:
        A = self.fa.loadings_
        D = np.diag(1 - np.sum(A ** 2, axis=1))  # 计算特殊方差
        D_ = np.linalg.inv(D)
        self.factorScoreCoef = D_ @ A @ np.linalg.inv(A.T @ D_ @ A)  # 计算因子得分函数系数
        self.factorScore = self.X @ self.factorScoreCoef  # 计算因子得分
        return self.factorScore


def calContributionRate(X) -> np.ndarray:
    R = np.corrcoef(X.T)
    w, v = np.linalg.eig(R)
    contribution_rate = sorted(w / sum(w), reverse=True)
    return np.array(contribution_rate)


if __name__ == "__main__":
    c = np.array([[100, 92.5, 97, 86, 103, 94.5, 95.5, 91, 90.5, 84.5, 83, 82, 88, 77.5, 83, 74, 60.5],
                  [107.5, 99, 93.5, 90.5, 89.5, 72, 65, 59, 63.5, 56, 44.5, 64, 56, 49, 52, 38, 38],
                  [108.5, 114, 110, 106, 75.5, 110, 81.5, 109.5, 71, 73.5, 93, 61, 38.5, 34, 19, 44.5, 23],
                  [61, 54.5, 46.5, 44, 47, 52, 51, 28.5, 61, 33, 34.5, 28, 21, 46.5, 37, 26.5, 12.5],
                  [67.5, 52, 57, 70, 68, 58, 66, 53, 55.5, 58.5, 47.5, 47, 59.5, 29, 47.5, 45.5, 20],
                  [60, 66.5, 62.5, 64.5, 61.5, 52.5, 67, 68, 52, 63, 53, 45, 46, 57.5, 35.5, 25, 28]]).T
    d = zscore(c, ddof=1)  # 数据标准化

    ratio = calContributionRate(d)
    print("累计贡献率:", np.cumsum(ratio))

    myfa = MyFA(3, rotation='varimax')  # 构建模型
    myfa.fit(d)  # 求解方差最大的模型
    df = myfa.getFactorScore()
    gxl = myfa.getFactorContributionRatio()
    pj = df @ gxl
    ind0 = np.argsort(-pj)  # 从大到小的排名地址
    ind = np.ndarray(17)
    ind[ind0] = np.arange(1, 18)
    print('排名次序为:', ind)
