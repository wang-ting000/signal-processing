import numpy as np
import matplotlib.pyplot as plt


x=np.random.randn(500)
y=np.correlate(x,x,mode='full')
print(len(y))
Y=np.fft.fft(y,len(y))
Pw=abs(Y)**2/len(y)
plt.plot(abs(Pw))
plt.show()
x=sorted(x)
y=np.correlate(x,x,mode='full')
Y=np.fft.fft(y,len(y))
Pw=abs(Y)**2/len(y)
plt.plot(abs(Pw))
plt.show()