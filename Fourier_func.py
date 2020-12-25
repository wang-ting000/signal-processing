#from UliEngineering.SignalProcessing.Simulation import sawtooth 在其他编辑器里不能使用
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


m = input("How many times:")
def xy_sys():       #画坐标轴的函数
    plt.grid()
    zero_x=[0]
    zero_y=[0]
    plt.plot(zero_x,zero_y,color = 'black',marker='o')
    i=np.linspace(-1,1,100)
    axis_x=np.zeros_like(i)
    plt.plot(i,axis_x,'black')
    arrow_xx=[1]
    arrow_xy=[0]
    plt.plot(arrow_xx,arrow_xy,color='black',marker=5)
    j=np.linspace(-1,1,100)
    axis_y=np.zeros_like(i)
    plt.plot(axis_y,j,'black')
    arrow_yy=[1]
    arrow_yx=[0]
    plt.plot(arrow_yx,arrow_yy,color='black',marker=6)

    

 #初始信号   
#t = np.linspace(-1,1,10000)
#y = sawtooth(frequency=5, samplerate=10e3)
def plot_pic0():  #斜三角波，在【1，1】的区间内重复5次，T1=0.4
    l=np.linspace(-0.2,0.2,2000)
    t=5*l
    t[0]=0
    t[-1]=0
    y=np.append(t,t)
    for i in range(3):
        y = np.append(y,t)
    return y


t = np.linspace(-1,1,10000)
y=plot_pic0()
y_new=np.zeros_like(y)
xy_sys()
plt.plot(t,y)
plt.title(u'斜三角波')
plt.pause(2)
plt.cla()

for n in range(1,eval(m)+1):
    for i in range(len(y)):
        y_new[i] += (-1)**(n-1)*2*np.sin(n*5*np.pi*t[i])/np.pi/n
    plt.plot(t,y_new)
    plt.plot(t,y,color=(0.8,0.1,0.1),marker=',')
    xy_sys()
    #font_set=font_manager.FontProperties(fname="C:\\Windows\\Fonts\\MSYHBD.TTC")
    plt.title(u'斜三角波的傅里叶级数分解至第 %s 次谐波'%(n))#,fontproperties=font_set)#两种显示中文的方法
    plt.ylim([-1.2,1.2])
    if n == eval(m):
        plt.pause(0.1)
    else:
        plt.pause(0.1)
        plt.cla()

    
    

