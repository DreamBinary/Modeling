# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:02:19 2020

@author: 86158
"""

from copy import deepcopy
import numpy as np

def Dijkstra(graph,start,stop):
    start -= 1
    stop -= 1
    n = len(graph)  
    flag = [0]*n    #记录各节点是否着色
    P = [start]*n   #初始化前驱点
    D = deepcopy(graph[start])  #记录各节点到起始点的最短距离
    flag[start] = 1
    while flag[stop]!=1:    #还有n-1个地方未确定，循环n-1次
        #查找当前未确定点中到start点的最短路径长度，并记录该点
        dmin = float("Inf") 
        for i in range(0,n):
            if not flag[i] and D[i] < dmin:
                k = i
                dmin = D[i]
        flag[k] = 1
        #更新其余未确定点到start点的最短路径长度
        for i in range(0,n):
            if not flag[i] and dmin + graph[k][i] < D[i]:
                D[i] = dmin + graph[k][i]
                P[i] = k
    path = [stop+1]
    i = stop
    while P[i]!=start: #从终点倒回起点
        i = P[i]
        path.insert(0,i+1)
    else:
        path.insert(0,start+1)
    return D[stop],path



def floyd(graph,start,stop):
    start -= 1
    stop -= 1
    D = deepcopy(graph)
    n = len(D)
    p = list(range(n))
    P = []
    for i in range(n):  #初始化后驱点
        P.append(p)
    P = np.array(P)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(D[i][j] >D[i][k]+D[k][j]):         #两个顶点直接较小的间接路径替换较大的直接路径
                    P[i][j] = P[i][k]                 #记录新路径的后驱d点
                    D[i][j] = D[i][k]+D[k][j]
    
    path = [start+1]
    i = start
    while P[i][stop]!=stop:
        i = P[i][stop]
        path.append(i+1)
    else:
        path.append(stop+1)
    
    return D[start][stop],path





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
'''
graph = [[0,50,Inf,40,25,10],
         [50,0,15,20,Inf,25],
         [Inf,15,0,10,20,Inf],
         [40,20,10,0,10,25],
         [25,Inf,20,10,0,55],
         [10,25,Inf,25,55,0]]
'''

a,d = floyd(graph,5,11)
print(a)
print(d)



















