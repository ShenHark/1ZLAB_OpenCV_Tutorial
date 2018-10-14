import cv2
import numpy as np

img = cv2.imread('cat.png')

def translate(image, x, y):

    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


shifted = translate(img, 10, 30)
cv2.imwrite('shift_right_10_down_30.png', shifted)