import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('bear.png')


for cmpi in range(0, 10):
    # 保存为PNG图片
    cv2.imwrite('bear_compression_{}.png'.format(cmpi), img, [cv2.IMWRITE_PNG_COMPRESSION, cmpi])
    print("压缩级别 {}".format(cmpi))