# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 14:55
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : ddt_test.py
# @Software: PyCharm

import time
import unittest

import ddt
from selenium import webdriver

from page_object_model.register_business import RegisterBusiness


@ddt.ddt
class DdtRegisterTest(unittest.TestCase):

    def setUp(self):
        print('开始执行测试')
        self.register_url = 'http://www.5itest.cn/register'
        self.driver = webdriver.Chrome()
        self.driver.get(self.register_url)
        self.rb = RegisterBusiness(self.driver)
        self.filename = './image/test.png'

    def tearDown(self):
        time.sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = './report/' + case_name + 'screen_shot.png'
                self.driver.save_screenshot(file_path)
        print('执行结束')
        self.driver.close()

    @ddt.data(
        ['123', 'shishigou', 'password', 'code', 'register_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'shishigou', 'password', 'code', 'register_email_error', '请输入有效的电子邮件地址'],
        ['123@qq.com', 'shishigou', 'password', 'code', 'register_email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack
    def test_register(self, email, username, password, code, test_element, tip_msg):
        email_error = self.rb.register_func(email, username, password, code, test_element, tip_msg)
        return self.assertTrue(email_error, '测试失败')


if __name__ == '__main__':
    unittest.main()
