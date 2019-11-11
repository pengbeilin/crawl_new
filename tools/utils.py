#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Version : python3.6
@Author  : Pengbl
@Time    : 2019/1/28 16:16
@Describe: 工具类
"""
import time

from tools.logutil import i


class Utils:
    @staticmethod
    def sleep(s):
        i("等待 %s" % s)
        time.sleep(s)
