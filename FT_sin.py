def fourier_t(func,w_arg,t):

    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.integrate import quad
    import scipy
    from funcs import delta, heaviside, xy_sys

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


    w = []
    Fw = []
    w1=w_arg
    T=2*np.pi/w1
    for i in np.linspace(-20, 20, 41):
        y_real = lambda t: eval(func) * scipy.real(np.exp(-1J * i*w1 * t))
        y_imag = lambda t: eval(func) * scipy.imag(np.exp(-1J * i*w1 * t))
        Fn = 1 / T * (quad(y_real, -T / 2, T / 2)[0]
                      +
                      quad(y_imag, -T / 2, T / 2)[0] * 1J)
        if abs(Fn) < 10 ^ (-10):
            Fn = 0
        w += [i * w1]
        # Fw+=[2*np.pi*Fn*delta(w,i*w1,1)]
        Fw += [-2J * np.pi * Fn]

    w = np.asarray(w)
    Fw = np.asarray(Fw)
    y=eval(func)
    plt.subplot(1, 2, 1)
    plt.plot(t, y, 'k')
    plt.grid()
    plt.title('cos(t)')
    plt.xlabel('t')
    plt.ylabel('cos(t)')
    plt.subplot(1, 2, 2)
    plt.stem(w, abs(Fw), markerfmt='^')
    plt.grid()
    plt.title('cos(t)的频谱')
    plt.xlabel('w')
    plt.ylabel('F(w)')
    xy_sys(-20, 20, -4, 4)
    plt.show()


