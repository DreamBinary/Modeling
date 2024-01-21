# 下面提供的是一元非线性函数的最小二乘拟合
# 多元线性函数的最小拟合可以用`statsmodels.api.OLS`类

def polynome(x, p):
    """多项式函数"""
    y = 0
    for i in p:
        y = y*x+i
    return y


def exponent(x, p):
    """指数函数"""
    A, e, b = p
    y = A*pow(e, x)+b
    return y


def logarithm(x, p):
    """对数函数"""
    A, x0, b = p
    y = A*log(x+x0)+b
    return y


def sine(x, p):
    """三角函数"""
    A, w, theta = p
    y = A*sin(w*x+theta)
    return y


def fitting(x, y, func, n):
    """根据func拟合，参数n为需要的参数个数"""
    def residuals(p, y, x):
        return y-func(x, p)
    p0 = np.zeros(n)
    plsq = opt.leastsq(residuals, p0, args=(y, x))
    return plsq[0]
