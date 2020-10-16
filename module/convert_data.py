#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   convert_data.py
@Time    :   2020/10/16 15:38:15
@Author  :   EvilRecluse
@Contact :   evilrecluse@sxkid.com
@Desc    :   None
'''

# here put the import lib
from module.utils.excel_helper import PyExcel

def load_data_from_excel():
    '''
    從Excel獲取數據
    '''
    a = PyExcel.get_data_simple(
        file_path='resources\副本信源 （知乎已确认）(1).xlsx',
        sheet_name='Sheet1',
        data_format={'name':3, 'home_page_url':6},
        rowlimit=[1,'max'])
    print(a)