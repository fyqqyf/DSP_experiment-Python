'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-08 12:27:06
LastEditors  : 傅宇千
LastEditTime : 2020-09-16 19:13:17
'''
'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-08 12:27:06
LastEditors  : 傅宇千
LastEditTime : 2020-09-14 16:06:20
'''

import wave
from scipy.fftpack import fft, ifft
import numpy as np
import pylab as plt
from matplotlib.pylab import mpl
import scipy.signal as sg
from pyaudio import PyAudio, paInt16

mpl.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
mpl.rcParams['axes.unicode_minus'] = False  #显示负号

CHUNK = 1024  # wav文件是由若干个CHUNK组成的，CHUNK我们就理解成数据包或者数据片段。
FORMAT = paInt16  # 量化位数16位
CHANNELS = 2  #声道是双声道。
RATE = 44100  # 采样率
RECORD_SECONDS = 5  # 录制时间:5秒


def get_audio(filepath):
    isstart = str(input("是否开始录音？ （1/0）")) 
    if isstart == str("1"):
        pa = PyAudio()
        stream = pa.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         input=True,
                         frames_per_buffer=CHUNK)
        print("*" * 10, "开始录音：请在5秒内输入语音")
        frames = []  # 定义一个列表
        for i in range(0, int(RATE / CHUNK *
                              RECORD_SECONDS)):  # 循环，采样率 44100 / 1024 * 5
            data = stream.read(CHUNK)  # 读取chunk个字节 保存到data中
            frames.append(data)  # 向列表frames中添加数据data
        print("*" * 10, "录音结束\n")

        stream.stop_stream()
        stream.close()  # 关闭
        pa.terminate()  # 终结

        save_wave_file(pa, filepath, frames)
    elif isstart == str("0"):
        exit()
    else:
        print("无效输入，请重新选择")
        get_audio(filepath)


def save_wave_file(pa, filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(data))
    wf.close()


filepath = 'task5/01.wav'
get_audio(filepath)

#打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
f = wave.open(r"D:\学习\大三上\数字信号\实验\task5\01.wav", "rb")
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。
# wave模块只支持非压缩的数据，因此可以忽略最后两个信息
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
str_data = f.readframes(nframes)
f.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
wave_data = np.fromstring(str_data, dtype=np.short)

wave_data.shape = -1, 2
#转置数据
wave_data = wave_data.T
#取某一声道
wave_data = wave_data[0]
y = wave_data
#通过取样点数和取样频率计算出每个取样的时间。
time = np.arange(0, nframes) / framerate
time1 = np.arange(0, 2048) / framerate
time2 = np.arange(0, 1024) / framerate

fft_size1 = 2048
fft_size2 = 1024

sampling_rate = framerate  #采样频率

xs1 = y[0:fft_size1]  # 从波形数据中取样fft_size个点进行运算
xf1 = np.fft.rfft(xs1) / fft_size1

#通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
freqs1 = np.linspace(0, sampling_rate / 2, fft_size1 / 2 + 1)
xfp1 = np.abs(xf1)

xs2 = y[:fft_size2]
xf2 = np.fft.rfft(xs2) / fft_size2

freqs2 = np.linspace(0, sampling_rate / 2, fft_size2 / 2 + 1)
xfp2 = np.abs(xf2)

xs = y
xf = np.fft.rfft(xs) / nframes
freqs = np.linspace(0, sampling_rate / 2, nframes / 2 + 1)
xfp = np.abs(xf)

#求傅里叶变换
z = np.fft.ifft(xf, 220160)

#只保留幅度最大的正弦分量
f = np.argmax(xfp)
a = 5 * xfp[f]
y3 = a * np.sin(2 * np.pi * f * time)
wave_data = y3.astype(np.short)
#open a wav document
wav = wave.open("task5/test.wav", "wb")
#set wav params
wav.setnchannels(2)
wav.setsampwidth(sampwidth)
wav.setframerate(20000)
#turn the data to string
wav.writeframes(wave_data.tostring())
wav.close()

plt.figure(1)
plt.subplot(311)
plt.plot(time, y)
plt.xlabel("时间")
plt.title("原波形")

plt.subplot(312)
plt.plot(freqs, xfp)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('频谱')

plt.subplot(313)
plt.plot(time, z)
plt.xlabel("时间")
plt.title("原波形")

plt.figure(2)

plt.subplot(211)
plt.plot(time1, xs1)
plt.xlabel("时间")
plt.title("原波形")

plt.subplot(212)
plt.plot(freqs1, xfp1)
plt.xlabel("频率/HZ")
plt.ylabel("振幅")
plt.title('频谱')

plt.figure(3)

plt.subplot(211)
plt.plot(time2, xs2)
plt.xlabel("时间")
plt.title("原波形")

plt.subplot(212)
plt.plot(freqs2, xfp2)
plt.xlabel("频率/Hz")
plt.ylabel("振幅")
plt.title('频谱')

plt.figure(4)
plt.plot(time, wave_data)
plt.xlabel("时间")
plt.title("原波形")

plt.show()
