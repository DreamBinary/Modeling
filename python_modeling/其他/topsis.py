from math import sqrt
from typing import Sequence

import numpy as np
import pandas as pd
from pandas.core.series import Series


def pretreat(data: Sequence or pd.Series, method="benefit", vector: bool = False, **kwargs):
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
    if(vector == True):
        tmp = 0
        for i in res.values:
            tmp += i*i
        res = res / sqrt(tmp)
    return res


def topsis(datas: np.ndarray or pd.DataFrame, w=1) -> pd.Series:
    def getDistance(a: pd.Series, b: pd.Series):
        dis = 0
        for i in range(a.size):
            dis += (a[i]-b[i])**2
        return sqrt(dis)
    df = pd.DataFrame(datas * w)
    best = df.max()
    worst = df.min()
    result = []
    for i in range(df.shape[0]):
        d1 = getDistance(best, df.loc[i])
        d2 = getDistance(worst, df.loc[i])
        result.append(d2/(d1+d2))
    return pd.Series(result)


if __name__ == "__main__":
    datas = np.array([[0.1, 0.2, 0.4, 0.9, 1.2],
                      [5, 6, 7, 10, 2],
                      [5000, 6000, 7000, 10000, 400],
                      [4.7, 5.6, 6.7, 2.3, 1.8]])
    methods = ["benefit", "section", "benifit", "cost"]
    for i in range(4):
        datas[i] = pretreat(datas[i], method=methods[i],
                            vector=True, section=[2, 5, 6, 12])
    res = topsis(datas.T, w=[0.2, 0.3, 0.4, 0.1])
    print(res.values)
    # print(datas.T)
