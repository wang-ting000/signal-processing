import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import scipy
from funcs import delta,heaviside,xy_sys

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

t=np.linspace(-10,10,10)
y=np.ones_like(t)
T=2*np.pi
w1=2*np.pi/T
w=[]
Fw=[]
for i in np.linspace(-20,20,41):

    Fn=1/T
    w += [i * w1]
    #Fw+=[2*np.pi*Fn*delta(w,i*w1,1)]
    Fw += [2 * np.pi * Fn]

w=np.asarray(w)
Fw=np.asarray(Fw)

plt.subplot(1,2,1)
plt.bar(t,y,color='k',width=0.1)
plt.grid()
plt.title('delta(t)')
plt.xlabel('t')
plt.ylabel('delta(t)')
plt.subplot(1,2,2)
plt.bar(w,Fw,width=0.1,color='red')
plt.grid()
plt.title('delta(t)的频谱')
plt.xlabel('w')
plt.ylabel('F(w)')
xy_sys(-20,20,-4,4)
plt.show()