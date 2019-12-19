# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 23:03
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_page.py
# @Software: PyCharm
import time

from selenium import webdriver

from base.find_element import FindElement

"""
     此页面主要是查找注册页面中正常的元素和异常的元素（错误的提示信息）
"""


class RegisterPage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.fe = FindElement(driver)

    # 查找注册邮箱
    def get_register_email(self):
        return self.fe.get_element('register_email')

    # 查找用户名
    def get_username(self):
        return self.fe.get_element('username')

    # 查找密码
    def get_password(self):
        return self.fe.get_element('password')

    # 识别验证码图片
    def verify_code(self):
        return self.fe.get_element('code_img')

    # 查找验证码输入框
    def get_code_text(self):
        return self.fe.get_element('code_text')

    # 查找注册按钮
    def get_register_btn(self):
        return self.fe.get_element('register_btn')

    def email_error(self):
        return self.fe.get_element()


if __name__ == '__main__':
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rp = RegisterPage(driver)
    rp.get_register_email()
    print('找到email')
    rp.get_username()
    print('找到username')
    rp.get_code_text()
    time.sleep(2)
    driver.close()
