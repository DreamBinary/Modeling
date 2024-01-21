import numpy as np

N = 7
dist = np.ndarray((N, N))
dist.fill(0)
dist[0, 1] = 50
dist[0, 2] = 60
dist[1, 3] = 65
dist[1, 4] = 40
dist[2, 3] = 52
dist[2, 6] = 45
dist[3, 4] = 50
dist[3, 5] = 30
dist[3, 6] = 42
dist[4, 5] = 70
dist += dist.T
dist[dist == 0] = float("inf")


def prim(dist: np.ndarray) -> list:
    size = dist.shape[0]
    result = []
    while(len(result) < size):
        min_index = dist.argmin()
        a, b = min_index//size, min_index % size
        result.append([a+1, b+1, dist.min()])
        dist[a, b] = dist[b, a] = float("inf")
    return result


print(prim(dist))
