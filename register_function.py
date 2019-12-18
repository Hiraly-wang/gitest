# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 13:49
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_function.py
# @Software: PyCharm


import random
import string
import time

from PIL import Image
from selenium import webdriver

import lianzhong_api
from find_element import FindElement


class Register():

    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)
    '''
        初始化driver打开url
    '''

    def get_driver(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 0:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 获取页面元素
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入用户信息
    def input_user_info(self, key, data):
        print('输入用户信息' + key)
        self.get_user_element(key).send_keys(data)

    '''
       用户名随机产生 
    '''

    def random_info(self):
        username = ''.join(random.sample(string.ascii_letters + string.digits, 6))
        return username

    '''
        验证码处理
    '''

    def find_code(self, file_name):
        # 获取注册页面截屏保存图片
        self.driver.save_screenshot(file_name)
        # 获取验证码图片原点坐标
        code_element = self.get_user_element('code_img')
        # 原点坐标（左上角）
        # print(code_element.location)
        x0 = code_element.location['x']
        y0 = code_element.location['y']
        x1 = code_element.size['width'] + x0
        y1 = code_element.size['height'] + y0
        im = Image.open(file_name)
        # 裁剪验证码图片
        img = im.crop((x0, y0, x1, y1))
        # 保存图片
        img.save(file_name)
        return file_name

    '''
        联众API识别验证码
    '''

    def verify_code(self, api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type, tools_token):

        code = lianzhong_api.main(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type,
                                  tools_token)
        print(code)
        return code

    def main(self):
        username = self.random_info()
        user_email = username + '@163.com'
        file_name = './code.png'
        self.find_code(file_name)
        # code_text = self.verify_code('warflor',
        #                              'lianzhong0608.',
        #                              './code.png',
        #                              'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload',
        #                              '1',
        #                              '8',
        #                              '1013',
        #                              '')
        self.input_user_info('register_email', user_email)
        self.input_user_info('username', username)
        self.input_user_info('password', '111111')
        self.input_user_info('code_text', '123')
        self.get_user_element('register_btn').click()
        # 验证码输入错误，保存截图
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print('注册成功！')
        else:
            print('注册失败')
            self.driver.save_screenshot('./code_erorr_screenshot.png')
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    register_url = 'http://www.5itest.cn/register'
    for i in range(3):
        register = Register(register_url, i)
        register.main()
