# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 17:33
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : test_case.py
# @Software: PyCharm

from keyword_model.keyword_actionMethod import ActionMethod
from util.read_excel import ReadExcel


class Run(object):

    def run_main(self):
        self.action_method = ActionMethod()
        # print(self.action_method)
        handle_excel = ReadExcel('../config/test_case.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_cell(i, 3)
                # r如果方法执行为yes
                if is_run == 'yes':
                    method = handle_excel.get_cell(i, 4)
                    input_data = handle_excel.get_cell(i, 5)
                    handle_element = handle_excel.get_cell(i, 6)
                    expect_result_method = handle_excel.get_cell(i, 7)
                    expect_result = handle_excel.get_cell(i, 8)
                    self.run_method(method, input_data, handle_element)
                    # 预期结果不等于空
                    if expect_result != '':
                        except_result_value = self.get_expect_result(expect_result)
                        # 获取页面title
                        if except_result_value[0] == 'text':
                            result = self.run_method(expect_result_method)
                            if except_result_value[1] in result:
                                handle_excel.write_value(i, 9, 'pass')
                            else:
                                handle_excel.write_value(i, 9, 'fail')
                        elif except_result_value[0] == 'element':
                            result = self.run_method(expect_result_method, except_result_value[1])
                            if result:
                                handle_excel.write_value(i, 9, 'pass')
                            else:
                                handle_excel.write_value(i, 9, 'fail')
                        else:
                            print('除了text和element之外的')
                    else:
                        print('预期结果为空')

    # 获取预期结果
    def get_expect_result(self, data):
        # 以‘=’拆分为列表
        return data.split('=')

    # method 方法名
    def run_method(self, method, input_data='', handle_element=''):
        # print(input_data, end='---------->' + handle_element)
        # 反射
        method_value = getattr(self.action_method, method)
        # 如果有输入值和操作元素
        if input_data != '' and handle_element != '':
            result = method_value(input_data, handle_element)
        # 没有输入值，只有操作元素
        elif input_data == '' and handle_element != '':
            result = method_value(handle_element)
        # 有输入值，没有操作元素
        elif input_data != '' and handle_element == '':
            result = method_value(input_data)
        # 如果没有输入值和操作元素
        else:
            result = method_value()
        return result


if __name__ == '__main__':
    run = Run()
    run.run_main()
