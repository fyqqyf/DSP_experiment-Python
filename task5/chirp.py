'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-14 13:33:31
LastEditors  : 傅宇千
LastEditTime : 2020-09-21 16:53:54
'''
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np
import scipy.signal as sg
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
mpl.rcParams['axes.unicode_minus'] = False  #显示负号

t = np.linspace(0, 10, 2048)
w = chirp(t, f0=6, f1=1, t1=10, method='linear')

def fft(y,sampling_rate,fft_size):
    xs = y
    xf = np.fft.rfft(xs) / fft_size
    freqs = np.linspace(0, sampling_rate / 2,  fft_size / 2 + 1)
    xfp = np.abs(xf)
    return freqs,xfp

# y = w[0:1024]

# freqs,xfp=fft(y,1024/5,1024)

y = w[0:2048]

freqs,xfp=fft(y,2048/5,2048)

plt.figure(1)
plt.subplot(211)
plt.plot(t, w)
plt.xlabel("时间")
plt.ylabel("振幅")
plt.title("原波形")

plt.subplot(212)
plt.plot(freqs, xfp)
plt.xlabel("频率/Hz")
plt.ylabel("振幅")
plt.title('频谱')

plt.show()
