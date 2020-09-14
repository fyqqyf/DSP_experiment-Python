'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-06 17:08:10
LastEditors  : 傅宇千
LastEditTime : 2020-09-14 17:40:49
'''
"""
    三角函数 合成三角波
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号

# 准备x值
x = np.linspace(0, 0.05, 2000)
a=3*4/np.pi/np.pi*2
f=50
# 叠加3条曲线 组成三角波
n =3
y1 = np.zeros_like(x)
for i in range(1,n,2):
    y1+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*f*x)

# 叠加100条曲线 组成三角波
n =100
y2 = np.zeros_like(x)
for i in range(1,n,2):
    y2+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*f*x)

# 叠加5条曲线 组成三角波
n =5
y3 = np.zeros_like(x)
for i in range(1,n,2):
    y3+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*f*x)

# 叠加19条曲线 组成三角波
n =19
y4 = np.zeros_like(x)
for i in range(1,n,2):
    y4+= a/i/i*np.sin(i*np.pi/2)*np.sin(2*np.pi*i*f*x)
# y4 = np.zeros(1000)
# for i in range(1, n + 1):
#     y4 += (12/np.pi/np.pi) * np.sin(2*np.pi*(2*i-1)*x)/np.sqrt(2*i-1)*np.power(-1,i-1)


# 绘制图片
plt.grid(linestyle=":")
plt.plot(x, y1, label="3条")
plt.plot(x, y3, label="5条")
plt.plot(x, y4, label="19条")
plt.plot(x, y4, label="100条")
plt.xlabel("时间/s")
plt.ylabel("信号")

plt.legend()
plt.show()


