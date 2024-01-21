import numpy as np


def calCorr(x: np.ndarray, y: np.ndarray) -> float:
    cov = np.cov(x, y, ddof=0)
    tmp = (cov[0, 0]*cov[1, 1])**0.5
    if(tmp == 0):
        res = 0
    else:
        res = cov[0, 1]/tmp
    return res


def calCorrArray(data: np.ndarray) -> np.ndarray:
    """
    parameter
    ---------

    data : {array-like, sparse matrix} of shape (n_samples, n_features)
    """
    data = data.T
    n = len(data)
    corrArray = np.ndarray((n, n))
    for i in range(n):
        corrArray[i, i] = 1
        for j in range(i+1, n):
            corrArray[i, j] = corrArray[j, i] = calCorr(data[i], data[j])
    return corrArray


def calAngleCos(x: np.ndarray, y: np.ndarray) -> float:
    """夹角余弦"""
    tmp1 = (x*y).sum()
    tmp2 = ((x**2).sum()*(y**2).sum())**0.5
    if(tmp2 == 0):
        res = 0
    else:
        res = tmp1/tmp2
    return res


if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([1, 4, 3])
    print(calCorrArray(np.array([a, b]).T))
