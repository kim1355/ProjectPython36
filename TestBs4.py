# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: TestBs4.py
@time: 2017/10/19 14:32
"""
from bs4 import BeautifulSoup
import requests

html = requests.get('https://wenku.baidu.com/view/30118dab846a561252d380eb6294dd88d0d23d29.html').text
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('div', id="doc"))
