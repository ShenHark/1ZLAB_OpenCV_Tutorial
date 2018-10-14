import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('bear.jpg', cv2.IMREAD_COLOR)


for quality in range(0, 100, 10):
    
    # 保存为PNG图片
    cv2.imwrite('bear_quality_{}.jpg'.format(quality), img, [cv2.IMWRITE_JPEG_QUALITY, quality])