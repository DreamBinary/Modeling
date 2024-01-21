# 元胞自动机模拟森林火灾
import numpy as np
import random
import seaborn as sbn
import matplotlib.pyplot as plt


# 森林火灾函数
# 传入参数为：（1）当前的燃烧矩阵；（2）空格位 树的生长概率p；（3）正常位 树的燃烧概率f

# 假定：空格位 --> 0  正常位 --> 1   燃烧位 --> -1
# 总量：空格位 --> C  正常位 --> G   燃烧位 --> R
area = 100
def Forest_Fire(current_matrix, p, f):
    matrix = current_matrix

    # （1）空位生长树木 （0 --> 1）   储存位置
    i_C_indexes = []
    j_C_indexes = []
    for i in range(area):  # 行循环
        for j in range(area):  # 列循环
            if matrix[i, j] == 0 and random.random() < p:
                i_C_indexes.append(i)
                j_C_indexes.append(j)
            else:
                pass

    # (2)周围树木燃烧 &  (1 --> -1)   储存位置，并存储上一时刻的燃烧数据
    fire_memory = np.where(matrix == -1)
    i_indexes = []
    j_indexes = []

    for i in range(area):  # 行循环
        for j in range(area):  # 列循环
            if matrix[i, j] == -1:
                try:
                    if matrix[i - 1, j] == 1:
                        i_indexes.append(i - 1)
                        j_indexes.append(j)
                except:
                    pass

                try:
                    if matrix[i + 1, j] == 1:
                        i_indexes.append(i + 1)
                        j_indexes.append(j)
                except:
                    pass

                try:
                    if matrix[i, j - 1] == 1:
                        i_indexes.append(i)
                        j_indexes.append(j - 1)
                except:
                    pass

                try:
                    if matrix[i, j + 1] == 1:
                        i_indexes.append(i)
                        j_indexes.append(j + 1)
                except:
                    pass

            else:
                pass

    for k in range(len(i_indexes)):
        matrix[i_indexes[k], j_indexes[k]] = -1

    # （3）燃烧树木清除 （-1 --> 0）
    matrix[fire_memory] = 0

    # （4）雷电击中正常树木 （1 --> -1）    储存位置
    i_indexes = []
    j_indexes = []

    for i in range(area):  # 行循环
        for j in range(area):  # 列循环
            if matrix[i, j] == 1:

                # 判断最近邻居是否有树木燃烧
                try:
                    if matrix[i - 1, j] == -1:
                        continue
                    else:
                        pass
                except:
                    pass

                try:
                    if matrix[i + 1, j] == -1:
                        continue
                    else:
                        pass
                except:
                    pass

                try:
                    if matrix[i, j - 1] == -1:
                        continue
                    else:
                        pass
                except:
                    pass

                try:
                    if matrix[i, j + 1] == -1:
                        continue
                    else:
                        pass
                except:
                    pass

                # 树木被雷击中
                if random.random() < f:
                    i_indexes.append(i)
                    j_indexes.append(j)
                else:
                    pass

            else:
                pass

    for k in range(len(i_indexes)):
        matrix[i_indexes[k], j_indexes[k]] = -1

    # 完成空位生长树木的操作
    for k in range(len(i_C_indexes)):
        matrix[i_C_indexes[k], j_C_indexes[k]] = 1

    return matrix


    # （1）空位生长树木 （0 --> 1）   储存位置
    i_C_indexes = []
    j_C_indexes = []
    for i in range(area):   # 行循环
        for j in range(area):   # 列循环
            if matrix[i, j] == 0 and random.random()<p:
                i_C_indexes.append(i)
                j_C_indexes.append(j)
            else:
                pass
    # (2)周围树木燃烧   (1 --> -1)   储存位置，并存储上一时刻的燃烧数据
    fire_memory=np.where(matrix==-1)
    i_indexes=[]
    j_indexes=[]

    for i in range(area):   # 行循环
        for j in range(area):   # 列循环
            if matrix[i,j]==-1:
                try:
                    if matrix[i-1,j]==1:
                        i_indexes.append(i-1)
                        j_indexes.append(j)
                except:
                    pass

                try:
                    if matrix[i + 1, j] == 1:
                        i_indexes.append(i + 1)
                        j_indexes.append(j)
                except:
                    pass

                try:
                    if matrix[i , j-1] == 1:
                        i_indexes.append(i)
                        j_indexes.append(j-1)
                except:
                    pass

                try:
                    if matrix[i , j+1] == 1:
                        i_indexes.append(i)
                        j_indexes.append(j+1)
                except:
                    pass

            else:
                pass

    for k in range(len(i_indexes)):
        matrix[i_indexes[k],j_indexes[k]]=-1
    matrix[fire_memory]=0