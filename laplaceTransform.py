import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import quad
import scipy


fig=plt.figure()
ax=Axes3D(fig)


w=list(np.linspace(-10,10,201))
for a in np.linspace(1,3,200):
    F=[]
    for i in range(len(w)):
        '''F += [quad(lambda t:np.exp(-a*t) * np.cos(w[i] * t), 0, np.inf)[0]
              - 1J *
              quad(lambda t: np.exp(-a * t) * np.sin(w[i] * t), 0, np.inf)[0]
              ]'''
        '''F += [quad(lambda t: np.exp(-(a + 1) * t) * np.cos(w[i] * t), 0, np.inf)[0]
              - 1J *
              quad(lambda t: np.exp(-(a + 1) * t) * np.sin(w[i] * t), 0, np.inf)[0]
              ]'''
        '''F += [quad(lambda t: t**3*np.exp(-a * t) * np.cos(w[i] * t), 0, np.inf)[0]
              - 1J *
              quad(lambda t: t**3*np.exp(-a * t) * np.sin(w[i] * t), 0, np.inf)[0]
              ]'''
        '''F += [quad(lambda t: np.sin(t)*np.exp(-a * t) * np.cos(w[i] * t), 0, np.inf)[0]
              - 1J *
              quad(lambda t: np.sin(t)*np.exp(-a * t) * np.sin(w[i] * t), 0, np.inf)[0]
              ]'''
        F += [quad(lambda t: t*np.exp(-3*t)*np.exp(-a * t) * np.cos(w[i] * t), 0, np.inf)[0]
              - 1J *
              quad(lambda t: t*np.exp(-3*t)*np.exp(-a * t) * np.sin(w[i] * t), 0, np.inf)[0]
              ]
    F=np.asarray(F)
    print(a,F)
    aw=a*np.ones_like(w)
    ax.plot(aw,w,F,color=tuple(np.random.rand(3)))
plt.savefig('LT')
plt.show()

