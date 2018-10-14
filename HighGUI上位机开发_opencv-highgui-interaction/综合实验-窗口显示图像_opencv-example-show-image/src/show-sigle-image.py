import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# 展示图像
cv2.imshow('image',img)
# 等待按键摁下 最多5s钟
# 如果超时key_pressed 就会等于-1
key_pressed = cv2.waitKey(5000)
print("有按键摁下或者已超时")
# 使用chr() 
print("Key Pressed : {}  == {}".format(key_pressed, chr(key_pressed)))

# 关闭所有窗口
cv2.destroyAllWindows()
# 或者是这样， 销毁创建的单个窗口
# cv2.destroyWindow('image')