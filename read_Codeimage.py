# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 17:44
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : read_Codeimage.py
# @Software: PyCharm
import pytesseract
import tesserocr
from PIL import Image
im=Image.open('E:/Other Document/Py_Project/Python3_proj/5itest/imooc1.png')
# 将图片化为灰度图片
image = im.convert('L')
# 指定图片二值化的阈值
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
# image.show()
# print(image.mode)
# 将图片进行二值化处理
# iamge = image.convert('1')
result = tesserocr.image_to_text(image)
print(result)