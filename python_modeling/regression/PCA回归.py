import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import statsmodels.api as sm


class PCA_OLS(object):
    def __init__(self, x: pd.DataFrame, y: pd.Series) -> None:
        self.x = x
        self.y = y
        self.mu = self.x.mean().values
        self.std = self.x.std().values
        self.x_std = (self.x-self.mu)/self.std

    def pca(self, n: int = -1):
        if(n == -1):
            n = len(self.mu)-1
        self.pca_ = PCA().fit(self.x_std)
        self.explained_variance_ratio_ = self.pca_.explained_variance_ratio_[
            :n]
        self.sigma = self.pca_.components_[:n]
        self.z = self.x_std.values@self.sigma.T
        return self

    def ols(self):
        d = {"y": self.y.values, "x": self.z}
        self.ols_ = sm.formula.ols('y~x', d).fit()
        self.params_z = self.ols_.params
        return self

    def transformBack(self):
        self.A = self.params_z[1:]@self.sigma/self.std
        self.b = self.params_z[0]-self.A@self.mu.T
        return self


x = pd.DataFrame([[7, 1, 11, 11, 7, 11, 3, 1, 2, 21, 1, 11, 10],
                  [26, 29, 56, 31, 52, 55, 71, 31, 54, 47, 40, 66, 68],
                  [6, 15, 8, 8, 6, 9, 17, 22, 18, 4, 23, 9, 8],
                  [60, 52, 20, 47, 33, 22, 6, 44, 22, 26, 34, 12, 12]]).T
y = pd.Series([78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7,
               72.5, 93.1, 115.9, 83.8, 113.3, 109.4])

pca_ols = PCA_OLS(x, y)
pca_ols.pca(3).ols().transformBack()

print('回归方程的常数项:', np.round(pca_ols.A, 4))
print('回归方程的其他系数:', np.round(pca_ols.b, 4))
print('主成分回归的残差方差:', round(pca_ols.ols_.mse_resid, 4))
