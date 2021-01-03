import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def corr(x):
    N=len(x)
    l1=np.linspace(-N+1,N,N*2-1)
    sum=list(np.zeros_like(l1))
    for M in range(-N+1,1,1):
        for m in range(0,N+M):
            sum[N-1+M]+=x[m-M]*x[m]
    for M in range(1,N,1):
        for m in range(0,N-M,1):
            sum[N-1+M]+=x[m+M]*x[m]
    return sum

