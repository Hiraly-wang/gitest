# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 13:58
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : read_ini.py
# @Software: PyCharm
import configparser


class ReadIni(object):
    """
        初始化类，设置默认值
    """

    def __init__(self, filename=None, node=None):
        if filename == None:
            filename = r'F:\Python_project\gitest\config\LocalElement.ini'
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.Load_ini(filename)

    '''
        加载配置文件
    '''

    def Load_ini(self, filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    '''
        获取配置文件内容
    '''

    def getValue(self, key):
        return self.cf.get(self.node, key)


if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.getValue('username'))
