'''
使用仿射矩阵实现
'''
import numpy as np
import cv2

img = cv2.imread('cat.jpg')

height,width,channel = img.shape

# x轴焦距 1.5倍
fx = 1.5
# y轴焦距 2倍
fy = 2

# 声明变换矩阵 向右平移10个像素， 向下平移30个像素
M = np.float32([[fx, 0, 0], [0, fy, 0]])

# 进行2D 仿射变换
resized = cv2.warpAffine(img, M, (int(width*fx), int(height*fy)))
cv2.imwrite('resize_raw.png', resized)