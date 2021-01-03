import numpy as np
import matplotlib.pyplot as plt
from awgn import awgn
from corr_self import corr
from scipy.fftpack import fft
from scipy import signal

'''加噪信号'''
dt=0.001
t0=2
fs=1/dt
t=np.linspace(0,t0,t0/dt,endpoint=True)
N=int(t0/dt)
n=np.arange(0,N)
w=n/N*fs
f0=100
f1=200
y=np.sin(2*np.pi*f0*t)+0.3*np.sin(2*np.pi*f1*t)
'''plt.psd(y,Fs=fs,NFFT=1024)
plt.show()'''
plt.subplot(4,1,3)
yyr=np.correlate(y,y,mode='full')
ppw=fft(yyr,len(t))
plt.plot(w,10*np.log10(abs(ppw)))
plt.subplot(4,1,1)
y+=awgn(y,0)
yr=np.correlate(y,y,mode='full')
#yr=np.correlate(y,y,mode='full')
plt.plot(y)
Pw=fft(yr,len(t))
plt.subplot(4,1,2)
plt.plot(w,20*np.log10(np.abs(Pw)))


'''中值滤波'''
for i in range(1,2*N-2):
    yr[i]=1/3*(yr[i-1]+yr[i]+yr[i+1])
Pw=fft(yr,len(t))
plt.subplot(4,1,4)
plt.plot(w,20*np.log10(abs(Pw)))
plt.show()

