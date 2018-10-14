import numpy as np
import cv2

# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win', cv2.WINDOW_NORMAL)

# windows下啥也不放置

# 检测按下的按钮
print("请按任意键关闭窗口")

# 如果没有下面的waitKey, 窗口会一闪而过, 后面会讲解
key_pressed = cv2.waitKey(0)

# cv2.destroyAllWindows()
cv2.destroyWindow('image_win')