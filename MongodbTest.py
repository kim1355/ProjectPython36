# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: MongodbTest.py
@time: 2017/11/11 19:42
"""
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test

collection = db.students
results = collection.find_one()
print(results['name'])
print("pymongo")

