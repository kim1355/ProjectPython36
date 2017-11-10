# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: testSpider.py
@time: 2017/11/10 21:51
"""

import re
import requests
import pandas
import json
from bs4 import BeautifulSoup

res = requests.get('http://www.meituan.com/api/v1/divisions?mtt=1.help%2Fapi.0.0.j9u06211')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'xml')
jdata = soup.select('division')
name = re.compile(r'<name>(.*?)</name>').findall(str(jdata))
latitude = re.compile(r'<latitude>(.*?)</latitude>').findall(str(jdata))
longitude = re.compile(r'<longitude>(.*?)</longitude>').findall(str(jdata))

L5 = []
for i in range(len(name)):
    L4 = []
    L4.append(name[i])
    L4.append(latitude[i])
    L4.append(longitude[i])
    L5.append(L4)

df = pandas.DataFrame(L5)
df.columns = ['城市', '纬度', '经度']
# print(df)
df.to_excel('E://美团.xlsx')