import cv2
import time
# 创建窗口
cv2.namedWindow('image_win')


def do_something():
    print('Button Pressed!!')
    print('Do Something')


def update(x):
    if x == 1:
        do_something()
        cv2.waitKey(500)
        cv2.setTrackbarPos('button', 'image_win', 0)
    


cv2.createTrackbar('button','image_win',0,1,update)

# 等待按键按下
cv2.waitKey(0)
# 销毁窗口
cv2.destroyAllWindows()