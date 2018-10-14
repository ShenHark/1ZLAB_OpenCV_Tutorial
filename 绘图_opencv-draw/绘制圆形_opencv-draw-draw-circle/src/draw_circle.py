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