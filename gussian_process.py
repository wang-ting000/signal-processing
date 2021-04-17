# -*- encoding: utf-8 -*-
"""
@File   : gussian_process.py
@Time   : 2021/4/17 11:44
@Author : Wang
"""
from psd import psd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

k=eval(input('你要几个样本:'))
alpha=2
sigma = 2
Ts=eval(input('采样间隔:'))
fs=1/Ts
n=eval(input('样本长度:'))
for i in range(k):
    xn=np.random.normal(0,1,n)
    yn=np.zeros_like(xn)
    yn[0]=sigma*xn[0]
    for j in range(1,n):
        yn[j]=np.exp(-alpha*Ts)*yn[j-1]+sigma*np.sqrt(1-np.exp(-2*alpha*Ts))*xn[j]
    yn_corr=sum([i**2 for i in yn])/n
    print(yn_corr)#R(0)
    plt.subplot(311)
    plt.plot(yn,label='第%s个样本函数'%(i+1),color='orange')
    plt.legend()
    plt.subplot(312)
    ycorr=np.correlate(yn,yn,'full')
    tau=np.linspace(-n,n,n*2-1)*Ts
    ycorr=ycorr/n
    plt.plot(tau, ycorr,color='purple',marker='^',label='实际的自相关函数')
    R_tau=4*np.exp(-2*abs(tau))
    plt.plot(tau,R_tau,'r',marker='*',label='理想的自相关函数')
    plt.xlabel('t')
    plt.ylabel('R(t)')
    plt.legend()
    plt.subplot(313)
    f=(tau/n*fs)[n-1:2*n-1]
    yrr0=np.fft.fft(R_tau)[0:n]/fs
    #plt.plot(f,abs(yrr0),label='理想psd')
    plt.plot(f,20*np.log(abs(yrr0)),label='理想psd')
    yrr1=np.fft.fft(ycorr)[0:n]/fs
    #plt.plot(f,abs(yrr1),label='实际psd')
    plt.plot(f,20*np.log10(abs(yrr1)),label='实际psd')
    plt.legend()
    plt.title('功率谱密度函数')
    plt.xlabel('f/Hz')
    plt.ylabel('psd/(dB/Hz)')


plt.show()