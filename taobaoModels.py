# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: taobaoModels.py
@time: 2017/11/12 11:07
"""
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import pandas
import os


def getGoods(html):
    # 获取名字
    name = BeautifulSoup(html, 'html.parser').select('.name')
    names = []
    for i in name:
        names.append(re.compile('<span class="name">(.*?)</span>').search(str(i)).group(1))

    # 获取城市
    city = BeautifulSoup(html, 'html.parser').select('.city')
    citys = []
    for i in city:
        citys.append(re.compile('<span class="city">(.*?)</span>').findall(str(i)))

    # 创建目录
    for i in names:
        i = 'E:\\taobaoModels\%s' % i
        path = i.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        os.chdir(path)

    # 保存图片
    img = BeautifulSoup(html, 'html.parser').select('.img')
    imgs = []

    for i in img:
        imgs.append(re.compile(r'="//gtd(.*?)jpg"').findall(str(i)))

    imgs_cur = []
    for i in range(len(imgs)):
        h = str(imgs[i])
        h = re.sub(r'\[\'|\'\]', '', h)
        h = 'http://gtd' + h + 'jpg'
        imgs_cur.append(h)

    for i in range(len(names)):
        try:
            data_img = requests.get(imgs_cur[i])
            f1 = open('E:\\taobaoModels\%s\靓照.jpg' % names[i], 'wb')
            f1.write(data_img.content)
            f1.close()
        except:
            f1.close()
            continue

    # 保存资料
    for i in range(len(names)):
        data_doc = '模特昵称：' + str(names[i]) + '  ' + '所在城市：' + str(citys[i])
        f2 = open('E:\\taobaoModels\%s\资料.txt' % names[i], 'w')
        f2.write(data_doc)
        f2.close()

    # pandas 展示
    L5 = []
    for i in range(len(names)):
        L4 = [names[i], citys[i], imgs_cur[i]]
        L5.append(L4)

    df = pandas.DataFrame(L5)
    df.columns = ['模特昵称', '所在城市', '照片链接']
    print(df)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://mm.taobao.com/search_tstar_model.htm?spm=5679.126488.640745.2.19accbafwIHQLI")
    time.sleep(3)
    for i in range(1, 100):
        driver.find_element_by_css_selector('.page-skip').clear()
        driver.find_element_by_css_selector('.page-skip').send_keys(i)
        driver.find_element_by_css_selector('.page-btn').click()
        time.sleep(5)
        html = driver.page_source
        getGoods(html)
    driver.close()