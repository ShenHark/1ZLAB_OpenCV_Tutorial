'''
根据fx跟fy进行图像缩放
'''
import cv2
import numpy as np

img = cv2.imread('cat.jpg')
height,width,channel = img.shape

# 指定输出图片
dst = np.zeros((100, 100, 3), dtype='uint8')

# 指定新图片的维度与插值算法（interpolation）
cv2.resize(img, dst=dst, dsize=(dst.shape[1], dst.shape[0]), fx=1.5, fy=2)

cv2.imwrite('cat_resize_from_dst.png', dst)