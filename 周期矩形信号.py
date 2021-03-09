import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import scipy
from scipy.signal import square
from funcs import delta,heaviside,xy_sys

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



T=5
w1=2*np.pi/T
w=[]
Fw=[]
for i in np.linspace(-50,50,101):

    Fn=1/T*(quad(lambda t:scipy.real((square(2*np.pi/5*t+np.pi*0.4,duty=0.4)+1)/2*np.exp(-1J*i*w1*t)),-T/2,T/2)[0]
            +
            quad(lambda t:scipy.imag((square(2*np.pi/5*t+np.pi*0.4,duty=0.4)+1)/2*np.exp(-1J*i*w1*t)),-T/2,T/2)[0]*1J)
    print(Fn)
    if abs(Fn)<10^(-10):
        Fn=0
    w += [i * w1]
    #Fw+=[2*np.pi*Fn*delta(w,i*w1,1)]
    Fw += [2 * np.pi * Fn]


ww=np.linspace(w[0],w[100],1001)
w=np.asarray(w)
Y=0.8*np.pi*np.sinc(ww/np.pi)
Fw=np.asarray(Fw)

t=np.linspace(-5,5,1000)
y=(square(2*np.pi/5*t+np.pi*0.4,duty=0.4)+1)/2

plt.subplot(1,2,1)
plt.plot(t,y,'k')
plt.grid()
plt.title('square(t)')
plt.xlabel('t')
plt.ylabel('square(t)')
plt.subplot(1,2,2)
plt.bar(w,Fw,width=0.2,color='red')
plt.plot(ww,Y)
plt.grid()
plt.title('square(t)的频谱')
plt.xlabel('w')
plt.ylabel('F(w)')
plt.show()