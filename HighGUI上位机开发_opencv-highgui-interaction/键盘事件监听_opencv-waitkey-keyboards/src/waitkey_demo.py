import cv2

# 创建一个窗口
cv2.namedWindow('image')


while True:
    # 等待按键事件发生
    key_code = cv2.waitKey(1000)
    
    if key_code != -1:
        print('key {} pressed!!! value={}'.format(chr(key_code), key_code))
        if chr(key_code) == 'q':
            # 退出程序
            print('Quit')
            break
    else:
        # 没有按键按下
        print('no key pressed , wait 1s')

cv2.destroyWindow('image')