import wave
from scipy.fftpack import fft
import numpy as np
import pylab as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
mpl.rcParams['axes.unicode_minus'] = False  #显示负号

#打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
f = wave.open(r"D:\学习\大三上\数字信号\实验\task5\DING.wav", "rb")
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
str_data = f.readframes(nframes)
f.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
wave_data = np.fromstring(str_data, dtype=np.short)
#将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
wave_data.shape = -1, 2
#转置数据
wave_data = wave_data.T
wave_data=wave_data[0]
y = wave_data
#通过取样点数和取样频率计算出每个取样的时间。
time = np.arange(0, nframes) / framerate


fft_y = fft(y)  #快速傅里叶变换
N = 200
x0 = np.arange(N)  # 频率个数
half_x = x0[range(int(N / 2))]  #取一半区间

abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
angle_y = np.angle(fft_y)  #取复数的角度
normalization_y = abs_y / N  #归一化处理（双边频谱）
normalization_half_y = normalization_y[range(int(N / 2))]  #由于对称性，只取一半区间（单边频谱）

#print(params)

plt.figure(1)
plt.subplot(311)
plt.plot(time, wave_data)
plt.xlabel("时间")
plt.title("原波形")

plt.subplot(312)
plt.plot(half_x,normalization_half_y)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('频谱')
plt.show()
