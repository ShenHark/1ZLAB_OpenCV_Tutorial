'''
    数学形态学 开运算 opening
'''
import cv2
import numpy as np

# 迭代次数
iter_time = 4
# 读入灰度图
img = cv2.imread("dao.png", flags=cv2.IMREAD_GRAYSCALE)

# 创建 核
kernel = np.ones((5,5), np.uint8)
# 开运算
opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=iter_time)

cv2.imwrite('dao_opening_k5_iter%d.png'%(iter_time), np.hstack((img, opening_img)))