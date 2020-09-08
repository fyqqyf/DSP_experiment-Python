import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号
 
#采样点选择
x=np.linspace(-1,1,200)      

#设置正弦信号
y1=np.sin(2*np.pi*10*x)

#设置三角波信号
n =100
y = np.zeros_like(x)
for i in range(1,n,2):
    y+= (1/np.pi/np.pi)*(np.cos(2 * np.pi * i * x)/i/i)  


fft_y=fft(y) 
fft_y1=fft(y1)                         #快速傅里叶变换
 
N=200
x0 = np.arange(N)             # 频率个数
half_x = x0[range(int(N/2))]  #取一半区间
 
abs_y=np.abs(fft_y)
abs_y1=np.abs(fft_y1)                 # 取复数的绝对值，即复数的模(双边频谱)
angle_y=np.angle(fft_y)
angle_y1=np.angle(fft_y1)             #取复数的角度
normalization_y=abs_y/N
normalization_y1=abs_y1/N             #归一化处理（双边频谱）                              
normalization_half_y = normalization_y[range(int(N/2))]
normalization_half_y1 = normalization_y1[range(int(N/2))]      #由于对称性，只取一半区间（单边频谱）
 
plt.subplot(231)
plt.plot(x,y) 
plt.xlabel("时间/s")
plt.ylabel("信号")  
plt.title('三角波原始波形')
 
plt.subplot(232)
plt.plot(x0,normalization_y,'g')
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('三角波双边振幅谱')
 
plt.subplot(233)
plt.plot(half_x,normalization_half_y,'blue')
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('三角波单边振幅谱')

plt.subplot(234)
plt.plot(x,y1) 
plt.xlabel("时间/s")
plt.ylabel("信号")    
plt.title('正弦波原始波形')
 
plt.subplot(235)
plt.plot(x0,normalization_y1,'g')
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('正弦波双边振幅谱')

plt.subplot(236)
plt.plot(half_x,normalization_half_y1,'blue')
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('正弦波单边振幅谱')

plt.show()
 