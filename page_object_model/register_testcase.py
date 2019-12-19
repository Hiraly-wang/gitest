# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 15:22
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_testcase.py
# @Software: PyCharm

import time
import unittest

from selenium import webdriver

from page_object_model.register_business import RegisterBusiness


class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        print('开始执行测试')
        self.register_url = 'http://www.5itest.cn/register'
        self.driver = webdriver.Chrome()
        self.driver.get(self.register_url)
        self.rb = RegisterBusiness(self.driver)

    def tearDown(self):
        print('执行结束')
        time.sleep(4)
        self.driver.close()

    # 测试邮箱输入错误
    def test_email_error(self):
        register_email_error = self.rb.email_format_error('123asdcom', 'name123', '88888', 'a12c')
        self.assertTrue(register_email_error, '用例执行失败，邮箱正确')

    # 测试用户名输入错误
    def test_username_error(self):
        register_username_error = self.rb.username_format_error('123asdcom@qq.com', 'n', '88888', 'a12c')
        self.assertTrue(register_username_error, '用例执行失败，用户名正确')

    # 测试密码格式错误
    def test_password_error(self):
        register_password_error = self.rb.password_len_tiny_error('123asdcom@qq.com', 'nfaisfibaldi23', '88', 'a12c')
        self.assertTrue(register_password_error, '用例执行失败，密码正确')

    # 测试验证码输入错误
    def test_code_error(self):
        self.rb.code_null_error('123asdcom@qq.com', 'nfaisfibaldi23', '812148', '')
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
