'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-06 17:22:29
LastEditors  : 傅宇千
LastEditTime : 2020-09-14 20:47:32
'''
# 导入 需要的 library 库  
import numpy as np # 科学计算
import matplotlib.pyplot as plt # 画图工具
import scipy.signal as sg # 导入 scipy 的 signal 库 重命名为 sg
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号

ns=200
fs=ns/2


str1=str(fs)
x0=np.linspace(-1,1,1000)
x=np.linspace(-1,1,ns)  #抽样
n =1000
#三角波
# a=3*4/np.pi/np.pi*2
# y = np.zeros_like(x)
# for i in range(1,n,2):
#     y+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*x)

# y0 = np.zeros_like(x0)
# for i in range(1,n,2):
#     y0+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*x0)

#方波
# y = np.zeros_like(x)
# for i in range(1, n + 1):
#     y += (12/np.pi) * np.sin(2*np.pi*(2*i-1)*x)/(2*i-1)
# y0 = np.zeros_like(x0)
# for i in range(1, n + 1):
#     y0 += (12/np.pi) * np.sin(2*np.pi*(2*i-1)*x0)/(2*i-1)

# #正弦波
y0=3*np.sin(2*np.pi*50*x0)
y=3*np.sin(2*np.pi*50*x)



def fft(y,sampling_rate,fft_size):
    xs = y
    xf = np.fft.rfft(xs) / fft_size
    freqs = np.linspace(0, sampling_rate / 2,  fft_size / 2 + 1)
    xfp = np.abs(xf)
    return freqs,xfp


freqs,xfp=fft(y,fs,ns)
freqs0,xfp0=fft(y0,500,1000)
plt.figure(1)
plt.subplot(211)
plt.plot(x0,y0,'blue')
plt.xlabel("时间/s")
plt.ylabel("振幅")
plt.title('原信号')

plt.subplot(212)
plt.stem(x,y,'blue')
plt.xlabel("时间/s")
plt.ylabel("振幅")
plt.title('抽样频率'+str1+'Hz')

# b, a = sg.butter(8, 0.1, 'lowpass') 
b, a = sg.butter(8, 0.1, 'lowpass') 
y1 = sg.filtfilt(b, a, y)       #data为要过滤的信号

plt.figure(2)
plt.plot(x,y1,'blue')
plt.xlabel("时间/s")
plt.ylabel("振幅")
plt.title('恢复')

plt.figure(3)
plt.subplot(211)
plt.plot(freqs0, xfp0)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('频谱')

plt.subplot(212)
plt.plot(freqs, xfp)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('抽样频率为'+str1+'Hz时的频谱')

plt.show()

