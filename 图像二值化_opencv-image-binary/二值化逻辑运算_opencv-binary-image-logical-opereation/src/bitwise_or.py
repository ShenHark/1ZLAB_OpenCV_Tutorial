'''
二值化图像-或
'''
import cv2

circle = cv2.imread('bitwise_circle.png', cv2.IMREAD_GRAYSCALE)
rectangle = cv2.imread('bitwise_rectangle.png', cv2.IMREAD_GRAYSCALE) 

bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imwrite("bitwise_or.png", bitwiseOR)