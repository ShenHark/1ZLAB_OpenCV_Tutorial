'''
使用仿射矩阵实现反转
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.png')
height,width,channel = img.shape

# 水平翻转
M1 = np.float32([[-1, 0, width], [0, 1, 0]])
flip_h =  cv2.warpAffine(img, M1, (width, height))

# 垂直翻转
M2 = np.float32([[1, 0, 0], [0, -1, height]])
flip_v =  cv2.warpAffine(img, M2, (width, height))

# 水平垂直同时翻转
M3 = np.float32([[-1, 0, width], [0, -1, height]])
flip_hv =  cv2.warpAffine(img, M3, (width, height))

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