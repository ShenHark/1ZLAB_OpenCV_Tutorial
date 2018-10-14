import cv2
import numpy as np

img = cv2.imread('cat.png')
height,width,channel = img.shape

# 声明变换矩阵 向右平移10个像素， 向下平移30个像素
M = np.float32([[1, 0, 10], [0, 1, 30]])
# 进行2D 仿射变换
shifted = cv2.warpAffine(img, M, (width, height))

cv2.imwrite('shift_right_10_down_30.png', shifted)