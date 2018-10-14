'''
仿射矩阵实现缩放 fx,fy
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 生成一个随机噪点
img = np.uint8(np.random.randint(0,255,size=(5,5)))

height,width = img.shape

# x轴焦距 1.5倍
fx = 1.5
# y轴焦距 2倍
fy = 2

# 声明变换矩阵 向右平移10个像素， 向下平移30个像素
M = np.float32([[fx, 0, 0], [0, fy, 0]])

# 进行2D 仿射变换
resized = cv2.warpAffine(img, M, (int(width*fx), int(height*fy)))

print(img)
print(resized)

# 数据可视化
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.subplot(122)
plt.imshow(resized,cmap="gray")
plt.show()