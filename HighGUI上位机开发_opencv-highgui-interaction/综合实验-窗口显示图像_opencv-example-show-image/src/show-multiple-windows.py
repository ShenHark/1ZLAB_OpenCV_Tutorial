import numpy as np
import cv2

# 导入一张图像 模式为彩色图片 cv2.IMREAD_COLOR = 1
img_color = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
# 导入一张图片 模式为灰度图 cv2.IMREAD_GRAYSCALE = 0
img_gray = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
# 导入一张图片  cv2.IMREAD_UNCHANGED = -1 包括 alpha透明度通道 
img_alpha = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

# 创建一个名字叫做 image_color 的窗口 窗口可拉伸
cv2.namedWindow('image_color', cv2.WINDOW_NORMAL)
# 在名字叫做 image_color 的窗口下展示图像 
cv2.imshow('image_color',img_color)

cv2.namedWindow('image_grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('image_grayscale', img_gray)


cv2.namedWindow('image_alpha', cv2.WINDOW_NORMAL)
cv2.imshow('image_alpha', img_alpha)


# 检测按下的按钮
print("请按 按键 e (exit)键关闭窗口")
while True:
    key_pressed = cv2.waitKey(100)
    if key_pressed >= 0:
        # 打印一下按键记录
        print("Key Pressed : {}  == {}".format(key_pressed, chr(key_pressed)))
    # 匹配为e后 跳出 while循环
    if key_pressed == ord('e'):
        break

# 关闭所有打开的窗口
cv2.destroyAllWindows()