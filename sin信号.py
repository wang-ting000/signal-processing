import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import scipy
from funcs import delta,heaviside,xy_sys

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

t=np.linspace(-10,10,1000)
y=2*np.cos(t)
T=2*np.pi
w1=2*np.pi/T
w=[]
Fw=[]
for i in np.linspace(-20,20,41):

    Fn=1/T*(quad(lambda t:scipy.real(2*np.cos(t)*np.exp(-1J*i*w1*t)),-T/2,T/2)[0]
            +
            quad(lambda t:scipy.imag(2*np.cos(t)*np.exp(-1J*i*w1*t)),-T/2,T/2)[0]*1J)
    if abs(Fn)<10^(-10):
        Fn=0
    w += [i * w1]
    #Fw+=[2*np.pi*Fn*delta(w,i*w1,1)]
    Fw += [-2J * np.pi * Fn]

w=np.asarray(w)
Fw=np.asarray(Fw)

plt.subplot(1,2,1)
plt.plot(t,y,'k')
plt.grid()
plt.title('cos(t)')
plt.xlabel('t')
plt.ylabel('cos(t)')
plt.subplot(1,2,2)
plt.stem(w,abs(Fw),markerfmt='^')
plt.grid()
plt.title('cos(t)的频谱')
plt.xlabel('w')
plt.ylabel('F(w)')
xy_sys(-20,20,-4,4)
plt.show()