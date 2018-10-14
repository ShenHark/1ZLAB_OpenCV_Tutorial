# 仿射变换简介

## 概要
本文讲解了什么是仿射变换, 给出了仿射变换的公式.

**keywords** 放射变换 affine-transform 公式推导


## 什么是放射变换
图像上的仿射变换, 其实就是图片中的一个像素点，通过某种变换，移动到另外一个地方。

从数学上来讲， 就是一个向量空间进行一次线形变换并加上平移向量， 从而变换到另外一个向量空间的过程。

向量空间m : 

$m = (x, y)$

向量空间n :

$n  = (x', y’)$

向量空间从m到n的变换   $n = A * m + b$
整理得到:

$$ x' = A_{00} *x + A_{01}*y + b_0$$

$$ y' = A_{10} *x + A_{11}*y + b_1$$



将$A$跟$b$ 组合在一起就组成了仿射矩阵 $M$。 它的维度是$2*3$
$$
M = {
\left[ \begin{array}{ccc}
A_{00} , A_{01}, b_0\\
A_{10}, A_{11}, b_1\\
\end{array} 
\right ]}
$$




使用不同的矩阵$$M$$就获得了不同的2D仿射变换效果。

**在opencv中，实现2D仿射变换， 需要借助`warpAffine` 函数。**

```
cv2.warpAffine(image, M, (image.shape[1], image.shape[0])
```



接下来，阿凯带你结合具体的2D仿射变换，分析其变换矩阵。


## 参考文献

[Geometric Transformations of Images](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html)

[【OpenCV】图像几何变换：旋转，缩放，斜切](http://blog.csdn.net/xiaowei_cqu/article/details/7616044)

[Resampling Methods](https://seadas.gsfc.nasa.gov/help/general/ResamplingMethods.html)

[旋转变换（一）旋转矩阵](http://blog.csdn.net/csxiaoshui/article/details/65446125)