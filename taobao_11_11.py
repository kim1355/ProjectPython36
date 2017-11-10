# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: taobao_11_11.py
@time: 2017/11/9 23:58
"""
import requests
from bs4 import BeautifulSoup
import json
import pandas

# 获取网页内容
try:
    res = requests.get('https://pages.tmall.com/wow/act/18132/industry-100719')
    soup = BeautifulSoup(res.text, 'html.parser')
except:
    print('打开网页失败！')

''' 只取一项 '''
result = soup.select('.J_dynamic_data')[1].text.strip()
jd = json.loads(result)
df2 = pandas.DataFrame(jd['items'])
# print(df)

''' 遍历获取 '''
j_ary = []
for jdata in soup.select('.J_dynamic_data'):  # 获取界面class = J_dynamic_data
    if jdata.text.strip() != '':
        jd = json.loads(jdata.text.strip())  # 转换为JSON 并去空格
        if isinstance(jd, dict) and jd.get('items'):  # 判断为字典时 且 itmes不为空
            df = pandas.DataFrame(jd['items'])
            j_ary.append(df)
        if isinstance(jd, list):  # 判断为list时
            df = pandas.DataFrame(jd)
            j_ary.append(df)
jdf = pandas.concat(j_ary)  # 集合数据
# print(jdf.columns)          # 显示列名
# print(jdf[['itemTitle', 'itemUrl', 'itemTagPrice']])    # 显示指定列
# jdf[['itemTitle', 'itemUrl', 'itemTagPrice']].to_excel('E:\\淘宝手机.xlsx')  # 保存为excel

''' Excel保存方式 '''
df1 = jdf[['itemTitle', 'itemUrl', 'itemTagPrice']]  # 选指定列
writer = pandas.ExcelWriter('E:\\淘宝手机.xlsx')
df1.to_excel(writer, 'Sheet1')
df2.to_excel(writer, 'Sheet2')
writer.save()
