# 程序说明

## 程序流程

![流程图](https://i.loli.net/2020/09/16/aJK6qvZ34fx8edF.png)

## 函数说明

```python
multenterbox(msg,title,fields,values)
```

### 用于构建GUI

msg:显示提示信息

title:显示标题

fields:变量名称

values:默认初始值

```
StateSpace(a, b, c, d)
```

### 用于构建状态空间

$$
{\dot {\mathbf {x} }}(t)=\mathbf {A} (t)\mathbf {x} (t)+\mathbf {B} (t)\mathbf {u} (t)\\
{\displaystyle \mathbf {y} (t)=\mathbf {C} (t)\mathbf {x} (t)+\mathbf {D} (t)\mathbf {u} (t)}
$$
a,b,c,d为状态方程中的参数(以矩阵形式输入)

```
step(system, X0, T, N)
```

### 用于求解状态方程

system:状态方程

x0:初始状态向量

T:初始时间点

N:需计算的时间点数