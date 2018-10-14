import numpy as np
import cv2

img = cv2.imread('cute_princess.png')
# 读入灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 转化为二值化图
ret,thresh = cv2.threshold(gray,127,255,0)
# 获取边缘信息
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for idx,cnt in enumerate(contours):
    tmp = cv2.drawContours(np.copy(img), [cnt], 0, (0,255,0), 3)
    print("Contour No.%d"%(idx))
    print(cnt)
    cv2.imwrite('contours_part_%d.png'%(idx), tmp)