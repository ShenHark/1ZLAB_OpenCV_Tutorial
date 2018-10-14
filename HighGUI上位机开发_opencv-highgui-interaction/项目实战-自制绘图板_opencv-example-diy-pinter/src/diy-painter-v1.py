'''
鼠标 每次双击，触发回调函数， 在点击处绘制一个圆圈

'''
import cv2  
import numpy as np  
  
# 鼠标回调函数  
# x, y 都是相对于窗口内的图像的位置

def draw_circle(event,x,y,flags,param): 
    # 判断事件是否为 Left Button Double Clicck 
    if event == cv2.EVENT_LBUTTONDBLCLK:  
        cv2.circle(img,(x,y),20,(255,0,0),-1)  
  
# 创建一个黑色图像，并绑定窗口和鼠标回调函数  
img = np.zeros((512,512,3), np.uint8)  
cv2.namedWindow('image')
# 设置鼠标事件回调
cv2.setMouseCallback('image',draw_circle)  
  
while(True):  
    cv2.imshow('image',img)  
    if cv2.waitKey(20) == ord('q'):  
        break  
cv2.destroyAllWindows()

# 保存图片
cv2.imwrite("MousePaint01.png",  img)