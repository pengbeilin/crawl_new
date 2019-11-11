#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Version : python3.6
@Author  : Song Yancong
@Time    : 2019/1/25 2019/1/25 14:33
@Describe: 常量类
"""
import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CHROME_DRIVER_PATH = os.path.join(BASE_PATH, 'driver', 'chromedriver.exe')
