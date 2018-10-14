import numpy as np
import cv2

gray = cv2.imread('cute_princess.png', cv2.IMREAD_GRAYSCALE)

# 设定模式
mode = cv2.RETR_TREE
# 获取边缘信息
image, contours, hierarchy = cv2.findContours(image=gray,mode=mode, method=cv2.CHAIN_APPROX_SIMPLE)

# 创建画布
canvas = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# 绘制轮廓
cv2.drawContours(image=canvas, contours=contours, contourIdx=-1, color=(0,255,0), thickness=3)

# 保存画布
cv2.imwrite('countours_part_all_mode_%d.png'%(mode), canvas)
# 打印继承矩阵
print(hierarchy)