# 程序说明

## 流程图

![流程图](https://i.loli.net/2020/09/14/aRBnXFp8WQbeG9t.png)

## 函数描述



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