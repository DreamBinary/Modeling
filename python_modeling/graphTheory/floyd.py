# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:52:06 2020

@author: 86158
"""


import numpy as np



def floyd(d):
    D=d
    lengthD = len(D)                    #邻接矩阵大小
    p = list(range(lengthD))
    P = []
    for i in range(lengthD):
        P.append(p)
    P = np.array(P)
    for k in range(lengthD):
        for i in range(lengthD):
            for j in range(lengthD):
                if(D[i][j] >D[i][k]+D[k][j]):         #两个顶点直接较小的间接路径替换较大的直接路径
                    P[i][j] = P[i][k]                 #记录新路径的前驱
                    D[i][j] = D[i][k]+D[k][j]
    return P


Inf = float("Inf") 
graph = [[0,2,8,1,Inf,Inf,Inf,Inf,Inf,Inf,Inf],
         [2,0,6,Inf,1,Inf,Inf,Inf,Inf,Inf,Inf],
         [8,6,0,7,5,1,2,Inf,Inf,Inf,Inf],
         [1,Inf,7,0,Inf,Inf,9,Inf,Inf,Inf,Inf],
         [Inf,1,5,Inf,0,3,Inf,2,9,Inf,Inf],
         [Inf,Inf,1,Inf,3,0,4,Inf,6,Inf,Inf],
         [Inf,Inf,2,9,Inf,4,0,Inf,3,1,Inf],
         [Inf,Inf,Inf,Inf,2,Inf,Inf,0,7,Inf,9],
         [Inf,Inf,Inf,Inf,9,6,3,7,0,1,2],
         [Inf,Inf,Inf,Inf,Inf,Inf,1,Inf,1,0,4],
         [Inf,Inf,Inf,Inf,Inf,Inf,Inf,9,2,4,0]]



d = floyd(graph)
print(d)











