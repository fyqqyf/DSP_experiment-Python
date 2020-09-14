from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np
import scipy.signal as sg
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
mpl.rcParams['axes.unicode_minus'] = False  #显示负号

t = np.linspace(0, 10, 2000)
w = chirp(t, f0=6, f1=1, t1=10, method='linear')


y = w[0:1024]

fft_y = fft(y)  #快速傅里叶变换
N = 1000
x0 = np.arange(N)  # 频率个数
half_x = x0[range(int(N / 2))]  #取一半区间

abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
angle_y = np.angle(fft_y)  #取复数的角度
normalization_y = abs_y / N  #归一化处理（双边频谱）
normalization_half_y = normalization_y[range(int(N / 2))]  #由于对称性，只取一半区间（单边频谱）

plt.figure(1)
plt.subplot(211)
plt.plot(t, w)
plt.xlabel("时间")
plt.ylabel("振幅")
plt.title("原波形")

plt.subplot(212)
plt.plot(half_x, normalization_half_y)
plt.xlabel("频率/Hz")
plt.ylabel("振幅")
plt.title('频谱')

plt.show()
