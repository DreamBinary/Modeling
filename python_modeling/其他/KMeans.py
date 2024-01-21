# 下面这个函数是我自己写的，sklearn库有KMeans类（sklearn.cluster.KMeans）

def KMeans(K: int, datas: list):
    def getDistance(dimension, a, b):
        dis = 0
        for i in range(dimension):
            dis += (a[i]-b[i])**2
        return sqrt(dis)

    def judgeGroup(data, groupLeaders):
        distances = []
        for i in range(len(groupLeaders)):
            dis = getDistance(data.dimension, data.coordinate,
                              groupLeaders[i].coordinate)
            distances.append((groupLeaders[i].category, dis))
        distances.sort(key=operator.itemgetter(1))
        data.category = distances[0][0]

    def getLeaders(datas, groupLeaders):
        dimension = groupLeaders[0].dimension
        groups = []
        s = []
        for i in groupLeaders:
            groups.append([])
            s.append([])
            for j in range(dimension):
                s[-1].append(0)
        for i in datas:
            index = i.category
            groups[index].append(i)
            for j in range(dimension):
                s[index][j] += i.coordinate[j]
        newLeaders = []
        for i in range(len(groups)):
            center = []
            for j in range(dimension):
                center.append(s[i][j] / len(groups[i]))
            distances = []
            for j in groups[i]:
                dis = getDistance(dimension, center, j.coordinate)
                distances.append([dis, j])
            distances.sort(key=operator.itemgetter(0))
            newLeaders.append(deepcopy(distances[0][1]))
        return newLeaders

    def judge(a, b):
        if b == []:
            return True
        for i in range(len(a)):
            if a[i].coordinate != b[i].coordinate:
                return True
        return False

    dataNum = len(datas)
    groupLeaders = []
    tempLeaders = []
    for i in range(K):
        datas[i].category = i
        groupLeaders.append(datas[i])
    while judge(groupLeaders, tempLeaders):
        tempLeaders = deepcopy(groupLeaders)
        for i in range(dataNum):
            judgeGroup(datas[i], groupLeaders)
        groupLeaders = getLeaders(datas, groupLeaders)
