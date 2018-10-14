'''
反转Demo
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.png')

def bgr2rbg(img):
    '''
        将颜色空间从BGR转换为RBG
    '''
    return img[:,:,::-1]

# 水平翻转
flip_h = cv2.flip(img, 1)
# 垂直翻转
flip_v = cv2.flip(img, 0)
# 同时水平翻转与垂直翻转
flip_hv = cv2.flip(img, -1)

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