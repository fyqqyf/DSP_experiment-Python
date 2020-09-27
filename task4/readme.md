# 程序说明

## 程序流程

![流程图](https://i.loli.net/2020/09/16/FMcSUdOL3jGKNVD.png)

## 函数说明

```
get_audio(filepath)
```

### 采集语音信号

filepath:采集语音信号的保存路径

```
save_wave_file(pa,filename,data)
```

### 保存wav信号

pa:保存前的处理函数

filename:保存路径

data:wav信号



```python
fft(y,sampling_rate,fft_size)
```

### 傅里叶变换函数

y为待变换函数

sampling_rate为采样率,用于对频率归一化

fftsize为傅里叶取样范围,提取信号中某一时间段进行傅里叶变换,作为该信号的近似频谱



