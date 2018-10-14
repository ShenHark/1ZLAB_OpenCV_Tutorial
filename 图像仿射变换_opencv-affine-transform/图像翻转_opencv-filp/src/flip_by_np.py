'''
使用numpy的索引进行图像反转
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.png')
height,width,channel = img.shape

# 水平翻转
flip_h =  img[:,::-1]

# 垂直翻转
flip_v =  img[::-1]

# 水平垂直同时翻转
flip_hv =  img[::-1, ::-1]

def bgr2rbg(img):
    '''
        将颜色空间从BGR转换为RBG
    '''
    return img[:,:,::-1]

plt.subplot(221)
plt.title('SRC')
plt.imshow(bgr2rbg(img))

plt.subplot(222)
plt.title('Horizontally')
plt.imshow(bgr2rbg(flip_h))

plt.subplot(223)
plt.title('Vertically')
plt.imshow(bgr2rbg(flip_v))

plt.subplot(224)
plt.title('Horizontally & Vertically')
plt.imshow(bgr2rbg(flip_hv))

plt.show()