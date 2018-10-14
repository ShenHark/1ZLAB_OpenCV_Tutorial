# 绘制直线


## 概要
讲解了如何使用OpenCV在图片中绘制直线.

**keywords** OpenCV 直线绘制 

## 绘制直线(cv2.line)

```python
# 绘制一根红色的线  宽度为3
cv2.line(img=canvas, pt1=(300, 0), pt2=(0, 300), color=COLOR_MAP["red"], thickness=3)
```

**参数说明**

* `img` 图片(画布)
* `pt1` 直线起始端坐标 (x, y)
* `pt2` 直线结束端坐标 (x, y)
* `color` 颜色
* `thickness` 线宽

当然我们也可以简写

```python
cv2.line(canvas, (300, 0), (0, 300), COLOR_MAP["red"], 3)
```

可是一旦参数变多， 你就不知道哪个是哪个了， 一个规范的做法还是要加上参数名。

**演示样例**

![draw_line.png](./image/draw_line.png)

`src/draw_line.py`

```python
import cv2
import numpy as np

# 预设几种颜色 B
COLOR_MAP = {
    "green": (0, 255, 0),
    "red": (0, 0, 255)
}

'''
初始化一个彩色的画布
颜色为BGR色彩空间
'''
def InitCanvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas

# 初始化一个空画布 300×300 三通道 背景色为黑色 
canvas = InitCanvas(300, 300)

# pt1 线段起始点， pt2 线段终止点
# 在画布canvas上， 从(0，0） 到(300,300) 绘制一根绿色直线
cv2.line(canvas, pt1=(0, 0), pt2=(300, 300), color=COLOR_MAP["green"])

# 颜色变为红色 BGR
red = (0, 0, 255)
# 绘制一根红色的线  宽度为3
cv2.line(img=canvas, pt1=(300, 0), pt2=(0, 300), color=COLOR_MAP["red"], thickness=3)
cv2.imshow("Canvas", canvas)

cv2.imwrite("draw_line.png", canvas)

cv2.waitKey(0)

```