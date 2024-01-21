from math import log
import numpy as np
import pandas as pd


class BayesDiscriminant(object):
    def __init__(self, datas: pd.DataFrame, L_ratio: float = 1, p_ratio: float = 1) -> None:
        y0 = datas.index.values
        self.labels = list(set(y0))
        self.G1 = datas[y0 == self.labels[0]]
        self.G2 = datas[y0 == self.labels[1]]
        self.mu1 = self.G1.mean()
        self.mu2 = self.G2.mean()
        sigma = pd.concat([self.G1, self.G2], axis=0).cov()
        self.sigma_ = np.linalg.inv(sigma)
        self.beta = log(L_ratio/p_ratio)

    def predict(self, x: np.ndarray):
        res = (x-0.5*(self.mu1+self.mu2)).T @ self.sigma_ @ (self.mu1-self.mu2)
        return self.labels[0] if(res >= self.beta) else self.labels[1]


if __name__ == "__main__":
    datas = pd.DataFrame([[13.85, 2.79,  7.80, 49.60],
                          [22.31, 4.67, 12.31, 47.80],
                          [28.82, 4.63, 16.18, 62.15],
                          [15.29, 3.54,  7.58, 43.20],
                          [28.29, 4.90, 16.12, 58.70],
                          [2.18,  1.06,  1.22, 20.60],
                          [3.85,  0.80,  4.06, 47.10],
                          [11.40, 0.00,  3.50,  3.00],
                          [3.66,  2.42,  2.14, 15.10],
                          [12.10, 0.00,  5.68,  0.00]], index=[1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
    xs = np.array([[8.85, 3.38, 5.17, 26.1],
                   [28.6, 2.4, 1.2, 127],
                   [20.7, 6.7, 7.6, 30.8],
                   [7.9, 2.4, 4.3, 33.2],
                   [3.19, 3.2, 1.43, 9.9],
                   [12.4, 5.1, 4.48, 24.6]])

    fisher = BayesDiscriminant(datas)
    for x in xs:
        print(fisher.predict(x))
