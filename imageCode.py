# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: imageCode.py
@time: 2017/11/2 10:17
"""
from selenium import webdriver
import os
import pytesser3
import sys, time
from PIL import Image, ImageEnhance

options = webdriver.ChromeOptions()
'''模拟手机浏览器'''
# options.add_argument(
#     'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.baidu.com')
try:
    elem_user = driver.find_element_by_name('id')
    elem_psw = driver.find_element_by_name('password')
    elem_code = driver.find_element_by_name('checkcode')
except:
    pass
driver.get_screenshot_as_file("E:\\test.jpg")
time.sleep(5)
element = driver.find_element_by_id('qrcode')
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']
print(left, right, top, bottom)
im = Image.open('E:\\test.jpg')
box = (left, top, right, bottom)  # 设置要裁剪的区域
region = im.crop(box)  # 此时，region是一个新的图像对象
# region.show()                # 显示图像
driver.close()
region.save('E:\\region.jpg')

'''验证码识别'''
# img = Image.open('E:\\region.jpg')
# vcode = pytesser3.image_to_string(img)
# print(vcode)
