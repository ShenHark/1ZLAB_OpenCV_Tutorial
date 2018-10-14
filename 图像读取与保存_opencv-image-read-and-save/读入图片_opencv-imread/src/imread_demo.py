import cv2

# 读入彩图
img_color = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
# 读入灰度图
img_gray = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)