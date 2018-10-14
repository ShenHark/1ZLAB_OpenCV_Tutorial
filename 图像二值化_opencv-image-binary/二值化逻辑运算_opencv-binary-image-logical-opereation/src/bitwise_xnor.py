'''
二值化图像抑或非
'''
import cv2

circle = cv2.imread('bitwise_circle.png', cv2.IMREAD_GRAYSCALE)
rectangle = cv2.imread('bitwise_rectangle.png', cv2.IMREAD_GRAYSCALE) 

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
bitwiseNOR = cv2.bitwise_not(cv2.bitwise_or(rectangle, circle))

bitwiseXNOR = cv2.bitwise_or(bitwiseAnd, bitwiseNOR)
cv2.imwrite("bitwise_xnor.png", bitwiseXNOR)