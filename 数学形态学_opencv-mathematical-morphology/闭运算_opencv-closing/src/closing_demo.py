'''
    数学形态学 闭运算 closing
'''
import cv2
import numpy as np

# 迭代次数
iter_time = 1
# 读入灰度图
img = cv2.imread("dao-bin.png", flags=cv2.IMREAD_GRAYSCALE)

# 创建 核
kernel = np.ones((5,5), np.uint8)
# 闭运算
closing_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=iter_time)

cv2.imwrite('dao_closing_k5_iter%d.png'%(iter_time), np.hstack((img, closing_img)))