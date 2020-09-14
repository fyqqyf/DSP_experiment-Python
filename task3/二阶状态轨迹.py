import scipy.signal as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
import easygui as g

mpl.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
mpl.rcParams['axes.unicode_minus'] = False  #显示负号

#GUI的创建
ret = g.multenterbox(msg='请输入电路参数',
                     title='二阶状态轨迹程序',
                     fields=['R', 'L', 'C'],
                     values=['1', '10', '0.1'])
R = float(ret[0])
L = float(ret[1])
C = float(ret[2])

t = np.arange(0, 100, 0.01)
a = np.array([[-R / L, -1 / L], [1 / C, 0]])
b = np.array([[1 / L], [0]])
c = np.array([[1, 0]])  #iL为输出
c1 = np.array([[0, 1]])  #vC为输出
d = np.array([[0]])
sys = sg.StateSpace(a, b, c, d)
sys1 = sg.StateSpace(a, b, c1, d)
t, y1 = sg.step(sys, 0, t, 1000)
t, y2 = sg.step(sys1, 0, t, 1000)

fig, ax = plt.subplots(3, 1)
#显示iL(t)
plt.subplot(311)
plt.plot(t, y1, 'blue')
plt.xlabel("时间/s")
plt.ylabel('iL(t)')

#显示vc(t)
plt.subplot(312)
plt.plot(t, y2, 'blue')
plt.xlabel("时间/s")
plt.ylabel('vC(t)')

#显示状态轨迹
plt.subplot(313)
plt.plot(y2, y1, 'blue')
plt.xlabel('vC(t)')
plt.ylabel('iL(t)')

#判断系统阻尼状态
alph = R / (2 * L)
omega = 1 / np.sqrt(L * C)
if (R == 0):
    str = '无阻尼'
else:
    if (alph > omega):
        str = '过阻尼'
    if (alph == omega):
        str = '临界阻尼'
    if (alph < omega):
        str = '欠阻尼'
print(str)
fig.suptitle("此时状态为" + str)
plt.show()
