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
soup = BeautifulSoup(res.text,'xml')
jdata = soup.select('division')
name = re.compile(r'<name>(.*?)</name>').findall(str(jdata))
latitude = re.compile(r'<latitude>(.*?)</latitude>').findall(str(jdata))
longitude = re.compile(r'<longitude>(.*?)</longitude>').findall(str(jdata))


df1 = pandas.DataFrame(name)
df2 = pandas.DataFrame(latitude)
df3 = pandas.DataFrame(longitude)

df1.columns = ['城市']
df2.columns = ['纬度']
df3.columns = ['经度']

# frame = [df1, df2, df3]
# df4 = pandas.concat(frame)
df4 = df1.append([df2, df3])
df4.to_excel('E://aa.xlsx')

