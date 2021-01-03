from periodic_func_pw import fourier_t
import numpy as np
import matplotlib.pyplot as plt



plt.subplot(1,2,1)
t=np.linspace(-5,5,500)
y=np.cos(2*np.pi*3*t)+3*np.cos(2*np.pi*1*t)
plt.plot(t,y)
plt.subplot(1,2,2)
fourier_t('np.cos(2*np.pi*3*t)',2*np.pi*3,np.linspace(-30,50,600))
fourier_t('3*np.cos(2*np.pi*1*t)',2*np.pi*1,np.linspace(-30,50,600))
plt.show()


from FT_NT import fourier
plt.subplot(2,1,1)
y=fourier('np.cos(2*np.pi*3*t)+3*np.cos(2*np.pi*1*t)',np.linspace(-50,50,100),-5,5,np.linspace(-5,5,100))
plt.subplot(2,1,2)
Yw=abs(y)**2*5
f=np.linspace(-50,50,100)/2/np.pi
plt.plot(f,Yw)
plt.show()