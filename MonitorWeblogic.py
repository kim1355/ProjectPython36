# -*- coding:utf-8 -*-
"""
@version: python3.6
@author: Administrator
@license: iTech Licence 
@contact: konp88@gmail.com
@site: 
@software: PyCharm
@file: MonitorWeblogic.py
@time: 2017/10/13 14:55
"""
import time
import os
import psutil
import logging
import logging.handlers

# configure LogFile
LOG_FILE = 'MonitorWeblogic.log'

# 实例化handler,文件大小10MB，超出则创建新的文件
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10240 * 1024, backupCount=5, encoding="utf-8")
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('tst_logger')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.debug('first debug message')


# configure variables(cpu memory disk)
cpu_info = {'user': 0, 'system': 0, 'idle': 0, 'percent': 0}
memory_info = {'total': 0, 'available': 0, 'percent': 0, 'used': 0, 'free': 0}
disk_id = []
disk_total = []
disk_used = []
disk_free = []
disk_percent = []


# get cpu information
def get_cpu_info():
    cpu_times = psutil.cpu_times()
    cpu_info['user'] = cpu_times.user
    cpu_info['system'] = cpu_times.system
    cpu_info['idle'] = cpu_times.idle
    cpu_info['percent'] = psutil.cpu_percent(interval=2)


# get memory information
def get_memory_info():
    mem_info = psutil.virtual_memory()
    memory_info['total'] = mem_info.total
    memory_info['available'] = mem_info.available
    memory_info['percent'] = mem_info.percent
    memory_info['used'] = mem_info.used
    memory_info['free'] = mem_info.free


def get_disk_info():
    for id in psutil.disk_partitions():
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        s = disk_name[0]
        disk_id.append(s)
        disk_info = psutil.disk_usage(id.device)
        disk_total.append(disk_info.total)
        disk_used.append(disk_info.used)
        disk_free.append(disk_info.free)
        disk_percent.append(disk_info.percent)


# restart weblogic server
def restart_web():
    # stop server
    logger.info(u'开始关闭weblogic服务')
    os.system('taskkill /f /t /im java.exe')
    time.sleep(3)
    # start server
    logger.info(u'开始启动weblogic服务')
    os.system('start C:\\Oracle\\Middleware\\user_projects\\domains\\dgts_domain\\startWebLogic.cmd')


if __name__ == '__main__':
    while True:
        get_cpu_info()
        cpu_status = cpu_info['percent']
        logger.info('cpu usage is:%s%%' % cpu_status)

        get_memory_info()
        mem_status = memory_info['used'] / 1024 / 1024
        logger.info('memory usage is:%s MB' % mem_status)

        get_disk_info()
#        for i in range(len(disk_id)):
        logger.info('%s   disk usage is:%s%%' % (disk_id[0], 100 - disk_percent[0]))
        logger.info('%s   disk usage is:%s%%' % (disk_id[1], 100 - disk_percent[1]))

        # if mem_status > 5120:
        #     restart_web()
        # else:
        #     pass
        time.sleep(15)
