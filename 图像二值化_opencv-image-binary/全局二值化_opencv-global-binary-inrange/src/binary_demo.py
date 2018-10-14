import cv2
import numpy as np

# 读入图片
img = cv2.imread('tiaoyitiao.png')
# 判断图片是否正确读入
if img is None:
    print("请检查图片路径")
    exit()

# 阈值下界
lowerb = (50, 36, 36)
# 阈值上界
upperb = (104, 80, 80)

# 图像二值化
mask = cv2.inRange(img, lowerb, upperb)

cv2.namedWindow("mask", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow('mask', mask)
cv2.waitKey(0)