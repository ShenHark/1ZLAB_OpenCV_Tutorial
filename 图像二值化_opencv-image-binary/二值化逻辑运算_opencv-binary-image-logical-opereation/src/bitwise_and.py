'''
二值化图像逻辑与
'''
import cv2

circle = cv2.imread('bitwise_circle.png', cv2.IMREAD_GRAYSCALE)
rectangle = cv2.imread('bitwise_rectangle.png', cv2.IMREAD_GRAYSCALE) 
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imwrite("bitwise_and.png", bitwiseAnd)