# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 14:37
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : data_test.py
# @Software: PyCharm

import unittest

import ddt


@ddt.ddt
class DataTest(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    @ddt.data(
        [1, 2],
        [3, 4],
        [5, 6]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a + b)


if __name__ == '__main__':
    unittest.main()
