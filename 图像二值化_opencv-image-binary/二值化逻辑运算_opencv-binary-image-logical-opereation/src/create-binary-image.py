'''
创建二值化的矩形还有圆形
'''
import cv2
import numpy as np

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imwrite("bitwise_rectangle.png", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imwrite("bitwise_circle.png", circle)