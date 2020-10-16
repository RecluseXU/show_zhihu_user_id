#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   zhihu.py
@Time    :   2020/10/16 15:36:07
@Author  :   EvilRecluse
@Contact :   evilrecluse@sxkid.com
@Desc    :   None
'''

# here put the import lib
import requests
import logging
from requests.sessions import session
from fake_useragent import UserAgent
from lxml import etree


session = requests.session()


def get_user_id(user_home_page_url: str) -> str:
    '''
    获取知乎用户id信息
    '''
    logging.info('Try to get ')
    _crawl_user_page(user_home_page_url)


def _crawl_user_page(user_home_page_url):
    ua = UserAgent()
    headers = {
        'authority': 'www.zhihu.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.chrome,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': r'https://www.baidu.com/s?wd=%E7%9F%A5%E4%B9%8E',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    response = session.get(user_home_page_url, headers=headers)
    _html = response.text
    return _html
