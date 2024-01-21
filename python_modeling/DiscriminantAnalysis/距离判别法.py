import numpy as np
import pandas as pd


def distinguishByDistance(x: np.ndarray, categoryDatas, labels=None):
    def calMahalanobis(x: np.ndarray, A: pd.DataFrame):
        """计算样本x到总体A之间的Mahalanobis距离（马氏距离）"""
        mu = A.mean().values
        cov = A.cov().values
        x_ = (x-mu).reshape(-1, 1)
        res = x_.T @ np.linalg.inv(cov) @ x_
        return res[0][0]**0.5
    if(labels == None):
        labels = range(len(categoryDatas))
    d = list()
    for i in categoryDatas:
        d.append(calMahalanobis(x, i))
    print(d)
    return labels[d.index(min(d))]


if __name__ == "__main__":
    Af = pd.DataFrame(np.array([[1.24, 1.36, 1.38, 1.38, 1.38, 1.40, 1.48, 1.54, 1.58],
                                [1.72, 1.74, 1.64, 1.82, 1.90, 1.70, 1.82, 1.82, 2.08]]).T,
                      columns=["触角", "翼长"])
    Apf = pd.DataFrame(np.array([[1.14, 1.16, 1.20, 1.26, 1.28, 1.30],
                                 [1.78, 1.96, 1.86, 2.00, 2.00, 1.96]]).T,
                       columns=["触角", "翼长"])
    x = np.array([1.24, 1.80])

    label = distinguishByDistance(x, [Af, Apf], ["Af", "Apf"])
    print(label)
