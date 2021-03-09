import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

n=np.linspace(0,4,5)
k=np.linspace(-6,6,13)
Xk=list(np.zeros_like(k))
for j in range(len(k)):
    Xk[j]=sum(np.exp(-1J*2*np.pi*n*k[j]/5))

plt.subplot(2,1,1)
n=np.linspace(-6,6,13)
xn=np.ones_like(n)
plt.stem(n,xn)
plt.title('x(n)周期序列')
plt.subplot(2,1,2)
plt.stem(k,Xk)
k=np.linspace(-6.2,6.3,1300)
Xk=list(np.zeros_like(k))
n=np.linspace(0,4,5)
for j in range(len(k)):
    Xk[j]=sum(np.exp(-1J*2*np.pi*n*k[j]/5))
plt.plot(k,np.abs(Xk),'r--')
plt.title('|X(k)|')
plt.show()