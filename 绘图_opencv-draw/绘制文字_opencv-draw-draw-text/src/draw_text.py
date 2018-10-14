'''
绘制字符
'''
import cv2
import numpy as np

# 初始化一个空画布 300×300 三通道 背景色为白色 
canvas = np.ones((400, 400, 3), dtype="uint8")
canvas *= 255

# 选择字体
font = cv2.FONT_HERSHEY_SIMPLEX
'''
text: 要写入的文本
org: 文本左下角在图像中的位置
fontFace: 文本字体
fontScale: 文本的放大倍数
tickness: 文本宽度
lineType: 线条样式
color: 颜色
'''
cv2.putText(canvas, text="HelloWorld", org=(50, 200), fontFace=font, fontScale=2, thickness=1, lineType=cv2.LINE_AA, color=(0, 0, 255))

cv2.imwrite("draw_text.png", canvas)