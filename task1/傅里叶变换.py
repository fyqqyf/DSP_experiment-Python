'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-06 17:45:36
LastEditors  : 傅宇千
LastEditTime : 2020-09-14 18:09:37
'''
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号

ns=1000#采样数目

#采样点选择
x=np.linspace(-1,1,ns)      
fs=ns/2#采样频率

#设置方波信号
n1 =1000
y1 = np.zeros_like(x)
for i in range(1, n1 + 1):
    y1 += (12/np.pi) * np.sin(2*np.pi*0.5*(2*i-1)*x)/(2*i-1)

#设置三角波信号
n2 =1000#累加次数
a=3*4/np.pi/np.pi*2
f=0.5
y2 = np.zeros_like(x)
for i in range(1,n2,2):
    y2+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*f*x)

def fft(y,sampling_rate,fft_size):
    xs = y
    xf = np.fft.rfft(xs) / fft_size
    freqs = np.linspace(0, sampling_rate / 2,  fft_size / 2 + 1)
    xfp = np.abs(xf)
    return freqs,xfp

freqs1,xfp1=fft(y1,fs,ns)
freqs2,xfp2=fft(y2,fs,ns)
plt.subplot(221)
plt.plot(x,y1) 
plt.xlabel("时间/s")
plt.ylabel("振幅")    
plt.title('方波原始波形')
 
plt.subplot(222)
plt.plot(freqs1, xfp1)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('方波频谱')

plt.subplot(223)
plt.plot(x,y2) 
plt.xlabel("时间/s")
plt.ylabel("振幅")    
plt.title('三角波原始波形')
 
plt.subplot(224)
plt.plot(freqs2, xfp2)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('三角波频谱')
 
plt.show()
 