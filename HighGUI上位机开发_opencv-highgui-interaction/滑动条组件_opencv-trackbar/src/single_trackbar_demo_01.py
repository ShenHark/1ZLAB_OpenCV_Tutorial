import cv2

# 创建窗口
cv2.namedWindow('image_win')


value = None

def update(x):
    # 回调函数 更新value的值
    global value
    value = x
    print('Update Value, value ={}'.format(value))

# 创建一个滑动条对象 数值名字叫做 value_name
# 滑动条创建在 image_win 窗口之下
# 取值范围为 0-255, 回调函数为update
cv2.createTrackbar('value_name','image_win',0,255,update)

# 等待按键按下
cv2.waitKey(0)
# 销毁窗口
cv2.destroyAllWindows()