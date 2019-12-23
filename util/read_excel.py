# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 15:46
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : read_excel.py
# @Software: PyCharm
import xlrd
from xlutils.copy import copy


class ReadExcel(object):

    def __init__(self, excel_path=None, index=None):
        # print(os.getcwd())
        if excel_path is None:
            self.excel_path = 'config/test_case.xls'
            self.index = 0
        else:
            self.excel_path = excel_path
            self.index = index
        # 打开excel文件，获取数据列表
        self.data = xlrd.open_workbook(self.excel_path)
        # 读取第一个sheet的数据
        self.sheet = self.data.sheets()[0]

    # 获取表格的行数
    def get_lines(self):
        rows = self.sheet.nrows
        if rows >= 1:
            return rows
        else:
            return None

    # 获取每行的数据
    def get_data(self):
        result = []
        rows = self.get_lines()
        # 判断行数是否为空
        if rows is not None:
            for i in range(rows):
                # 获取每行的数据
                col = self.sheet.row_values(i)
                result.append(col)
            return result
        return None

    # 获取单元格的值
    def get_cell(self, row, col):
        if self.get_lines() > row:
            data = self.sheet.cell(row, col).value
            return data
        return None

    # 写入数据,表格是从0行0列开始计算的
    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)
        write_data.get_sheet(self.index).write(row, col, value)
        # write_data.save('config/test_case.xls')
        write_data.save(self.excel_path)


if __name__ == '__main__':
    re = ReadExcel()
    print(re.get_data())
    print(re.get_lines())
    print(re.get_cell(1, 1))
    re.write_data(4, 5, '通过外部添加')
