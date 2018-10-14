
# 窗口展示


## 概要
讲解了如何显示/更新窗口里的图像

**keywords** highgui imshow

## imshow的API讲解

在HighGUI展示图像， 需要使用到 `imshow` 函数， 第一个参数， 我们传入窗口的名称，第二个参数就是 `Image` 对象。

```python
# 展示图像
cv2.imshow('image',img)
```

如果`image`这个窗口之前并没有被声明， 那么同时会先创建一个名字叫做`image`的窗口， 然后再更新窗口里面的图像。


请注意，你执行完这个`cv2.imshow()`之后，窗口会一闪而过，这个时候你就需要使用到`cv2.waitKey`这个函数啦，后文有讲。