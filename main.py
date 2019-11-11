#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 3.6
@author: pengbeilin
@file: main.py
@time: 2019/10/28 16:10
"""
from model.get_tencent_news import get_news
from model.get_zhihu_hot_list import get_hot_list_des

if __name__ == '__main__':
    get_news()
    get_hot_list_des()