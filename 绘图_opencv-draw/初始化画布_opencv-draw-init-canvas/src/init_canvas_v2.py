'''
初始化画布
'''
import cv2
import numpy as np

# 初始化一个彩色的画布 - cv2版本
def init_canvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    
    # 将原来的三个通道抽离出来， 分别乘上各个通道的值
    (channel_b, channel_g, channel_r) = cv2.split(canvas)
    # 颜色的值与个通道的全1矩阵相乘
    channel_b *= color[0]
    channel_g *= color[1]
    channel_r *= color[2]

    # cv.merge 合并三个通道的值
    return cv2.merge([channel_b, channel_g, channel_r])

canvas = init_canvas(200, 200, color=(125, 40, 255))

cv2.imshow('canvas', canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()