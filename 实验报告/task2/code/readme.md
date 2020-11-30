# 程序说明

## 程序流程

![流程图](https://i.loli.net/2020/09/14/RDhLsf5JB39oZIC.png)

## 函数说明

与**实验一**类似

```python
fangbo(x,n,a,f):
```

### 生成方波

x为输入横坐标

n为谐波次数

a为振幅

f为频率

```python
sanjiaobo(x,n,a,f)
```

### 生成三角波

x为输入横坐标

n为谐波次数

a为振幅

f为频率

```python
fft(y,sampling_rate,fft_size)
```

### 傅里叶变换函数

y为待变换函数

sampling_rate为采样率,用于对频率归一化

fftsize为傅里叶取样范围,提取信号中某一时间段进行傅里叶变换,作为该信号的近似频谱