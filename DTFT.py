import matplotlib.pyplot as plt
import numpy as np

w=np.linspace(-15,15,2100)
n=np.linspace(0,100,99)
x=np.cos(0.2*np.pi*n)
y=list(np.zeros_like(w))
for i in range(len(w)):
    y[i]=sum(x*np.exp(-1J*w[i]*n))
plt.subplot(3, 1, 1)
plt.stem(n,x)
plt.subplot(3,1,2)
plt.plot(w,abs(np.asarray(y)))
plt.subplot(3,1,3)
arg=np.angle(np.asarray(y))
plt.plot(w,arg)
plt.show()
plt.ylim([0,7])
