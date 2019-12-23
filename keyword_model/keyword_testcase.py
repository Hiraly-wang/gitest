# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 17:33
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : keyword_testcase.py
# @Software: PyCharm

import xlrd
from selenium import webdriver
from util.read_excel import ReadExcel


class Run(object):

    def run_main(self):
        handle_excel = ReadExcel('config/test_case.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_cell(i, 3)
                if is_run == 'yes':
                    method = handle_excel.get_cell(i, 4)
                    input_data = handle_excel.get_cell(i, 5)
                    handle_element = handle_excel.get_cell(i, 6)
                    if input_data :


