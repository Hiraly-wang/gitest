# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 18:11
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : keyword_actionMethod.py
# @Software: PyCharm
import time

from selenium import webdriver

from base.find_element import FindElement


class ActionMethod(object):

    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        # 获取元素
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def input_element(self, ket, value):
        element = self.get_element(ket)
        element.send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待
    def sleep_time(self):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()
