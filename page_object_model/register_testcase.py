# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 15:22
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_testcase.py
# @Software: PyCharm

import HTMLTestRunner
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

    # 测试邮箱输入错误
    def test_email_error(self):
        register_email_error = self.rb.email_format_error('123asdcom', 'name123', '88888', self.filename)
        self.assertTrue(register_email_error, '用例执行失败，邮箱正确')

    # 测试用户名输入错误
    def test_username_error(self):
        register_username_error = self.rb.username_format_error('123asdcom@qq.com', 'n', '88888', self.filename)
        self.assertTrue(register_username_error, '用例执行失败，用户名正确')

    # 测试密码格式错误
    def test_password_error(self):
        register_password_error = self.rb.password_len_tiny_error('123asdcom@qq.com', 'nfaisfibaldi23', '88',
                                                                  self.filename)
        self.assertTrue(register_password_error, '用例执行失败，密码正确')

    # 测试验证码输入为空
    def test_code_null_error(self):
        register_code_null_error = self.rb.code_null_error('123asdcom@qq.com', 'nfaisfibaldi23', '812148', '')
        self.assertTrue(register_code_null_error, '用例执行失败，验证码已输入')

    # 测试验证码输入错误
    def test_code_text_error(self):
        register_code_text_error = self.rb.code_null_error('123asdcom@qq.com', 'nfaisfibaldi23', '812148', '1234')
        self.assertTrue(register_code_text_error, '用例执行失败，验证码输入正确')


if __name__ == '__main__':
    # os.getcwd()+'/report/'+'result.html'
    # unittest.main()
    # 增加测试套件
    suite = unittest.TestSuite()
    # 将测试用例加入测试套件
    suite.addTest(RegisterTestCase('test_code_text_error'))
    # 增加测试报告
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='5itest 注册页面测试报告',
                                           description='运行环境：selenium+unittest')
    # 运行测试组件
    runner.run(suite)
    fp.close()
