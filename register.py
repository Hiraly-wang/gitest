# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 14:12
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register.py
# @Software: PyCharm

import random
import string
from PIL import Image
from selenium import webdriver
import lianzhong_api

driver = webdriver.Chrome()
'''
    初始化
'''


def register_init(register_url):
    driver.get(url=register_url)
    # 最大化窗口
    driver.maximize_window()


'''
    定位元素
'''


def find_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


'''
   用户名随机产生 
'''


def random_info():
    username = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return username


'''
    验证码处理
'''


def find_code(file_name):
    # 获取注册页面截屏保存图片
    driver.save_screenshot(file_name)
    # 获取验证码图片原点坐标
    code_element = driver.find_element_by_id('getcode_num')
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


def verify_code(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type, tools_token):
    return lianzhong_api.main(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type,
                              tools_token)


def main():
    register_url = 'http://www.5itest.cn/register'
    register_init(register_url)
    random_user = random_info()
    register_email = find_element('//*[@id="register_email"]')
    register_email.send_keys(random_user + '@163.com')
    username = find_element('//*[@id="register_nickname"]')
    username.send_keys(random_user)
    password = find_element('//*[@id="register_password"]')
    password.send_keys('111111')
    find_code('./code.png')
    code = verify_code(
        'warflor',
        'lianzhong0608.',
        './code.png',
        "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload",
        '1',
        '8',
        '1013',
        '')
    find_element('//*[@id="captcha_code"]').send_keys(code)
if __name__ == '__main__':
    main()
