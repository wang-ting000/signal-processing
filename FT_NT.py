def fourier(func,w_arg,t_min,t_max,t_show):

    """
    输出一个连续非周期信号的傅里叶变换表达式以及复频谱和频谱画图
    :param func: 需要进行傅里叶变换的函数,为一numpy表示的字符串
    :param t_min:信号的时域长度的左坐标
    :param t_max:信号的时域长度右坐标
    :param w_arg:期望展现的频谱范围，为ndarray数组
    :param t_show:期望展现的时域范围，为ndarray数组
    :return:None

    --------------------------------------------------
    传参Eg:
    a=fourier('np.sin(t)',np.linspace(0,1,1000),-1,1,np.linspace(-10,10,200))

    --------------------------------------------------
    """

    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.integrate import quad
    import scipy

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



    ###传参###------------------------------------------------------------------
    #w=w_arg
    ####------------------------------------------------------------------------
    #print(w_arg)

    a = list(np.zeros_like(w_arg))
    b = list(np.zeros_like(w_arg))
    c = list(np.zeros_like(w_arg))
    d = list(np.zeros_like(w_arg))

    #print(w_arg)
    w=w_arg
    n=np.random.randn(len(w))
    for i in range(len(w)):
        y_real = lambda t:eval(func)*scipy.real(np.exp(-1J*w[i]*t))
        #y_real = lambda t: (eval(func)+n[i]) * scipy.real(np.exp(-1J * w[i] * t))
        y_imag = lambda t: eval(func) * scipy.imag(np.exp(-1J * w[i] * t))
        #y_imag = lambda t:( eval(func)+n[i]) * scipy.imag(np.exp(-1J * w[i] * t))
        a[i] = quad(y_real, t_min, t_max)[0]
        b[i] = quad(y_imag, t_min, t_max)[0]
        c[i] = np.sqrt(a[i] ** 2 + b[i] ** 2)
        d[i] = np.arctan(b[i] / a[i])
    a = np.asarray(a)
    c = np.asarray(c)
    d = np.asarray(d)
    '''plt.subplot(4, 1, 1)
    plt.plot(w, a)
    plt.grid()
    plt.title('复频谱')
    plt.subplot(4, 1, 2)
    plt.plot(w, c)
    plt.grid()
    plt.title('幅度频谱')
    plt.subplot(4, 1, 3)
    plt.plot(w, d, 'r--')
    plt.grid()
    plt.title('相位频谱')
    plt.subplot(4, 1, 4)
    t = t_show
    y = eval(func)
    plt.plot(t, y, 'c--')
    plt.title('时域')
    plt.grid()
    plt.show()'''
    plt.plot(w, c, 'r--')
    return c

