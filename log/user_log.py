# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 21:19
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : user_log.py
# @Software: PyCharm

import logging
import time

# 获取当前时间的时间戳
now_time = time.time()
# 格式化时间
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(now_time))
print(now)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 控制台输入日志
# console = logging.StreamHandler()
# logger.addHandler(console)
# 关闭console
# console.close()
# logger.removeHandler(console)

# 文件输入日志
file_handle = logging.FileHandler('../log/logs/'+now+'.log')
# 格式化输出
logging.Formatter('%(asctime)s')
logger.addHandler(file_handle)
# 日志打印内容
logger.debug('test')
file_handle.close()
logger.removeHandler(file_handle)
