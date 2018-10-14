# 窗口销毁

## 概要
本文讲解了如何销毁窗口

**keywords** destroyWindow 关闭窗口 HighGUI

## 销毁窗口API讲解
销毁所有窗口。

```python
cv2.destroyAllWindows()
```

销毁单个窗口, 传入要销毁的窗口名称

```
cv2.destroyWindow(window_name)
```

## 关闭单个窗口的样例


等待任意按键按下，然后关闭特定的窗口
`destroy_sigle_window.py`
```python
import cv2

# 创建一个窗口
cv2.namedWindow('image')

# 等待键盘按键按下
cv2.waitKey(0)

# 销毁窗口
cv2.destroyWindow('image')
```

思考题： 如果我不加`cv2.destroyWindow`会怎么样， 如果意外中断程序，窗口会怎么样？


## 关闭所有窗口的样例


`destroy_all_window_demo.py`
```python
import cv2

# 创建一个窗口
cv2.namedWindow('image1')
cv2.namedWindow('image2')
cv2.namedWindow('image3')
# 等待键盘按键按下
cv2.waitKey(0)

# 销毁所有窗口
cv2.destroyAllWindows()

```

