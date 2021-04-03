# signal-processing
## there are some visualization about signals

# [对信号的时域频域及相域的观察](https://github.com/wang-ting000/signal-processing/blob/main/example_scenes.py)
[video:](https://github.com/wang-ting000/signal-processing/blob/main/ShowSignal.mp4)

# [计算相关的代码](ralation.py)

# FT

1. [傅里叶级数展开](傅里叶分解.py)
2. [正弦信号](sin信号.py)，[图示](sin信号的FT.svg)
3. DFS
4. DFT
5. DTFT


# PSD

使用条件：平稳信号，自相关函数和其功率谱密度是一对傅里叶变换对  

而非平稳信号由于自相关函数不仅仅和时间差有关系，无法根据功率谱密度表示

物理意义：
频率和时间有关系，因此不含时间维度的PSD无法体现信号特征

改进：用时频图来展示信号
eg:

![](https://i.loli.net/2021/04/03/JSBCkg15ncOFmAy.png)
![](https://i.loli.net/2021/04/03/Zs8etgwnAUi9pLC.png)
![](https://i.loli.net/2021/04/03/AWJzgT6K8ZGylH3.png)
