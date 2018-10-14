import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# 保存为PNG图片
cv2.imwrite('cat3.jpg', img)