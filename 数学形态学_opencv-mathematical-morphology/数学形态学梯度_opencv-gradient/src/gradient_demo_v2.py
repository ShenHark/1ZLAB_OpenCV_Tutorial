'''
    数学形态学 获取形态学梯度 gradient
'''
import cv2
import numpy as np

# 读入灰度图
img = cv2.imread("dao.png", flags=cv2.IMREAD_GRAYSCALE)

# 创建 核
kernel = np.ones((5,5), np.uint8)
# 获取形态学梯度
erode = cv2.erode(img, kernel)
dilate = cv2.dilate(img,kernel)
gradient = cv2.bitwise_xor(dilate, erode)

cv2.imwrite('dao_gradient_k5_v2.png', np.hstack((img, gradient)))