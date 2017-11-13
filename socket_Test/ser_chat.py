# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: ser_chat.py
@time: 2017/11/13 12:59
"""

import socket
import time
from threading import Thread

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind(('127.0.0.1', 12345))  # 需要IP和port 组成元组
S.listen(5)
print('--聊天室服务端--')

connect, address = S.accept()

def rcv_data():
    while True:
        r_data = connect.recv(1024).decode('utf8')      # decode 将 bytes 转为 str
        if r_data == 'exit':
            break
        print('Client[' + str(address) + ']> ' + r_data)
        print('Client[' + str(address) + ']> ' + '--%s--' % str(time.ctime(time.time())))

t = Thread(target=rcv_data, name='Thread-rcv', args=())
t.start()

while True:
    s_data = input('Server> ').encode('utf8')     # encode 将 str 转为 bytes
    connect.send(s_data)
    if s_data == 'exit':
        break
S.close()