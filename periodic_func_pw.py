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
    for i in np.linspace(-4, 4, 9):
        y_real = lambda t: eval(func) * scipy.real(np.exp(-1J * i*w1 * t))
        y_imag = lambda t: eval(func) * scipy.imag(np.exp(-1J * i*w1 * t))
        Fn = 1 / T * (quad(y_real, -T / 2, T / 2)[0]
                      +
                      quad(y_imag, -T / 2, T / 2)[0] * 1J)
        if abs(Fn) < 10 ^ (-10):
            Fn = 0
        w += [i * w1]
        # Fw+=[2*np.pi*Fn*delta(w,i*w1,1)]
        Fw += [abs(2 * np.pi * Fn)**2]
        #Fw += [2 * np.pi * Fn]

    w = np.asarray(w)
    Fw = np.asarray(Fw)
    plt.stem(w, abs(Fw), markerfmt='^')
    #plt.plot(w,abs(Fw))
    plt.grid()
    plt.xlabel('w')
    plt.ylabel('p(w)')
    plt.title('cos(2*pi*3*t)的PSD')
    #xy_sys(-80, 80, -4, 70)
    xy_sys(-80,80, -4, 10)
    #plt.show()