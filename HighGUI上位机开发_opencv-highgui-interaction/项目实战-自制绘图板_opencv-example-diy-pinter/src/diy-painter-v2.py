'''
 鼠标按下绘制线条

'''
import cv2  
import numpy as np  
  
# 鼠标回调函数  
# x, y 都是相对于窗口内的图像的位置
isMouseLBDown = False

def draw_circle(event,x,y,flags,param): 
    # 判断事件是否为 Left Button Double Clicck 
    print(event)
    global isMouseLBDown

    if event == cv2.EVENT_LBUTTONDOWN:
        # 检测到鼠标左键按下
        print("mouse down")
        isMouseLBDown = True
        cv2.circle(img,(x,y),5,(255,0,0),-1) 
    elif event == cv2.EVENT_LBUTTONUP:
        # 检测到鼠标左键抬起
        isMouseLBDown = False
        print("mouse up")
    elif event == cv2.EVENT_MOUSEMOVE:
        if isMouseLBDown:
            print("drawing")
            cv2.circle(img,(x,y),5,(255,0,0),-1)

# 创建一个黑色图像，并绑定窗口和鼠标回调函数  
img = np.zeros((512,512,3), np.uint8)  
cv2.namedWindow('image')
# 设置鼠标事件回调
cv2.setMouseCallback('image',draw_circle)  
  
while(True):  
    cv2.imshow('image',img)  
    if cv2.waitKey(1) == ord('q'):  
        break  
cv2.destroyAllWindows()

cv2.imwrite("MousePaint02.png",  img)