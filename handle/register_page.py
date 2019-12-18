# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 23:03
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_page.py
# @Software: PyCharm
import time
from base.find_element import FindElement
from selenium import webdriver

"""
     此页面主要是查找注册页面中正常的元素和异常的元素（错误的提示信息）
"""


class RegisterPage(object):

    def __init__(self, driver):
        self.fe = FindElement(driver)

    # 查找注册邮箱
    def get_register_email(self):
        return self.fe.get_element('register_email')

    # 查找用户名
    def input_username(self):
        return self.fe.get_element('username')

    # 查找密码
    def input_password(self):
        return self.fe.get_element('password')

    # 查找验证码输入框
    def input_code_text(self):
        return self.fe.get_element('code_text')

    # 识别验证码图片
    def verify_code(self):
        return self.fe.get_element('code_img')


if __name__ == '__main__':
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rp = RegisterPage(driver)
    time.sleep(2)
    driver.close()
