
# 绘制圆形

## 概要
讲解了如何使用OpenCV在图片中绘制圆形.

**keywords** OpenCV 圆形绘制 

## 圆形绘制(cv2.circle)

```python
# 绘制一个红色圆 边缘宽度(thickness = 5)
cv2.circle(img=canvas, center=(150, 150), radius=60, color=(0, 0, 255), thickness=5)
```

**参数说明**

* `img` 画布

* `center` 圆形中心坐标

* `radius` 圆形半径

* `thickness` 线宽， 如果是-1,代表填充

**演示样例**

![draw_circle.png](./image/draw_circle.png)

`src/draw_circle.py`

```python
import cv2
import numpy as np

# 初始化一个空画布 300×300 三通道 背景色为白色 
canvas = np.ones((300, 300, 3), dtype="uint8")
canvas *= 255

# 绘制一个绿色的圆
cv2.circle(canvas, center=(150, 150), radius=50, color=(0, 255, 0))
# 绘制一个红色圆 边缘宽度(thickness = 5)
cv2.circle(img=canvas, center=(150, 150), radius=60, color=(0, 0, 255), thickness=5)
# 绘制一个蓝色的实心圆 (thickness = -1)
cv2.circle(canvas, (150, 150), 30, color=(255, 0, 0), thickness=-1)

cv2.imshow("circle", canvas)

cv2.imwrite("draw_circle.png", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
```