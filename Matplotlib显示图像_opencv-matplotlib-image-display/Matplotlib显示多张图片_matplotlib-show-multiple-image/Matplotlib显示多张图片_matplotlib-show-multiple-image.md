# Matplotlib显示多张图片



## 概要

本文主要讲解了如何使用Matplotlib实现多窗口图片显示.



**keywords** subplot matplotlib 多窗口  图片显示



## subplot的API讲解

在Matplotlib里面绘制多个图，需要使用`subplot`方法， 具体的使用方法见官方文档[matplotlib.pyplot.subplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html)

subplot的函数原型如下：

```python
subplot(nrows, ncols, index, **kwargs)
```

第一个值`nrows` 代表有多少行， `ncols`代表有多少列 ， `index` 窗口编号，从1开始，一直到`nrows × ncolums`

 

例如Matplotlib被分成了2×3的窗口，他们的编号就依次为：

| 窗口编号 | colum=1 | colum=2 | column=3 |
| -------- | ------- | ------- | -------- |
| row =1   | 1       | 2       | 3        |
| row = 2  | 4       | 5       | 6        |



在执行`subplot` 函数之后的绘图操作，就相当于在这个格子下绘图.





## 例程-显示图片的RGB三个通道的图像



![three channel](./image/cat_threechannel_image.png)



`show-mutlple-image.py`

```python
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('cat.jpg')

b, g, r = cv2.split(img)


plt.subplot(2, 2, 1)
plt.title('origin')
plt.imshow(img[:,:,::-1])

plt.subplot(2, 2, 2)
plt.title('blue channel')
plt.imshow(b, cmap='Blues')

plt.subplot(2, 2, 3)
plt.title('green channel')
plt.imshow(g, cmap='Greens')

plt.subplot(2, 2, 4)
plt.title('red channel')
plt.imshow(r, cmap='Reds')


plt.show()


```

