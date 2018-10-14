'''
二值化图像-异或
'''
import cv2

circle = cv2.imread('bitwise_circle.png', cv2.IMREAD_GRAYSCALE)
rectangle = cv2.imread('bitwise_rectangle.png', cv2.IMREAD_GRAYSCALE) 

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imwrite("bitwise_xor.png", bitwiseXOR)
