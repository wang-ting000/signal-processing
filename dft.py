import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos,pi

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

n=np.arange(1,257,1)
Fs=1
N=256
x=sin(0.4* pi * n + pi / 3) + 1.5 * sin(0.2 * pi * n + pi / 4)
k=np.arange(0,256,1)
Xk=list(np.zeros_like(k))
XW=list(np.zeros_like(k))
for j in range(len(k)):
    Xk[j]=sum(x*np.exp(-1J*2*np.pi*n*k[j]/N))
    XW[j]=np.abs(Xk[j])**2

plt.subplot(2,1,1)
w=n/N*Fs
plt.plot(w,np.abs(Xk))
plt.title('sin(0.4* pi * n + pi / 3) + 1.5 * sin(0.2 * pi * n + pi / 4)的频谱')
plt.subplot(2,1,2)
plt.plot(w,np.abs(XW)*Fs)
plt.title('sin(0.4* pi * n + pi / 3) + 1.5 * sin(0.2 * pi * n + pi / 4)的功率谱')
plt.show()