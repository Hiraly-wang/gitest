# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 15:06
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : find_element.py
# @Software: PyCharm

from util.read_ini import ReadIni

'''
    定位元素
'''


class FindElement():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.getValue(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'className':
                return self.driver.find_element_by_className(value)
            else:
                return self.driver.find_element_by_name(value)
        except:
            print('找不到元素', by + '>' + value)
            return None
