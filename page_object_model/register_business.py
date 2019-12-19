# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:51
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_business.py
# @Software: PyCharm

import time
from selenium import webdriver
from page_object_model.register_handle import RegisterHandler
"""业务层，也就是我们要做些什么，做事的逻辑是什么？对于自动化测试来说，就是自动化的测试场景，也就是我们的测试点逻辑"""


class RegisterBusiness(object):

    def __init__(self, driver):
        self.rh = RegisterHandler(driver)

    # 输入用户信息
    def input_userinfo(self, email, username, password, code_text):
        self.rh.input_email(email)
        self.rh.input_username(username)
        self.rh.input_password(password)
        self.rh.input_code_text(code_text)
        self.rh.click_register_btn()

    # 判断是否注册成功
    def success_or_fail(self):
        if self.rh.get_register_btn_text() is None:
            print('注册成功')
            return True
        else:
            print('注册失败')
            return False


if __name__ == '__main__':
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    rb.input_userinfo('892@163.com', 'tom234', 'pass5435', '1241')
    time.sleep(3)
    driver.close()




