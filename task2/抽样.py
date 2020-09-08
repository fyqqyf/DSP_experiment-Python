# 导入 需要的 library 库  
import numpy as np # 科学计算
import matplotlib.pyplot as plt # 画图工具
import scipy.signal as sg # 导入 scipy 的 signal 库 重命名为 sg
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号


x0=np.linspace(-0.1,0.1,1000)
# x=np.linspace(-0.1,0.1,300)  #抽样
# x=np.linspace(-0.5,0.5,100)  #抽样 正弦波
# x=np.linspace(-0.1,0.1,2000/100)  #抽样 方波
x=np.linspace(-0.1,0.1,30)  #抽样 三角波

#三角波
n =100
y = np.zeros_like(x)
for i in range(1,n,2):
    y+= (1/np.pi/np.pi)*(np.cos(2 * np.pi * i * x)/i/i) 

n =100
y0 = np.zeros_like(x0)
for i in range(1,n,2):
    y0+= (1/np.pi/np.pi)*(np.cos(2 * np.pi * i * x0)/i/i) 

# #方波
# n0=1000
# y0 = np.zeros(1000)
# for i in range(1, n0 + 1):
#     y0 += (6/np.pi) * np.sin(2*np.pi*50*(2*i-1)*x0)/(2*i-1)

# n=1000
# y = np.zeros(2000)
# for i in range(1, n + 1):
#     y += (6/np.pi) * np.sin(2*np.pi*50*(2*i-1)*x)/(2*i-1)

# #正弦波
# y0=3*np.sin(2*np.pi*6*x0)
# y=3*np.sin(2*np.pi*6*x)

plt.subplot(311)
plt.plot(x0,y0,'blue')
plt.xlabel("时间/s")
plt.ylabel("信号")
plt.title('原信号')

plt.subplot(312)
plt.stem(x,y,'blue')
plt.xlabel("时间/s")
plt.ylabel("信号")
plt.title('抽样')

# b, a = sg.butter(8, 0.1, 'lowpass') 
b, a = sg.butter(8, 0.1, 'lowpass') 
y1 = sg.filtfilt(b, a, y)       #data为要过滤的信号

plt.subplot(313)
plt.plot(x,y1,'blue')
plt.xlabel("时间/s")
plt.ylabel("信号")
plt.title('恢复')

plt.show()

