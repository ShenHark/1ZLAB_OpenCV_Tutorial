
# 通过pip安装OpenCV


## 概要
本文介绍了如何通过pip安装OpenCV.
注: 本篇教程适用于全平台(Windows, Mac, Linux)

**keywords** opencv pip python-opencv

## 安装PIP3
Ubuntu16.04自带的默认Python版本是python3.5, 需要安装`pip3` 作为python的包管理工具. 

```bash
sudo apt-get install python3-pip
```
## Python科学计算工具包

做科学计算需要安装下面的一些工具包

```bash
sudo pip3 install jupyter ipython numpy scipy matplotlib
```



## 安装OpenCV



非官方的OpenCV预编译的包.
同时安装opencv的main还有contrib部分.

```bash
pip install opencv-contrib-python
```

详情见文档:
[opencv-python 3.4.3.18](https://pypi.org/project/opencv-python/)