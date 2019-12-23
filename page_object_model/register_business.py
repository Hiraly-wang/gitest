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
    def input_user_info(self, email, username, password, filename):
        self.rh.input_email(email)
        self.rh.input_username(username)
        self.rh.input_password(password)
        self.rh.input_code_text(filename)
        self.rh.click_register_btn()

    # 判断是否注册成功
    def success_or_fail(self):
        if self.rh.get_register_btn_text() is None:
            print('注册成功')
            return True
        else:
            print('注册失败')
            return False

    # 邮箱格式错误
    def email_format_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_email_error', '请输入有效的电子邮件地址') is not None:
            print('邮箱格式错误')
            return True
        else:
            return False

    # 没有输入邮箱错误
    def email_null_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_email_error', '请输入邮箱') is not None:
            print('没有输入邮箱')
            return True
        else:
            return False

    # 用户名格式错误
    def username_format_error(self, email, username, password, code_text):
        self.input_user_info(email, username, password, code_text)
        if self.rh.get_error_info('register_username_error', '字符长度必须大于等于4，一个中文字算2个字符') is not None:
            print('用户名格式错误')
            return True
        else:
            return False

    #  没有输入用户名错误
    def username_null_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_username_error', '字符长度必须大于等于4，一个中文字算2个字符') is not None:
            print('没有输入用户名错误')
            return True
        else:
            return False

    # 用户名重复错误
    def username_repeat_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_username_error', '名称已存在!') is not None:
            print('用户名重复错误')
            return True
        else:
            return False

    # 密码过长错误
    def password_len_big_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_password_error', '最多只能输入 20 个字符') is not None:
            print('密码过长错误')
            return True
        else:
            return False

    # 密码过短错误
    def password_len_tiny_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_password_error', '最多只能输入 20 个字符') is not None:
            print('密码过短错误')
            return True
        else:
            return False

    # 没有输入密码错误
    def password_null_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('register_password_error', '请输入密码') is not None:
            print('没有输入密码错误')
            return True
        else:
            return False

    # 验证码错误
    def code_null_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('captcha_code_error', '请输入验证码') is not None:
            print('没有输入验证码错误')
            return True
        else:
            return False

    # 验证码输入错误
    def code_value_error(self, email, username, password, filename):
        self.input_user_info(email, username, password, filename)
        if self.rh.get_error_info('captcha_code_error', '验证码错误') is not None:
            print('验证码输入错误')
            return True
        else:
            return False

    # 整个注册流程，test_element:提示错误信息的元素，tip_msg:错误提示信息
    def register_func(self, email, username, password, code, test_element, tip_msg):
        self.input_user_info(email, username, password, code)
        if self.rh.get_error_info(test_element,tip_msg) is not None:
            return True
        else:
            return False


if __name__ == '__main__':
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    rb.input_user_info('892@163.com', 'tom234', 'pass5435', '')
    rb.success_or_fail()
    time.sleep(5)
    driver.close()
