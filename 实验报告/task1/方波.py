'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-06 16:03:35
LastEditors  : 傅宇千
LastEditTime : 2020-09-14 21:01:38
'''
"""
    三角函数 合成方波
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号

def fangbo(x,n,a,f):
    for i in range(1, n + 1):
        y += (4*a/np.pi) * np.sin(2*np.pi*f*(2*i-1)*x)/(2*i-1)
    return y
# 准备x值
x = np.linspace(0, 0.02, 1000)

# 叠加1条曲线 组成方波
n =1
y1 = np.zeros(1000)
for i in range(1, n + 1):
    y1 += (12/np.pi) * np.sin(2*np.pi*50*(2*i-1)*x)/(2*i-1)

# 叠加2条曲线 组成方波
n =2
y2 = np.zeros(1000)
for i in range(1, n + 1):
    y2 += (12/np.pi) * np.sin(2*np.pi*50*(2*i-1)*x)/(2*i-1)

# 叠加5条曲线 组成方波
n =5
y3 = np.zeros(1000)
for i in range(1, n + 1):
    y3 += (12/np.pi) * np.sin(2*np.pi*50*(2*i-1)*x)/(2*i-1)

# 叠加19条曲线 组成方波
n =19
y4 = np.zeros(1000)
for i in range(1, n + 1):
    y4 += (12/np.pi) * np.sin(2*np.pi*50*(2*i-1)*x)/(2*i-1)


# 绘制图片
plt.grid(linestyle=":")
plt.plot(x, y1, label="基波")
plt.plot(x, y2, label="三次")
plt.plot(x, y3, label="五次")
plt.plot(x, y4, label="十九次")
plt.xlabel("时间/s")
plt.ylabel("幅度")

plt.legend()
plt.show()





