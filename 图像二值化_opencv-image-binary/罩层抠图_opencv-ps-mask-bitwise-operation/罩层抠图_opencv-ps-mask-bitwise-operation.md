
# 罩层抠图

## 概要

本节课，阿凯带大家通过罩层对彩图进行二值化操作，最终实现抠图与图像拼接的功能。


**keywords** 罩层 MASK 二值化 抠图
![png](./image/output_22_1.png)


## 图像二值化


```python
import cv2
```


```python
# 载入原图
img = cv2.imread('cat.jpeg')
```


```python
from matplotlib import pyplot as plt
```


```python
# 展示图像
plt.imshow(img[:, :, ::-1])
```






![png](./image/output_5_1.png)



```python
# 图像二值化
img_bin = cv2.inRange(img, lowerb=(9, 16, 84), upperb=(255, 251, 255))
```


```python
plt.imshow(img_bin, cmap='gray')
```






![png](./image/output_7_1.png)


## 数学形态学处理


```python
# 数学形态学预处理
import numpy as np
kernel = np.ones((5,5), np.uint8)
img_bin = cv2.erode(img_bin, kernel, iterations=1)
img_bin = cv2.dilate(img_bin, kernel, iterations=2)
plt.imshow(img_bin, cmap='gray')
```




![png](./image/output_9_1.png)


## 筛选连通域


```python
# 过滤掉小的contours
# 获取边缘信息
_, contours, hierarchy = cv2.findContours(image=img_bin,mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)


def contours_area(cnt):
    # 计算countour的面积
    (x, y, w, h) = cv2.boundingRect(cnt)
    return w * h

# 获取面积最大的contour
max_cnt = max(contours, key=lambda cnt: contours_area(cnt))
```


```python
# 创建空白画布
mask = np.zeros_like(img_bin)
# 获取面积最大的 contours
mask = cv2.drawContours(mask,[max_cnt],0,255,-1)
# 打印罩层
plt.imshow(mask, cmap='gray')
```




![png](./image/output_12_1.png)


## 抠图-带罩层的二值化与操作

img跟它本身进行或/与操作（其实他们的结果是一样的) 在罩层区域（MASK）内进行。
罩层区域为0, 黑色。 

二值化操作就是 如果两个img的该点的像素点都不为零则保留原来的取值，否则就是黑色。


```python
# 使用罩层对原来的图像进行抠图
sub_img = cv2.bitwise_or(img,img,mask=mask)
# sub_img = cv2.bitwise_and(img,img,mask=mask)

plt.imshow(sub_img[:,:,::-1])
```






![png](./image/output_14_1.png)


哇， 大白猫就抠出来了

## 换个背景颜色


```python
# 给大白猫换个背景
background = np.zeros_like(img)
background[:,:,:]  = (150, 198, 12)
plt.imshow(background[:,:,::-1])
```






![png](./image/output_17_1.png)



```python
# 获取新的背景
new_background = cv2.bitwise_or(background, background, mask=cv2.bitwise_not(mask))
plt.imshow(new_background[:,:,::-1])
```






![png](./image/output_18_1.png)


## 图片合并 cv2.add



```python
new_img = cv2.add(new_background, sub_img)
plt.imshow(new_img[:,:,::-1])
```






![png](./image/output_20_1.png)


## 高斯模糊

拼接感太强，做一下高斯模糊


```python
# 用5*5的kernel进行高斯模糊
new_img_blur = cv2.GaussianBlur(new_img, (9,9), 5)
plt.imshow(new_img_blur[:,:,::-1])
```





![png](./image/output_22_1.png)



## 推广

**1Z实验室出品** **1zlab: make things easy** 致力于在机器人+计算机视觉+人工智能的重叠区域, 制作小白友好的教程.

![img](https://camo.githubusercontent.com/12bb778212425766924226dfa6d1ae45c73b8c42/68747470733a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f313139393732382d353839613830666637376633383064382e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31303030)

