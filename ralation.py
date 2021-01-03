import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x=np.linspace(-1,1,1000)
y1=np.cos(20*x)

def xy_sys():       #画坐标轴的函数
    plt.grid()
    i=np.linspace(-1,1,100)
    axis_x=np.zeros_like(i)
    plt.plot(i,axis_x,'black')


for i in range(0,40):
    y2=np.cos(i*x)
    y=y2*y1
    xy_sys()
    plt.plot(x,y)
    plt.ylim([-1,1.5])
    plt.title(u'w= %s' % (i))
    plt.pause(0.2)
    plt.cla()


