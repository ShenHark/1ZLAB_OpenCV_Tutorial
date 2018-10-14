'''
测试二值化非
'''
import cv2

circle = cv2.imread('bitwise_circle.png', cv2.IMREAD_GRAYSCALE)

bitwiseNOT = cv2.bitwise_not(circle)
cv2.imwrite("bitwise_not_circle.png", bitwiseNOT)
