# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 17:33
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : keyword_testcase.py
# @Software: PyCharm

from keyword_model.keyword_actionMethod import ActionMethod
from util.read_excel import ReadExcel


class Run(object):

    def run_main(self):
        self.action_method = ActionMethod()
        # print(self.action_method)
        handle_excel = ReadExcel('config/test_case.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_cell(i, 3)
                # r如果方法执行为yes
                if is_run == 'yes':
                    method = handle_excel.get_cell(i, 4)
                    input_data = handle_excel.get_cell(i, 5)
                    handle_element = handle_excel.get_cell(i, 6)
                    self.run_method(method, input_data, handle_element)

    # method 方法名
    def run_method(self, method, input_data, handle_element):
        print(input_data, end='---------->' + handle_element)
        # 反射
        method_value = getattr(self.action_method, method)
        # 如果有输入值
        if input_data:
            method_value(input_data, handle_element)
        # 如果没有输入值
        elif input_data == '' and handle_element != '':
            method_value(handle_element)
        else:
            method_value()


if __name__ == '__main__':
    run = Run()
    run.run_main()
