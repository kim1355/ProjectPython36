# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: cli_chat.py
@time: 2017/11/13 12:59
"""
import socket
import time
from threading import Thread
import sys

C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C.connect(('127.0.0.1', 12345))  # 需要IP和port 组成元组
print('--911进入聊天室--')

def rcv_data():
    while True:
        r_data = C.recv(1024).decode('utf8')  # decode 将 bytes 转为 str
        if r_data == 'exit':
            sys.exit()
        print('Server> ' + r_data)
        print('Server> ' + '--%s--' % str(time.ctime(time.time())))

t = Thread(target=rcv_data, name='rcv_threading', args=())
t.start()

while True:
    s_data = input('Client> ').encode('utf8')  # encode 将 str 转为 bytes
    C.send(s_data)
    if s_data == 'exit':
        sys.exit()
C.close()
