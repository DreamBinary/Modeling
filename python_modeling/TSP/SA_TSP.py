import time
from math import acos, cos, exp, pi, sin
from random import random, sample

import matplotlib.pyplot as plt
import numpy as np


class SA_TSP():
    def __init__(self, path0: np.ndarray, distance: np.ndarray, t=20, at=0.99995, e=1e-10) -> None:
        """
        模拟退火算法解决旅行商问题
        
        parameter:
            path : 任意给定一条初始路径，保证起点和终点的编号正确即可
            distance : 距离矩阵，distance[i][j]表示编号分别为i、j的两个点间的距离
            t、at、e : 分别表示模拟退火算法中的起始温度、降温速度、终止温度
        notes:
            起始温度、降温速度的选择都会对算法的效果产生较大影响
        result:
            速度比`sko.SA.SA_TSP`快，效果差不多
        """
        self.path = path0
        self.num = len(path0)
        self.distance = distance
        self.t = t
        self.at = at
        self.e = e
        self.result = self.getPathLen(self.path)
        self.history = [self.result]

    def getPathLen(self, path) -> float:
        length = 0
        for i in range(self.num):
            length += self.distance[path[i]][path[(i+1) % self.num]]
        return length

    def getNewPath(self):
        if(random() > 0.5):  # 某一段逆序
            a, b = sorted(sample(range(0, self.num+1), 2))
            self.newpath = self.path.copy()
            self.newpath[a:b] = self.path[a:b][::-1]
            self.delta = self.distance[self.newpath[a]][self.newpath[a-1]]\
                + self.distance[self.newpath[b % self.num]][self.newpath[b-1]]\
                - self.distance[self.path[a]][self.path[a-1]]\
                - self.distance[self.path[b % self.num]][self.path[b-1]]
        else:  # 交换某两段序列
            a, b, c = sorted(sample(range(0, self.num+1), 3))
            self.newpath = self.path.copy()
            self.newpath[a:a+(c-b)] = self.path[b:c]
            self.newpath[c-(b-a):c] = self.path[a:b]
            self.delta = self.distance[self.path[a-1]][self.path[b]]\
                + self.distance[self.path[c-1]][self.path[a]]\
                + self.distance[self.path[b-1]][self.path[c % self.num]]\
                - self.distance[self.path[a]][self.path[a-1]]\
                - self.distance[self.path[b]][self.path[b-1]]\
                - self.distance[self.path[c % self.num]][self.path[c-1]]

    def cool_down(self):
        self.t *= self.at

    def solve(self) -> float:
        start = time.perf_counter()
        while self.t > self.e:
            self.getNewPath()
            if(self.delta <= 0):
                self.path = self.newpath.copy()
                self.result = self.result + self.delta
            elif(random() < exp(-self.delta/self.t)):
                self.path = self.newpath.copy()
                self.result = self.result + self.delta
            self.history.append(self.result)
            self.cool_down()
        # print(self.path)
        # print(self.result)
        stop = time.perf_counter()
        print("running time:", stop-start)

    def drawPath(self):
        best_points_ = np.concatenate([self.path, [self.path[0]]])
        best_points_coordinate = datas[best_points_, :]
        plt.plot(best_points_coordinate[:, 0],
                 best_points_coordinate[:, 1], 'o-r')

    def drawHistory(self):
        plt.plot(range(len(self.history)), self.history)


def getGlobeDist(point1: np.ndarray, point2: np.ndarray) -> float:
    tmp = cos(point1[0]-point2[0])*cos(point1[1])*cos(point2[1])\
        + sin(point1[1])*sin(point2[1])
    if tmp > 1:
        tmp = 1.
    elif tmp < -1:
        tmp = -1.
    return 6370*acos(tmp)


datas = eval("""[[70, 40], 
                 [53.7121, 15.3046], [51.1758, 0.0322], [46.3253, 28.2753], [30.3313, 6.9348],
                 [56.5432, 21.4188], [10.8198, 16.2529], [22.7891, 23.1045], [10.1584, 12.4819],
                 [20.1050, 15.4562], [1.9451, 0.2057], [26.4951, 22.1221], [31.4847, 8.9640],
                 [26.2418, 18.1760], [44.0356, 13.5401], [8.9836, 25.9879], [38.4722, 20.1731],
                 [28.2694, 29.0011], [32.1910, 5.8699], [36.4863, 29.7284], [0.9718, 28.1477],
                 [8.9586, 24.6635], [16.5618, 23.6143], [10.5597, 15.1178], [50.2111, 10.2944],
                 [8.1519, 9.5325], [22.1075, 18.5569], [0.1215, 18.8726], [48.2077, 16.8889],
                 [31.9499, 17.6309], [0.7732, 0.4656], [47.4134, 23.7783], [41.8671, 3.5667],
                 [43.5474, 3.9061], [53.3524, 26.7256], [30.8165, 13.4595], [27.7133, 5.0706],
                 [23.9222, 7.6306], [51.9612, 22.8511], [12.7938, 15.7307], [4.9568, 8.3669],
                 [21.5051, 24.0909], [15.2548, 27.2111], [6.2070, 5.1442], [49.2430, 16.7044],
                 [17.1168, 20.0354], [34.1688, 22.7571], [9.4402, 3.9200], [11.5812, 14.5677],
                 [52.1181, 0.4088], [9.5559, 11.4219], [24.4509, 6.5634], [26.7213, 28.5667],
                 [37.5848, 16.8474], [35.6619, 9.9333], [24.4654, 3.1644], [0.7775, 6.9576],
                 [14.4703, 13.6368], [19.8660, 15.1224], [3.1616, 4.2428], [18.5245, 14.3598],
                 [58.6849, 27.1485], [39.5168, 16.9371], [56.5089, 13.7090], [52.5211, 15.7957],
                 [38.4300, 8.4648], [51.8181, 23.0159], [8.9983, 23.6440], [50.1156, 23.7816],
                 [13.7909, 1.9510], [34.0574, 23.3960], [23.0624, 8.4319], [19.9857, 5.7902],
                 [40.8801, 14.2978], [58.8289, 14.5229], [18.6635, 6.7436], [52.8423, 27.2880],
                 [39.9494, 29.5114], [47.5099, 24.0664], [10.1121, 27.2662], [28.7812, 27.6659],
                 [8.0831, 27.6705], [9.1556, 14.1304], [53.7989, 0.2199], [33.6490, 0.3980],
                 [1.3496, 16.8359], [49.9816, 6.0828], [19.3635, 17.6622], [36.9545, 23.0265],
                 [15.7320, 19.5697], [11.5118, 17.3884], [44.0398, 16.2635], [39.7139, 28.4203],
                 [6.9909, 23.1804], [38.3392, 19.9950], [24.6543, 19.6057], [36.9980, 24.3992],
                 [4.1591, 3.1853], [40.1400, 20.3030], [23.9876, 9.4030], [41.1084, 27.7149]]""")  # 各点的经纬度坐标

num_points = len(datas)
datas = np.array(datas)*pi/180
distance = np.ndarray((num_points, num_points), dtype=np.float)
for i in range(len(datas)):
    for j in range(len(datas)):
        distance[i][j] = getGlobeDist(datas[i], datas[j])
path0 = np.arange(0, num_points, 1, dtype=int)
for i in range(10):  # 重复五次计算
    sa = SA_TSP(path0, distance)
    sa.solve()
    # print(sa.path)
    print(sa.result)
# plt.subplot(1, 2, 1)
# sa.drawPath()
# plt.subplot(1, 2, 2)
# sa.drawHistory()
# plt.show()
