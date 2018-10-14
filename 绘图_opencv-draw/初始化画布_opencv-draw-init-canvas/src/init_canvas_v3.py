'''
初始化画布
'''
import cv2
import numpy as np

def init_canvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    # Blue 
    canvas[:,:,0] = color[0]
    # Green
    canvas[:,:,1] = color[1]
    # Red
    canvas[:,:,2] = color[2]

    return canvas

canvas = init_canvas(200, 200, color=(125, 40, 255))

cv2.imshow('canvas', canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()