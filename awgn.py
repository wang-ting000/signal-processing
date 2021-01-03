import numpy as np
import matplotlib.pyplot as plt

def awgn(x,snr):
    snr=10**(snr/10)
    xpower=np.sum(x**2)/len(x)
    npower=xpower/snr
    a=np.random.randn(len(x))*np.sqrt(npower)
    return a


