import numpy as np
import cv2

img = cv2.imread('cute_princess.png')
# 读入灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 转化为二值化图
ret,thresh = cv2.threshold(gray,127,255,0)
# 获取边缘信息
image, contours, hierarchy = cv2.findContours(image=thresh,mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


all_cnt_img = cv2.drawContours(np.copy(img), contours, -1, (0,255,0), 3)

cv2.imwrite('countours_part_all.png', all_cnt_img)