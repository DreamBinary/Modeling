from typing import Sequence

import numpy as np
import pandas as pd


def pretreat(data: Sequence or pd.Series, method: str = "benefit", **kwargs):
    s = pd.Series(data, dtype=float)
    max = s.max()
    min = s.min()
    if(method == "benefit"):
        res = (s-min)/(max-min)
    elif(method == "cost"):
        res = (max-s)/(max-min)
    elif(method == "section"):
        section = kwargs["section"]
        for i in s.index:
            if(section[0] <= s[i] < section[1]):
                s[i] = 1-(section[1]-s[i])/(section[1]-section[0])
            elif(section[1] <= s[i] <= section[2]):
                s[i] = 1
            elif(section[2] < s[i] <= section[3]):
                s[i] = 1-(s[i]-section[2])/(section[3]-section[2])
            else:
                s[i] = 0
        res = s
    elif(method == "std"):
        res = (s-s.mean())/s.std()
    else:
        res = s
    return res.values


def GRA(df: pd.DataFrame, w: Sequence, tho=0.5) -> pd.Series:
    """
    灰色关联度分析
    
    parameters
    ----------
    `df` : 输入数据, {array-like, sparse matrix} of shape (n_samples, n_features)
    `w` : 参考序列, sequence of shape (n_features,)
    'tho' : 分辨系数
    """
    df0 = (df-w).abs()
    min = df0.min().min()
    max = df0.max().max()
    res = (min + tho * max) / (df0 + tho * max)
    res = res.T.mean()
    return res


if __name__ == "__main__":
    datas = np.array([[0.83, 0.90, 0.99, 0.92, 0.87, 0.95],
                      [326, 295, 340, 287, 310, 303],
                      [21, 38, 25, 19, 27, 10],
                      [3.2, 2.4, 2.2, 2.0, 0.9, 1.7],
                      [0.20, 0.25, 0.12, 0.33, 0.20, 0.09],
                      [0.15, 0.20, 0.14, 0.09, 0.15, 0.17],
                      [250, 180, 300, 200, 150, 175],
                      [0.23, 0.15, 0.27, 0.30, 0.18, 0.26],
                      [0.87, 0.95, 0.99, 0.89, 0.82, 0.94]])
    for i in [1, 5, 6, 7, 8, 9]:
        datas[i-1] = pretreat(datas[i-1], method="benefit")
    for i in [2, 3, 4]:
        datas[i-1] = pretreat(datas[i-1], method="cost")
    df = pd.DataFrame(datas.T)

    res = GRA(df, w=1)
    print(res.sort_values(ascending=False))  # 降序排列后打印
