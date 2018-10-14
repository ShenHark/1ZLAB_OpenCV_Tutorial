# -*- coding: utf-8 -*- 
import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.png', cv2.IMREAD_COLOR)

print("================打印一下图像的属性================")
print("图像对象的类型 {}".format(type(img)))
print(img.shape)
print("图像宽度: {} pixels".format(img.shape[1]))
print("图像高度: {} pixels".format(img.shape[0]))
print("通道: {}".format(img.shape[2]))
print("图像分辨率: {}".format(img.size))
print("数据类型: {}".format(img.dtype))