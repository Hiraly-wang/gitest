# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 23:22
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : discern_captcha.py
# @Software: PyCharm

from PIL import Image
from selenium import webdriver
from api import lianzhong_api

"""验证码识别"""

class VerifyCode(object):

    def __int__(self, driver):
        self.driver = driver

    def find_code(self, file_name):
        # 获取注册页面截屏保存图片
        self.driver.save_screenshot(file_name)
        # 获取验证码图片原点坐标
        code_element = self.driver.find_element_by_id('getcode_num')
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
        return lianzhong_api.api_verify_code(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max,
                                         yzm_type, tools_token)
