from math import *
import numpy as np
import matplotlib.pyplot as plt



def signal(n):
    return (sin(0.2 * pi * n + pi / 3) + 10 * sin(0.6 * pi * n + pi / 4))


# 生成WN项
def wn_k(k, n, N):
    return complex(cos(2 * pi * n * k / N), sin(-2 * pi * n * k / N))


amplitude = []  # 准备一个空列表
power_spectrum = []
sums = 0

# 64点DFT，X(0)到X(63)
for k in range(0, 64):
    for n in range(1, 257):
        # n的取值为从1到256
        sums = sums + signal(n) * wn_k(k, n, 64)
    amplitude.append(sums)
    sums = 0

print(amplitude, len(amplitude))

for i in range(0, 64):
    power_spectrum.append(amplitude[i] ** 2)

plt.suptitle("xn=sin(2*pi*f1*n+pi/3)+10*sin(2*pi*f2*n+pi/4)")
plt.subplot(2, 1, 1)
plt.plot(np.abs(amplitude))
plt.title("amplitude_spectrum")
plt.subplot(2, 1, 2)
plt.plot(np.abs(power_spectrum))
plt.title("power_spectrum")
plt.show()